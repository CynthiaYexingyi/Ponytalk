################################################################################
##  游戏流程：课程册 → 课时循环、对话、答题、星星、魔法字母拼拼乐
##
##  v6.0（2026-11 重做）
##  ------------------------------------------------------------------
##  · 答题拆成「选卡页 → 结果页」两步，任何一条路径都必定出现
##    「答对啦 / 再想一想」的结果提示，不会再出现「点了没反应」。
##  · 修掉了老版本的大 bug：魔法字母题用 renpy.return_statement 交卷，
##    会直接跳出整个课时（play_lesson 被 return 掉），所以拼词题永远
##    看不到「拼对啦」的提示、后面的剧情也全部断掉。现在统一用
##    屏幕的 Return 动作把结果交回引擎。
##  · 每题带倒计时（选句 45 秒 / 拼词 90 秒），答得快有速度加分。
##  · 每答对一题点亮一个发光字母，整册累计，HUD 里实时看得见。
##  · 课时结算显示每题用时、得分明细和点亮后的单词。
##
##  （游戏逻辑改这里；改故事请改 tools/story_book*.py，改界面请改 b_ui.rpy）
################################################################################

default persistent.pack_stars = {}
default persistent.intro_seen = {}
default persistent.story_version = 0
## 当前课程册。v6.0 的册 id 是 school / sugar / library / lantern，
## 旧版本残留的 "letter" 已经不存在了 —— 这里必须用真实存在的 id，
## 否则全新安装或旧存档升级后 cur_pack() 会直接 KeyError。
default persistent.last_pack_id = "school"
default current_pack_id = "school"

## 每道题的时间上限（秒）
define TIME_QUIZ = 45
define TIME_FILL = 90

## 计分规则
define SCORE_BASE = 10        ## 一次答对的基础分
define SCORE_SPEED = 5        ## 速度加分上限
define SCORE_WRONG = 3        ## 答错也有参与分
define SCORE_TIMEOUT = 2      ## 超时的安慰分


init 10 python:

    ## 把路径注册成图片名，这样 renpy.show / scene 才能正确显示
    for _pony_key, _pony_info in PONY.items():
        renpy.image("pony_" + _pony_key, _pony_info["img"])

    for _bg_name in ("title", "meadow", "farm", "forest", "garden", "rainbow", "party", "ending", "friends"):
        renpy.image("bg_" + _bg_name, "images/bg/" + _bg_name + ".png")


init python:

    import string as _string
    import time as _time

    cur_pony = None

    ## 自动化自测用开关：为 True 时跳过章节结算界面（正常游戏请勿修改）
    TEST_SKIP_UI = False

    ## ------------------------------------------------------------------
    ## 课程册 / 进度
    ## ------------------------------------------------------------------

    def set_pack(pack_id):
        """切换当前课程册，并记住下次启动默认打开哪一册。"""
        global current_pack_id
        if pack_id in PACKS_BY_ID:
            current_pack_id = pack_id
            persistent.last_pack_id = pack_id

    def cur_pack():
        """当前课程册的数据字典。"""
        return PACKS_BY_ID[current_pack_id]

    def pack_by_id(pack_id):
        return PACKS_BY_ID[pack_id]

    def init_run():
        global cur_pony, current_pack_id
        cur_pony = None
        ## v6.0：评分与发光字母机制升级，旧存档不兼容，自动重置一次
        if persistent.story_version != 6:
            persistent.pack_stars = {}
            persistent.intro_seen = {}
            persistent.story_version = 6
        ## 存档里的册 id 可能来自旧版本（"letter" 等），认不出来就退回第一册
        if persistent.last_pack_id in PACKS_BY_ID:
            current_pack_id = persistent.last_pack_id
        else:
            first_id = STORY_PACKS[0]["id"]
            current_pack_id = first_id
            persistent.last_pack_id = first_id

    def pack_stars_map(pack_id=None):
        """某一册的 {课时号: 星数} 字典（返回副本，避免 persistent 嵌套不保存）。"""
        pid = pack_id or current_pack_id
        return dict(persistent.pack_stars.get(pid, {}))

    def lesson_stars(num, pack_id=None):
        return pack_stars_map(pack_id).get(str(num), 0)

    def lesson_done(num, pack_id=None):
        return str(num) in pack_stars_map(pack_id)

    def save_lesson(num, stars):
        """保存一课时的星星，取历史最高分。"""
        m = pack_stars_map()
        m[str(num)] = max(m.get(str(num), 0), stars)
        all_map = dict(persistent.pack_stars)
        all_map[current_pack_id] = m
        persistent.pack_stars = all_map

    def pack_done_count(pack_id=None):
        return len(pack_stars_map(pack_id))

    def pack_total_lessons(pack_id=None):
        return len(pack_by_id(pack_id or current_pack_id)["lessons"])

    def pack_total_stars(pack_id=None):
        return sum(pack_stars_map(pack_id).values())

    def pack_question_count(pack_id=None):
        return pack_by_id(pack_id or current_pack_id)["qcount"]

    def all_done():
        return pack_done_count() >= pack_total_lessons()

    def total_stars():
        return pack_total_stars()

    def reset_progress(pack_id=None):
        """重玩：只清当前册（或指定册）的进度，其它册不受影响。"""
        pid = pack_id or current_pack_id
        all_map = dict(persistent.pack_stars)
        all_map[pid] = {}
        persistent.pack_stars = all_map
        seen = dict(persistent.intro_seen)
        seen.pop(pid, None)
        persistent.intro_seen = seen

    ## 序章每册只自动播放一次；换册时第一次进入会看到完整开场
    def intro_needed(pack_id=None):
        return (pack_id or current_pack_id) not in persistent.intro_seen

    def mark_intro(pack_id=None):
        seen = dict(persistent.intro_seen)
        seen[pack_id or current_pack_id] = True
        persistent.intro_seen = seen

    ## ------------------------------------------------------------------
    ## 对话 / 立绘
    ## ------------------------------------------------------------------

    def pony_pose(key):
        """默认站位：友谊之光飘在空中，其它小马站在右边。"""
        return pony_star if key == "star" else pony_right

    def pony_quiz_pose(key):
        return pony_star_quiz if key == "star" else pony_right_quiz

    def pony_focus(key):
        global cur_pony
        if cur_pony == key:
            return
        renpy.show("pony_" + key, at_list=[pony_pose(key)], tag="pony")
        cur_pony = key

    def restore_pose():
        """答题结束后把立绘放回默认站位。"""
        if cur_pony is None:
            return
        renpy.show("pony_" + cur_pony, at_list=[pony_pose(cur_pony)], tag="pony")

    def pony_say(key, en, zh=""):
        pony_focus(key)
        text = en
        if zh:
            text = en + "\n{size=30}{color=#8b7f96}" + zh + "{/color}{/size}"
        renpy.say(CHARS[key], text)

    def pony_narr(zh):
        renpy.say(None, zh)

    ## ------------------------------------------------------------------
    ## 剧情附加节拍
    ## ------------------------------------------------------------------

    def play_after(q):
        """答对之后的剧情：可以是一句旁白，也可以是一句小马台词。"""
        a = q.get("after")
        if not a:
            return
        if isinstance(a, str):
            pony_narr(a)
        elif a[0] == "say":
            pony_say(a[1], a[2], a[3])
        elif a[0] == "narr":
            pony_narr(a[1])

    def play_pack_intro():
        """播放当前册的序章：只有 scene / narr / say / choice 四种节拍。"""
        global cur_pony
        cur_pony = None
        for beat in cur_pack()["intro"]:
            if beat[0] == "scene":
                renpy.scene()
                renpy.show("bg_" + beat[1])
            elif beat[0] == "say":
                pony_say(beat[1], beat[2], beat[3])
            elif beat[0] == "narr":
                pony_narr(beat[1])
            elif beat[0] == "choice":
                pony_choice(beat[1], beat[2])

    ## 拼对单词后，出题小马的一句欢呼（每次随机，小朋友不会听腻）
    CHEERS = {
        "twilight": [
            ("Perfect! The letters are all in order!", "太好了！字母全都归位了！"),
            ("A plus spelling, Clover!", "拼写满分，Clover！"),
            ("Look! The letter is glowing again!", "看！信又亮起来一点啦！"),
        ],
        "pinkie": [
            ("YAY! The word popped like confetti!", "耶！单词像彩带一样蹦出来啦！"),
            ("That is the most fun word EVER!", "这是最好玩的单词啦！"),
            ("One more word for the cake!", "又多一个单词，加一块蛋糕！"),
        ],
        "applejack": [
            ("That is honest-to-goodness right!", "这可真是实打实地拼对啦！"),
            ("Good work, partner!", "干得好，伙伴！"),
            ("Now that is a fine word.", "这词拼得真漂亮。"),
        ],
        "rainbow": [
            ("Nice! Ten out of ten!", "漂亮！满分十分！"),
            ("Faster than a rainboom!", "比彩虹音爆还快！"),
            ("Awesomely spelled!", "拼得超帅！"),
        ],
        "rarity": [
            ("Simply gorgeous spelling!", "这拼写真是太优雅了！"),
            ("Darling, you are a natural!", "亲爱的，你天生就会嘛！"),
            ("Every letter is in its place.", "每个字母都待在该待的位置。"),
        ],
        "fluttershy": [
            ("Oh… you did it. Wonderful.", "呀……你做到了。真好。"),
            ("That was very gentle. Thank you.", "好轻柔呀，谢谢你。"),
            ("The little fox is clapping too.", "小狐狸也在拍手呢。"),
        ],
        "star": [
            ("Twinkle! You got it!", "叮！你拼对啦！"),
            ("One more letter is shining!", "又亮了一个字母！"),
        ],
    }

    def cheer_for(q):
        custom = q.get("cheer")
        if custom:
            pony_narr(custom)
            return
        key = q["who"]
        en, zh = renpy.random.choice(CHEERS.get(key, CHEERS["twilight"]))
        pony_say(key, en, zh)

    def pony_choice(question, opts):
        """轻互动：选一句，小马回一句。不计分，也不影响剧情走向。"""
        idx = renpy.call_screen("pony_choice", question=question, options=opts)
        if idx is None:
            idx = 0
        pony_narr(opts[idx][1])

    ## ------------------------------------------------------------------
    ## 计时与计分
    ## ------------------------------------------------------------------

    _deadline = {"quiz": 0.0, "fill": 0.0}

    def start_timer(kind, seconds):
        """给某道题开始倒计时（用绝对时间，界面重绘不会影响计时）。"""
        _deadline[kind] = _time.time() + seconds

    def time_left(kind):
        return max(0.0, _deadline[kind] - _time.time())

    def time_used(kind, limit):
        return max(0.0, limit - time_left(kind))

    def tick_timer(kind):
        """屏幕心跳：让倒计时显示保持新鲜。"""
        renpy.restart_interaction()

    def speed_bonus(kind, limit):
        """速度加分：剩余时间越多分越高，最多 SCORE_SPEED 分。"""
        left = time_left(kind)
        return int(round(SCORE_SPEED * max(0.0, min(1.0, left / float(limit)))))

    ## ------------------------------------------------------------------
    ## 选句子题
    ## ------------------------------------------------------------------

    def set_sprite_pose(z):
        global cur_pony
        if cur_pony is None:
            return
        renpy.show("pony_" + cur_pony, at_list=[z], tag="pony")

    def ask_quiz(ch, q):
        """
        选句子题。
        返回 {"attempts": 次数, "right": 是否答对, "used": 用了几秒,
              "score": 得分, "limit": 时间上限, "timed_out": 是否超时}
        """
        pony_focus(q["who"])
        set_sprite_pose(pony_quiz_pose(q["who"]))

        attempts = 0
        used = 0.0
        limit = TIME_QUIZ

        while True:
            start_timer("quiz", limit)
            result = renpy.call_screen("pony_quiz", ch=ch, q=q)

            ## 超时：直接给出正确答案，故事继续
            if result[0] == "timeout":
                used = limit
                renpy.call_screen("pony_quiz_result", q=q, ok=False, timeout=True,
                                  picked=None, used=used, limit=limit, score=SCORE_TIMEOUT)
                return {"attempts": attempts, "right": False, "used": used,
                        "score": SCORE_TIMEOUT, "limit": limit, "timed_out": True}

            picked = result[1]
            attempts += 1
            used = time_used("quiz", limit)

            if picked == q["answer"]:
                score = SCORE_BASE + speed_bonus("quiz", limit)
                renpy.call_screen("pony_quiz_result", q=q, ok=True, timeout=False,
                                  picked=picked, used=used, limit=limit, score=score)
                return {"attempts": attempts, "right": True, "used": used,
                        "score": score, "limit": limit, "timed_out": False}

            ## 答错：告诉小朋友错在哪，再来一次
            renpy.call_screen("pony_quiz_result", q=q, ok=False, timeout=False,
                              picked=picked, used=used, limit=limit, score=SCORE_WRONG)

    ## ------------------------------------------------------------------
    ## 魔法字母拼拼乐
    ##
    ##  spell = {
    ##      "answer"    : 小写答案，例如 "o'clock"
    ##      "fixed"     : {位置: 固定符号}，例如 o'clock 的撇号已经镶在信上
    ##      "slots"     : 每个位置放 tile 的 id，None 表示空槽
    ##      "tiles"     : 字母块列表，id 就是下标，永不改变
    ##      "pool_order": 字母块在池子里的显示顺序（可重排）
    ##      "hint"      : 已用第几级提示
    ##      "hidden"    : 被提示「变走」的干扰字母 id
    ##  }
    ## ------------------------------------------------------------------

    spell = None

    def _spell_refresh():
        renpy.restart_interaction()

    def build_spell(answer):
        """为这道拼词题造一批打乱的字母块（含 1~2 个干扰字母）。"""
        global spell
        ans = str(answer).lower()
        fixed = dict((i, c) for i, c in enumerate(ans) if not c.isalpha())
        letters = [c for c in ans if c.isalpha()]

        others = [c for c in _string.ascii_lowercase if c not in letters]
        renpy.random.shuffle(others)
        extra = others[:2]

        bag = letters + extra
        renpy.random.shuffle(bag)
        tiles = [{"id": i, "ch": c, "used": False} for i, c in enumerate(bag)]
        pool_order = [t["id"] for t in tiles]
        renpy.random.shuffle(pool_order)

        spell = {
            "answer": ans,
            "fixed": fixed,
            "slots": [None] * len(ans),
            "tiles": tiles,
            "pool_order": pool_order,
            "hint": 0,
            "hidden": [],
        }

    def spell_filled():
        """所有字母槽都填满了吗（固定符号位不算）。"""
        if spell is None:
            return False
        for i, tid in enumerate(spell["slots"]):
            if i in spell["fixed"]:
                continue
            if tid is None:
                return False
        return True

    def spell_guess():
        """按槽位读出当前拼出来的字符串。"""
        if spell is None:
            return ""
        out = []
        for i, tid in enumerate(spell["slots"]):
            if i in spell["fixed"]:
                out.append(spell["fixed"][i])
            elif tid is None:
                out.append("")
            else:
                out.append(spell["tiles"][tid]["ch"])
        return "".join(out)

    def clear_spell_slots():
        """把字母全部退回池子（固定符号保留）。"""
        if spell is None:
            return
        for i in range(len(spell["slots"])):
            spell["slots"][i] = None
        for t in spell["tiles"]:
            t["used"] = False

    def spell_place(tile_id):
        """点字母块 → 放进第一个空槽。"""
        if spell is None:
            return
        t = spell["tiles"][tile_id]
        if t["used"] or tile_id in spell["hidden"]:
            return
        for i, tid in enumerate(spell["slots"]):
            if i in spell["fixed"]:
                continue
            if tid is None:
                spell["slots"][i] = tile_id
                t["used"] = True
                break
        _spell_refresh()

    def spell_remove(slot_idx):
        """点已填的槽 → 字母退回池子。"""
        if spell is None:
            return
        if slot_idx in spell["fixed"]:
            return
        tid = spell["slots"][slot_idx]
        if tid is None:
            return
        spell["tiles"][tid]["used"] = False
        spell["slots"][slot_idx] = None
        _spell_refresh()

    def spell_clear():
        clear_spell_slots()
        _spell_refresh()

    def spell_shuffle():
        renpy.random.shuffle(spell["pool_order"])
        _spell_refresh()

    def spell_type(ch):
        """键盘打字也能玩：按字母键，把池子里对应的字母放进空槽。"""
        if spell is None:
            return
        for t in spell["tiles"]:
            if (not t["used"]) and (t["id"] not in spell["hidden"]) and t["ch"] == ch:
                spell_place(t["id"])
                return

    def spell_pop():
        """退格：把最后一个放进去的字母退回池子。"""
        if spell is None:
            return
        for i in range(len(spell["slots"]) - 1, -1, -1):
            if i in spell["fixed"]:
                continue
            if spell["slots"][i] is not None:
                spell_remove(i)
                return

    def spell_auto_one():
        """提示：自动点亮第一个还空着的正确字母。"""
        if spell is None:
            return False
        ans = spell["answer"]
        for i in range(len(ans)):
            if i in spell["fixed"] or spell["slots"][i] is not None:
                continue
            need = ans[i]
            cand = [t for t in spell["tiles"]
                    if (not t["used"]) and (t["id"] not in spell["hidden"]) and t["ch"] == need]
            if not cand:
                ## 这个字母被小朋友放到别处了，把它挪回来
                for t in spell["tiles"]:
                    if t["used"] and t["ch"] == need:
                        for j, tid in enumerate(spell["slots"]):
                            if tid == t["id"]:
                                spell["slots"][j] = None
                                break
                        t["used"] = False
                        cand = [t]
                        break
            if not cand:
                return False
            t = cand[0]
            t["used"] = True
            spell["slots"][i] = t["id"]
            return True
        return False

    def spell_hide_extra():
        """提示：让一个干扰字母「嗖」地飞走。"""
        if spell is None:
            return
        letters = set(c for c in spell["answer"] if c.isalpha())
        for t in spell["tiles"]:
            if (not t["used"]) and (t["id"] not in spell["hidden"]) and (t["ch"] not in letters):
                spell["hidden"].append(t["id"])
                return

    def spell_hint():
        """分级提示：① 首字母+长度 ② 点亮一个字母 ③ 飞走一个干扰字母 ④ 继续点亮。"""
        if spell is None:
            return
        spell["hint"] += 1
        if spell["hint"] == 2:
            spell_auto_one()
        elif spell["hint"] == 3:
            spell_hide_extra()
        elif spell["hint"] >= 4:
            spell_auto_one()
        _spell_refresh()

    def norm_answer(s):
        """比较答案：忽略大小写、空格和标点（o'clock 也能算对）。"""
        return "".join(ch for ch in str(s).lower() if ch.isalnum())

    def common_prefix(a, b):
        """答错时告诉小朋友：前面已经有几个字母排对了。"""
        x, y = norm_answer(a), norm_answer(b)
        n = 0
        for p, q in zip(x, y):
            if p != q:
                break
            n += 1
        return n

    def ask_fill(ch, q):
        """
        魔法字母拼拼乐。
        返回 {"attempts": 次数, "right": 是否拼对, "used": 用了几秒,
              "score": 得分, "limit": 时间上限, "timed_out": 是否超时}
        """
        global spell

        pony_focus(q["who"])
        set_sprite_pose(pony_quiz_pose(q["who"]))

        build_spell(q["answer"])
        attempts = 0
        limit = TIME_FILL

        while True:
            start_timer("fill", limit)
            result = renpy.call_screen("pony_fill", ch=ch, q=q, spell=spell)

            if result[0] == "timeout":
                renpy.call_screen("pony_fill_result", q=q, ok=False, timeout=True,
                                  guess=None, prefix=0, used=limit, limit=limit,
                                  score=SCORE_TIMEOUT)
                return {"attempts": attempts, "right": False, "used": limit,
                        "score": SCORE_TIMEOUT, "limit": limit, "timed_out": True}

            guess = result[1] or ""
            attempts += 1
            used = time_used("fill", limit)

            if norm_answer(guess) == norm_answer(q["answer"]):
                score = SCORE_BASE + speed_bonus("fill", limit)
                renpy.call_screen("pony_fill_result", q=q, ok=True, timeout=False,
                                  guess=guess, prefix=0, used=used, limit=limit, score=score)
                return {"attempts": attempts, "right": True, "used": used,
                        "score": score, "limit": limit, "timed_out": False}

            prefix = common_prefix(guess, q["answer"])
            renpy.call_screen("pony_fill_result", q=q, ok=False, timeout=False,
                              guess=guess, prefix=prefix, used=used, limit=limit,
                              score=SCORE_WRONG)
            ## 拼错了，字母退回池子，再来一次
            clear_spell_slots()
            spell["hint"] = 0
            spell["hidden"] = []
            _spell_refresh()

    ## ------------------------------------------------------------------
    ## 发光字母
    ## ------------------------------------------------------------------

    def lesson_word(ch):
        """本课时要点亮的单词（没有就用一个默认的）。"""
        w = (ch.get("word") or "").strip().upper()
        if not w:
            return "★"
        return w

    def light_letter(ch, index):
        """
        第 index 个答对的题目点亮单词里的第 index 个字母。
        返回被点亮的字母（点完了返回 "★"）。
        """
        w = lesson_word(ch)
        if index < len(w):
            return w[index]
        return "★"

    def show_letter_glow(ch, letter, index, total):
        """播放「一个字母亮起来」的瞬间。"""
        renpy.call_screen("letter_glow", ch=ch, letter=letter, index=index, total=total)

    def pack_letters_got(pack_id=None):
        """本册累计点亮的字母数（= 该册历史最高分之和）。"""
        return pack_total_stars(pack_id)


################################################################################
## 开场：选课程册 → 播序章 → 进课时表
################################################################################

label start:

    $ init_run()

    jump pack_select


################################################################################
## 选择课程册（主菜单「开始上课」与课时表「切换课程册」都会来这里）
################################################################################

label pack_select:

    $ cur_pony = None
    hide screen hud
    $ renpy.scene()
    $ renpy.show("bg_title")
    with dissolve

    call screen pack_pick

    $ picked = _return

    if picked == "back":
        $ renpy.full_restart()

    $ set_pack(picked)

    call maybe_intro from _call_maybe_intro

    jump lesson_hub


################################################################################
## 序章：每册只自动播放一次，重新进来直接上课
################################################################################

label maybe_intro:

    if intro_needed():
        $ play_pack_intro()
        $ mark_intro()

    return


################################################################################
## 课时表
################################################################################

label lesson_hub:

    $ init_run()
    $ cur_pony = None
    hide screen hud
    $ renpy.scene()
    $ renpy.show("bg_" + cur_pack()["bg"])
    with dissolve

    call screen lesson_pick

    $ picked = _return

    if picked == "back":
        $ renpy.full_restart()

    if picked == "switch":
        jump pack_select

    call play_lesson(picked) from _call_play_lesson

    if all_done():
        jump pack_ending

    jump lesson_hub


################################################################################
## 一节课的流程
################################################################################

label play_lesson(lesson_num):

    $ pack = cur_pack()
    $ ch = pack["lessons"][lesson_num - 1]
    $ cur_pony = None
    $ star_total = len([b for b in ch["beats"] if b[0] in ("quiz", "fill")])
    $ star_now = 0
    $ score_now = 0
    $ q_index = 0
    $ results = []
    $ word = lesson_word(ch)

    $ renpy.scene()
    $ renpy.show("bg_" + ch["bg"])
    with dissolve

    show screen hud(pack, ch, star_now, star_total, score_now, word, q_index)

    $ bi = 0

    while bi < len(ch["beats"]):

        $ beat = ch["beats"][bi]
        $ bi += 1

        if beat[0] == "say":
            $ pony_say(beat[1], beat[2], beat[3])

        elif beat[0] == "narr":
            $ pony_narr(beat[1])

        elif beat[0] == "scene":
            $ renpy.scene()
            $ renpy.show("bg_" + beat[1])
            with dissolve

        elif beat[0] == "choice":
            $ pony_choice(beat[1], beat[2])

        elif beat[0] == "report":
            $ renpy.call_screen("friendship_report", pack=pack, ch=ch, title=beat[1], body=beat[2])

        elif beat[0] == "quiz" or beat[0] == "fill":

            $ q_index += 1

            if beat[0] == "quiz":
                $ res = ask_quiz(ch, beat[1])
            else:
                $ res = ask_fill(ch, beat[1])

            $ score_now += res["score"]

            if res["right"] and res["attempts"] == 1:
                $ star_now += 1
                $ letter = light_letter(ch, star_now - 1)
                $ show_letter_glow(ch, letter, star_now - 1, star_total)
                $ renpy.show_screen("hud", pack=pack, ch=ch, star_now=star_now,
                                    star_total=star_total, score_now=score_now,
                                    word=word, q_index=q_index)
            else:
                $ renpy.show_screen("hud", pack=pack, ch=ch, star_now=star_now,
                                    star_total=star_total, score_now=score_now,
                                    word=word, q_index=q_index)

            $ results.append({"no": q_index, "kind": beat[0], "right": res["right"],
                              "used": res["used"], "score": res["score"],
                              "star": res["right"] and res["attempts"] == 1,
                              "timeout": res["timed_out"]})

            if beat[0] == "fill":
                $ cheer_for(beat[1])

            $ play_after(beat[1])

    hide screen hud

    $ save_lesson(ch["num"], star_now)

    if not TEST_SKIP_UI:
        call screen lesson_done(pack, ch, star_now, score_now, results, word)

    return


################################################################################
## 本册结局
################################################################################

label pack_ending:

    $ cur_pony = None
    hide screen hud

    $ renpy.scene()
    $ renpy.show("bg_friends")
    with fade

    $ end_pack = cur_pack()
    $ end_stars = total_stars()

    call screen the_end(end_pack, end_stars)

    $ ending_choice = _return

    if ending_choice == "again":
        $ reset_progress()
        jump start

    if ending_choice == "switch":
        jump pack_select

    $ renpy.full_restart()
