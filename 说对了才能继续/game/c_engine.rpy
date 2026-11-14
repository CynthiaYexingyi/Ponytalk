################################################################################
##  游戏流程：章节循环、对话、答题、星星
##  （一般不用改；改文案请改 d_story.rpy）
################################################################################

default persistent.chapter_stars = {}


init 10 python:

    ## 把路径注册成图片名，这样 renpy.show / scene 才能正确显示
    for _k, _v in PONY.items():
        renpy.image("pony_" + _k, _v["img"])

    for _bg in ("title", "meadow", "farm", "forest", "garden", "rainbow", "party", "ending", "friends"):
        renpy.image("bg_" + _bg, "images/bg/" + _bg + ".png")


init python:

    cur_pony = None

    ## ------------------------------------------------------------------
    ## 进度
    ## ------------------------------------------------------------------

    def init_run():
        global cur_pony
        cur_pony = None

    def chapter_stars(num):
        return persistent.chapter_stars.get(str(num), 0)

    def all_done():
        return all(str(i) in persistent.chapter_stars for i in range(1, 7))

    def total_stars():
        return sum(persistent.chapter_stars.values())

    def reset_progress():
        persistent.chapter_stars = {}

    ## ------------------------------------------------------------------
    ## 对话 / 立绘
    ## ------------------------------------------------------------------

    def pony_focus(key):
        global cur_pony
        if cur_pony == key:
            return
        renpy.show("pony_" + key, at_list=[pony_right], tag="pony")
        cur_pony = key

    def pony_say(key, en, zh=""):
        pony_focus(key)
        text = en
        if zh:
            text = en + "\n{size=30}{color=#8b7f96}" + zh + "{/color}{/size}"
        renpy.say(CHARS[key], text)

    def pony_narr(zh):
        renpy.say(None, zh)

    ## ------------------------------------------------------------------
    ## 答题
    ## ------------------------------------------------------------------

    def set_sprite_pose(z):
        global cur_pony
        if cur_pony is None:
            return
        renpy.show("pony_" + cur_pony, at_list=[z], tag="pony")

    def ask_quiz(ch, q):
        """弹出答题卡，返回答题次数（1 = 一次答对）。"""
        pony_focus(q["who"])
        set_sprite_pose(pony_right_quiz)

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

        set_sprite_pose(pony_right)
        return attempts


################################################################################
## 开场
################################################################################

label start:

    $ init_run()

    $ renpy.scene()
    $ renpy.show("bg_title")
    with fade

    $ pony_focus("twilight")
    $ pony_say("twilight", "Hello! I'm Twilight Sparkle.", "你好！我是紫悦。")
    $ pony_say("twilight", "Welcome to Ponyville!", "欢迎来到小马谷！")
    $ pony_narr("今天，你要用英语和小马们一起完成六个小故事。")
    $ pony_narr("每次会出现 3 张句子卡，选出最合适的那一句，就能继续往下说。")
    $ pony_narr("选错了不要紧，我会告诉你这几句话有什么不一样。")
    $ pony_say("twilight", "Ready? Let's go!", "准备好了吗？我们出发！")

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
    $ star_total = len([b for b in ch["beats"] if b[0] == "quiz"])
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

        elif beat[0] == "quiz":

            $ attempts = ask_quiz(ch, beat[1])

            if attempts == 1:
                $ star_now += 1
                $ renpy.show_screen("hud", ch=ch, star_now=star_now, star_total=star_total)
                $ renpy.notify("一次答对，得到 1 颗星！")
            else:
                $ renpy.show_screen("hud", ch=ch, star_now=star_now, star_total=star_total)

    hide screen hud

    $ persistent.chapter_stars[str(ch_num)] = max(chapter_stars(ch_num), star_now)

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
