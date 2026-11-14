################################################################################
##  界面：主菜单 / 玩法说明 / 选章 / HUD / 答题卡 / 结算 / 结局
################################################################################

init offset = 2


################################################################################
## 公用：星星条
################################################################################

screen star_row(n, total, star_size=1.0):
    hbox:
        spacing int(8 * star_size)

        for i in range(total):
            if i < n:
                add "images/ui/star_full.png" zoom 0.62 * star_size
            else:
                add "images/ui/star_empty.png" zoom 0.62 * star_size


################################################################################
## 主菜单
################################################################################

screen main_menu():
    tag menu

    add "images/bg/title.png"

    vbox:
        xpos 120
        ypos 90
        spacing 4

        text "My Little Pony":
            font FONT_CN
            size 112
            bold True
            color "#ffffff"
            outlines [(8, "#e0407f", 0, 0)]

        text "小马宝莉　说对了才能继续":
            font FONT_CN
            size 58
            bold True
            color "#ffe8f3"
            outlines [(5, "#b23a72", 0, 0)]

        text "三年级上册　英语句子闯关":
            font FONT_CN
            size 36
            color "#ffffffdd"

    vbox:
        xpos 140
        ypos 436
        spacing 12
        style_prefix "mm"

        textbutton "开始上课" action Start()
        textbutton "选择章节" action Start("chapter_hub")
        textbutton "玩法说明" action ShowMenu("how_to_play")
        textbutton "设置" action ShowMenu("preferences")
        textbutton "退出" action Quit(confirm=False)

    text "鼠标点击即可作答，键盘 1 / 2 / 3 也可以选":
        xpos 130
        ypos 992
        font FONT_CN
        size 28
        color "#ffffffdd"


################################################################################
## 玩法说明
################################################################################

screen how_to_play():
    tag menu

    add "images/bg/title.png"
    add Solid("#2b1435aa")

    frame:
        background Frame("images/ui/panel.png", 44, 44)
        xalign 0.5
        yalign 0.5
        xsize 1320
        padding (70, 46)

        vbox:
            spacing 24

            text "怎么玩？" font FONT_CN size 64 bold True color C_PINK_DEEP

            text "① 先听小马们说话：英文句子下面有中文，看不懂也没关系。" font FONT_CN size 36 color C_TEXT
            text "② 轮到你回答时，会出现 3 张句子卡，读一读，选出最合适的那一句。" font FONT_CN size 36 color C_TEXT
            text "③ 选对了就能继续；选错了会有讲解，再试一次就好。" font FONT_CN size 36 color C_TEXT
            text "④ 一次就答对得 1 颗星，每题最多 1 颗。" font FONT_CN size 36 color C_TEXT

            textbutton "我知道啦":
                action Return()
                style "kid_button"
                text_style "kid_button_text"
                xalign 0.5


################################################################################
## 选择章节
################################################################################

screen chapter_pick():
    modal True

    add "images/bg/title.png"
    add Solid("#2b1435aa")

    text "选择章节":
        xalign 0.5
        ypos 40
        font FONT_CN
        size 76
        bold True
        color "#ffffff"
        outlines [(6, "#e0407f", 0, 0)]

    text "六个单元，六个小故事：每一关都要选出最合适的句子":
        xalign 0.5
        ypos 142
        font FONT_CN
        size 32
        color "#ffffffdd"

    grid 3 2:
        xalign 0.5
        ypos 206
        spacing 26
        xsize 1590

        for ch in CHAPTERS:

            button:
                xsize 500
                ysize 340
                background Frame("images/ui/card_idle.png", 40, 40)
                hover_background Frame("images/ui/card_hover.png", 40, 40)
                padding (30, 22)
                action Return(ch["num"])

                vbox:
                    spacing 6
                    xfill True

                    text ch["unit"]:
                        font FONT_CN
                        size 26
                        color C_PINK_DEEP
                        bold True

                    text ch["title"]:
                        font FONT_CN
                        size 44
                        color C_TEXT
                        bold True

                    text ch["goal"]:
                        font FONT_CN
                        size 22
                        color C_TEXT_SOFT
                        xmaximum 430

                    use star_row(n=persistent.chapter_stars.get(str(ch["num"]), 0), total=ch["qcount"], star_size=0.85)

                add ("images/pony/" + ch["avatar"] + ".png"):
                    xalign 1.0
                    yalign 1.0
                    xoffset 2
                    yoffset 8
                    zoom 0.19

    textbutton "返回标题":
        style "kid_button"
        text_style "kid_button_text"
        xalign 0.5
        yalign 0.965
        action Return("back")

    key "game_menu" action Return("back")


################################################################################
## HUD：章节标题 + 星星数
################################################################################

screen hud(ch, star_now, star_total):
    zorder 40

    frame:
        background Frame("images/ui/ribbon.png", 40, 40)
        xpos 40
        ypos 20
        xsize 1020
        padding (44, 10)

        text ch["unit"] + "　" + ch["title"]:
            font FONT_CN
            size 32
            color C_TEXT
            bold True

    frame:
        background Frame("images/ui/panel.png", 44, 44)
        xpos 1640
        ypos 20
        ysize 80
        padding (26, 8)

        hbox:
            spacing 10
            add "images/ui/star_full.png" zoom 0.62 yalign 0.5
            text str(star_now) + "/" + str(star_total):
                font FONT_CN
                size 36
                color C_TEXT
                bold True
                yalign 0.5


################################################################################
## 答题卡
################################################################################

init python:

    def _total_quiz_count():
        return sum(c["qcount"] for c in CHAPTERS)

    def _card_bg(idx, chosen, answer):
        if chosen is not None and idx == chosen:
            if idx == answer:
                return "images/ui/card_correct.png"
            return "images/ui/card_wrong.png"
        if chosen is not None and idx == answer:
            return "images/ui/card_correct.png"
        return "images/ui/card_idle.png"


screen pony_quiz(ch, scene_cn, ask_cn, options, answer, explain, tip, prechosen=None):
    modal True
    zorder 55

    default chosen = prechosen
    default tries = 0

    add Solid("#2b143555")

    ## 情境 + 问题
    frame:
        background Frame("images/ui/panel.png", 44, 44)
        xpos 40
        ypos 132
        xsize 1220
        padding (46, 26)

        vbox:
            spacing 10

            text scene_cn:
                font FONT_CN
                size 36
                color C_TEXT

            text ask_cn:
                font FONT_CN
                size 30
                color C_PINK_DEEP
                bold True

    ## 数字键 1 / 2 / 3 作答
    if chosen is None:
        key "1" action [Play("sound", "sfx/correct.wav" if answer == 0 else "sfx/wrong.wav"), SetScreenVariable("chosen", 0)]
        key "2" action [Play("sound", "sfx/correct.wav" if answer == 1 else "sfx/wrong.wav"), SetScreenVariable("chosen", 1)]
        key "3" action [Play("sound", "sfx/correct.wav" if answer == 2 else "sfx/wrong.wav"), SetScreenVariable("chosen", 2)]

    ## 三张句子卡
    if chosen is None:
        vbox:
            xpos 40
            ypos 420
            spacing 20
            at card_pop

            for i, opt in enumerate(options):

                button:
                    xsize 1220
                    ysize 156
                    background Frame(_card_bg(i, chosen, answer), 40, 40)
                    hover_background Frame("images/ui/card_hover.png", 40, 40)
                    padding (44, 18)
                    action [Play("sound", "sfx/correct.wav" if i == answer else "sfx/wrong.wav"), SetScreenVariable("chosen", i)]

                    hbox:
                        spacing 26
                        yalign 0.5

                        text "ABC"[i]:
                            font FONT_CN
                            size 40
                            bold True
                            color C_PINK_DEEP
                            yalign 0.5

                        text opt["en"]:
                            font FONT_CN
                            size 44
                            bold True
                            color C_TEXT
                            yalign 0.5

    ## 反馈
    if chosen is not None:

        $ is_right = (chosen == answer)
        $ picked = options[chosen]
        $ right = options[answer]

        frame:
            background Frame("images/ui/panel.png", 44, 44)
            xpos 40
            ypos 410
            xsize 1220
            ysize 600
            padding (50, 34)
            at panel_pop

            vbox:
                spacing 18

                hbox:
                    spacing 18
                    if is_right:
                        add "images/ui/check.png" zoom 0.85 yalign 0.5
                        text "太棒了！答对啦":
                            font FONT_CN
                            size 52
                            bold True
                            color C_GREEN
                            yalign 0.5
                    else:
                        add "images/ui/cross.png" zoom 0.85 yalign 0.5
                        text "再想一想～":
                            font FONT_CN
                            size 52
                            bold True
                            color C_RED
                            yalign 0.5

                if is_right:

                    text right["en"] + "　＝　" + right["zh"]:
                        font FONT_CN
                        size 38
                        bold True
                        color C_TEXT

                    text explain:
                        font FONT_CN
                        size 30
                        color C_TEXT

                    if tip:
                        text "小贴士：" + tip:
                            font FONT_CN
                            size 28
                            color C_PURPLE

                    textbutton "继续":
                        style "kid_button"
                        text_style "kid_button_text"
                        xalign 1.0
                        action [Play("sound", "sfx/star.wav"), Return(tries + 1)]

                else:

                    text "你选的是：" + picked["en"] + "（" + picked["zh"] + "）":
                        font FONT_CN
                        size 34
                        color C_TEXT

                    text picked["note"]:
                        font FONT_CN
                        size 30
                        color C_RED

                    text "应该选：" + right["en"] + "（" + right["zh"] + "）":
                        font FONT_CN
                        size 34
                        bold True
                        color C_GREEN

                    textbutton "再试一次":
                        style "kid_button"
                        text_style "kid_button_text"
                        xalign 1.0
                        action [Play("sound", "sfx/click.wav"), SetScreenVariable("chosen", None), SetScreenVariable("tries", tries + 1)]


################################################################################
## 章节结算
################################################################################

screen chapter_done(ch, stars):
    modal True
    zorder 60

    add Solid("#2b143599")

    frame:
        background Frame("images/ui/panel.png", 44, 44)
        xalign 0.5
        yalign 0.5
        xsize 1100
        padding (60, 42)
        at panel_pop

        vbox:
            spacing 24
            xalign 0.5

            text "第 " + str(ch["num"]) + " 章 完成！":
                font FONT_CN
                size 68
                bold True
                color C_PINK_DEEP
                xalign 0.5

            text ch["title"]:
                font FONT_CN
                size 38
                color C_TEXT
                xalign 0.5

            use star_row(n=stars, total=ch["qcount"], star_size=1.3)

            if stars == ch["qcount"]:
                text "全部一次答对！你是句子小达人！":
                    font FONT_CN
                    size 34
                    bold True
                    color C_GOLD
                    xalign 0.5
            elif stars >= 2:
                text "很棒！再读一遍故事，下次一定更快。":
                    font FONT_CN
                    size 34
                    color C_TEXT
                    xalign 0.5
            else:
                text "没关系，我们把这几句再读一遍，就会记住啦。":
                    font FONT_CN
                    size 34
                    color C_TEXT
                    xalign 0.5

            textbutton "继续":
                style "kid_button"
                text_style "kid_button_text"
                xalign 0.5
                action [Play("sound", "sfx/done.wav"), Return()]


################################################################################
## 结局
################################################################################

screen the_end(total_stars):
    modal True

    add "images/bg/friends.png"
    add Solid("#1d0f2aaa")

    frame:
        background Frame("images/ui/panel.png", 44, 44)
        xalign 0.5
        yalign 0.5
        xsize 1250
        padding (60, 42)
        at panel_pop

        vbox:
            spacing 22
            xalign 0.5

            text "全部通关！":
                font FONT_CN
                size 84
                bold True
                color C_PINK_DEEP
                xalign 0.5

            text "你现在已经会用六个单元的句子啦。":
                font FONT_CN
                size 38
                color C_TEXT
                xalign 0.5

            text "一共收集了 " + str(total_stars) + " / " + str(_total_quiz_count()) + " 颗星星":
                font FONT_CN
                size 38
                bold True
                color C_GOLD
                xalign 0.5

            text "和朋友们说再见吧：Goodbye! See you next time!":
                font FONT_CN
                size 34
                color C_TEXT
                xalign 0.5

            hbox:
                spacing 30
                xalign 0.5

                textbutton "再玩一次":
                    style "kid_button"
                    text_style "kid_button_text"
                    action [Function(reset_progress), Return("again")]

                textbutton "回到标题":
                    style "kid_button"
                    text_style "kid_button_text"
                    action Return("title")
