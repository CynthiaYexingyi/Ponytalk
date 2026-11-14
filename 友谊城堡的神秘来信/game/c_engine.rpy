################################################################################
##  游戏流程：章节循环、对话、答题、星星、魔法字母拼拼乐
##  （一般不用改；改文案请改 d_story.rpy，改界面请改 b_ui.rpy）
##
##  v3.0 变化：
##    · 填词题从「26 键打字」升级为「魔法字母拼拼乐」——
##      散落的字母块 + 少量干扰字母，点进句子的空格槽，拼对才让信发光。
##    · 新增 choice（轻互动选择）、report（章末友谊报告）两种节拍。
##    · 题目可带 after：答对后推进剧情；拼对后出题小马会说一句欢呼台词。
################################################################################

default persistent.chapter_stars = {}
default persistent.story_version = 0


init 10 python:

    ## 把路径注册成图片名，这样 renpy.show / scene 才能正确显示
    for _k, _v in PONY.items():
        renpy.image("pony_" + _k, _v["img"])

    for _bg in ("title", "meadow", "farm", "forest", "garden", "rainbow", "party", "ending", "friends"):
        renpy.image("bg_" + _bg, "images/bg/" + _bg + ".png")


init python:

    import string as _string

    cur_pony = None

    ## 自动化自测用开关：为 True 时跳过章节结算界面（正常游戏请勿修改）
    TEST_SKIP_UI = False

    ## ------------------------------------------------------------------
    ## 进度
    ## ------------------------------------------------------------------

    def init_run():
        global cur_pony
        cur_pony = None
        ## 新剧情（神秘来信篇）题目数量与旧版不同，自动重置一次进度
        if persistent.story_version != 3:
            persistent.chapter_stars = {}
            persistent.story_version = 3

    def chapter_stars(num):
        return persistent.chapter_stars.get(str(num), 0)

    def all_done():
        return all(str(i) in persistent.chapter_stars for i in range(1, len(CHAPTERS) + 1))

    def total_stars():
        return sum(persistent.chapter_stars.values())

    def reset_progress():
        persistent.chapter_stars = {}

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
    ## 选句子题
    ## ------------------------------------------------------------------

    def set_sprite_pose(z):
        global cur_pony
        if cur_pony is None:
            return
        renpy.show("pony_" + cur_pony, at_list=[z], tag="pony")

    def ask_quiz(ch, q):
        """弹出答题卡，返回答题次数（1 = 一次答对）。"""
        pony_focus(q["who"])
        set_sprite_pose(pony_quiz_pose(q["who"]))

        attempts = renpy.call_screen(
            "pony_quiz",
            ch=ch,
            scene_cn=q["scene"],
            ask_cn=q["ask"],
            options=q["options"],
            answer=q["answer"],
            explain=q["explain"],
            tip=q.get("tip", ""),
        )

        restore_pose()
        return attempts

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

    def spell_submit():
        """确认 / 施放友谊魔法：把当前拼好的单词交回引擎判定。"""
        if not spell_filled():
            return
        renpy.return_statement(("submit", spell_guess()))

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
        """弹出魔法字母拼拼乐，返回答题次数（1 = 第一次就拼对）。"""
        global spell

        pony_focus(q["who"])
        set_sprite_pose(pony_quiz_pose(q["who"]))

        build_spell(q["answer"])
        attempt = 0
        feedback = None

        while True:
            result = renpy.call_screen(
                "pony_fill",
                ch=ch,
                q=q,
                spell=spell,
                feedback=feedback,
            )

            action = result[0]

            if action == "submit":
                guess = result[1] or ""
                attempt += 1
                if norm_answer(guess) == norm_answer(q["answer"]):
                    feedback = ("right", attempt)
                    renpy.play("sfx/correct.wav", channel="sound")
                else:
                    feedback = ("wrong", guess, common_prefix(guess, q["answer"]))
                    renpy.play("sfx/wrong.wav", channel="sound")
                    clear_spell_slots()

            elif action == "hint":
                spell_hint()

            elif action == "shuffle":
                spell_shuffle()

            elif action == "clear":
                spell_clear()

            elif action == "retry":
                feedback = None
                clear_spell_slots()

            elif action == "done":
                restore_pose()
                return attempt if attempt > 0 else 1


################################################################################
## 开场：友谊城堡的神秘来信
################################################################################

label start:

    $ init_run()

    $ renpy.scene()
    $ renpy.show("bg_title")
    with fade

    $ pony_focus("twilight")
    $ pony_say("twilight", "Hello! I'm Princess Twilight Sparkle.", "你好！我是紫悦公主。")
    $ pony_say("twilight", "Welcome to the Castle of Friendship in Ponyville!", "欢迎来到小马谷的友谊城堡！")
    $ pony_narr("每周，紫悦都要给宇宙公主寄一封「友谊报告」，说说小马谷这一周学到了什么关于友谊的事。")
    $ pony_narr("送信的活儿，一直是小龙穗龙干的：他呼地吐一口龙火，信就飞去坎特洛特了。")
    $ pony_narr("可是今天早上，紫悦在书桌上发现的不是报告，而是一封怪信——")
    $ pony_say("twilight", "The paper is burnt, the letters are all mixed up… and there is NO name on it!", "纸边烧焦了，字母全乱成一团……而且，上面没有署名！")
    $ pony_narr("穗龙站在壁炉边，把一封信悄悄藏到背后，尾巴尖冒了一小缕烟，假装在看天花板。")
    $ pony_narr("就在这时，城堡中央的友谊地图亮了起来：六个小光点，指向小马谷的六个地方。")
    $ pony_say("twilight", "The map is calling. Six little friendship troubles need fixing.", "地图在召唤我们。有六个小小的友谊麻烦，等着我们去帮忙。")
    $ pony_narr("奇怪的事发生了：每当你说对一句英语、拼对一个单词，那封怪信上就会自己浮出一个字母。")
    $ pony_say("twilight", "Clover, will you come with me? Let's read the letter back together.", "Clover，愿意和我一起吗？我们把它一句一句读回来。")
    $ pony_narr("路上会遇到两件事：听小马说话，选出最合适的句子；还有——把信上散落的魔法字母拼回原样。")
    $ pony_narr("拼不出来也完全没关系，点「小提示」会给你首字母、字母数，还会帮你点亮一个字母。")

    $ pony_choice("紫悦把斗篷递给你：「出发前，你想先说哪一句？」", [
        ("「Hello! I'm Clover.」", "紫悦眼睛一亮：「说得真好！一句 Hello，就是一封报告的开端。」"),
        ("「Let's go!」", "紫悦笑着点头：「干脆利落，很有云宝的风格！我们出发！」"),
    ])

    $ pony_say("twilight", "Ready? The first light spot is at Sugarcube Corner!", "准备好了吗？第一个光点在方糖角落！")

    jump chapter_hub


################################################################################
## 选关
################################################################################

label chapter_hub:

    $ cur_pony = None
    hide screen hud
    $ renpy.scene()
    $ renpy.show("bg_title")
    with dissolve

    call screen chapter_pick

    $ picked = _return

    if picked == "back":
        $ renpy.full_restart()

    call play_chapter(picked) from _call_play_chapter

    if all_done():
        jump ending

    jump chapter_hub


################################################################################
## 一章的流程
################################################################################

label play_chapter(ch_num):

    $ ch = CHAPTERS[ch_num - 1]
    $ cur_pony = None
    $ star_total = len([b for b in ch["beats"] if b[0] in ("quiz", "fill")])
    $ star_now = 0

    $ renpy.scene()
    $ renpy.show("bg_" + ch["bg"])
    with dissolve

    show screen hud(ch, star_now, star_total)

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
            $ renpy.call_screen("friendship_report", ch=ch, title=beat[1], body=beat[2])

        elif beat[0] == "quiz":

            $ attempts = ask_quiz(ch, beat[1])

            if attempts == 1:
                $ star_now += 1
                $ renpy.show_screen("hud", ch=ch, star_now=star_now, star_total=star_total)
                $ renpy.notify("一次答对，得到 1 颗星！")
            else:
                $ renpy.show_screen("hud", ch=ch, star_now=star_now, star_total=star_total)

            $ play_after(beat[1])

        elif beat[0] == "fill":

            $ attempts = ask_fill(ch, beat[1])

            if attempts == 1:
                $ star_now += 1
                $ renpy.show_screen("hud", ch=ch, star_now=star_now, star_total=star_total)
                $ renpy.notify("一次拼对，得到 1 颗星！")
            else:
                $ renpy.show_screen("hud", ch=ch, star_now=star_now, star_total=star_total)

            $ cheer_for(beat[1])
            $ play_after(beat[1])

    hide screen hud

    $ persistent.chapter_stars[str(ch_num)] = max(chapter_stars(ch_num), star_now)

    if not TEST_SKIP_UI:
        call screen chapter_done(ch, star_now)

    return


################################################################################
## 结局
################################################################################

label ending:

    $ cur_pony = None
    hide screen hud

    $ renpy.scene()
    $ renpy.show("bg_friends")
    with fade

    call screen the_end(total_stars())

    $ ending_choice = _return

    if ending_choice == "again":
        $ reset_progress()
        jump start

    $ renpy.full_restart()
