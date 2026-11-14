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

        text "小马宝莉　友谊城堡的神秘来信":
            font FONT_CN
            size 58
            bold True
            color "#ffe8f3"
            outlines [(5, "#b23a72", 0, 0)]

        text "三年级上册　选句子 + 魔法字母拼拼乐":
            font FONT_CN
            size 34
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

    text "点一点就能玩：选句子用鼠标或 1 / 2 / 3 / 4，拼单词点字母块，也可以直接打字":
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

            text "① 跟着小马读故事：英文台词下面有中文，看不懂也没关系。" font FONT_CN size 32 color C_TEXT
            text "② 选句子：读 3～4 个句子，选出最合适的那一句，鼠标点或按 1 / 2 / 3 / 4。" font FONT_CN size 32 color C_TEXT
            text "③ 魔法字母拼拼乐：句子空了一个单词，下面有一堆打乱的字母块（混着 1～2 个捣蛋字母）。" font FONT_CN size 32 color C_TEXT
            text "　 点字母放进空格，点空格可以退回；也可以直接用键盘打字。拼满后点「施放友谊魔法」。" font FONT_CN size 30 color C_TEXT
            text "④ 拼不出来就点「小提示」：会给首字母、帮你点亮字母，还会把捣蛋字母变走。" font FONT_CN size 32 color C_TEXT
            text "⑤ 答错不扣分，会告诉你前面几个字母已经排对啦。一次答对得 1 颗星。" font FONT_CN size 32 color C_TEXT

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
        ypos 24
        font FONT_CN
        size 66
        bold True
        color "#ffffff"
        outlines [(6, "#e0407f", 0, 0)]

    text "七个故事 · 一封没有署名的信 · 六封写给宇宙公主的友谊报告":
        xalign 0.5
        ypos 108
        font FONT_CN
        size 28
        color "#ffffffdd"

    vpgrid:
        cols 4
        xalign 0.5
        ypos 158
        spacing 16
        draggable False
        mousewheel False

        for ch in CHAPTERS:

            button:
                xsize 396
                ysize 248
                background Frame("images/ui/card_idle.png", 40, 40)
                hover_background Frame("images/ui/card_hover.png", 40, 40)
                padding (26, 18)
                action Return(ch["num"])

                vbox:
                    spacing 4
                    xfill True

                    text ch["unit"]:
                        font FONT_CN
                        size 22
                        color C_PINK_DEEP
                        bold True

                    text ch["title"]:
                        font FONT_CN
                        size 34
                        color C_TEXT
                        bold True

                    text ch["goal"]:
                        font FONT_CN
                        size 19
                        color C_TEXT_SOFT
                        xmaximum 210

                    use star_row(n=persistent.chapter_stars.get(str(ch["num"]), 0), total=ch["qcount"], star_size=0.66)

                add ("images/pony/" + ch["avatar"] + ".png"):
                    xalign 1.0
                    yalign 1.0
                    xoffset 4
                    yoffset 6
                    zoom 0.15

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
        if len(options) > 3:
            key "4" action [Play("sound", "sfx/correct.wav" if answer == 3 else "sfx/wrong.wav"), SetScreenVariable("chosen", 3)]

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
                    ysize (138 if len(options) >= 4 else 156)
                    background Frame(_card_bg(i, chosen, answer), 40, 40)
                    hover_background Frame("images/ui/card_hover.png", 40, 40)
                    padding (44, 18)
                    action [Play("sound", "sfx/correct.wav" if i == answer else "sfx/wrong.wav"), SetScreenVariable("chosen", i)]

                    hbox:
                        spacing 26
                        yalign 0.5

                        text "ABCD"[i]:
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
## 填单词卡
################################################################################
## 魔法字母拼拼乐（填词题）
##  散落的字母块 + 1~2 个捣蛋字母 → 点进句子的空格槽 → 拼对让信发光
################################################################################

screen pony_fill(ch, q, spell, feedback):
    modal True
    zorder 55

    add Solid("#2b143555")

    $ ans = spell["answer"]
    $ parts = q["sentence"].split("___")
    $ nslots = len(ans)
    $ sent_size = 38 if nslots >= 7 else 44
    $ filled = spell_filled()
    $ hint = spell["hint"]
    $ letter_count = len([c for c in ans if c.isalpha()])
    $ next_empty = next((j for j in range(nslots) if j not in spell["fixed"] and spell["slots"][j] is None), -1)

    ## 情境条
    frame:
        background Frame("images/ui/panel.png", 44, 44)
        xpos 40
        ypos 32
        xsize 1220
        padding (40, 14)

        vbox:
            spacing 6
            text q["scene"] font FONT_CN size 30 color C_TEXT
            text "魔法字母拼拼乐 · 把散落的字母按正确顺序放回信上" font FONT_CN size 24 color C_PINK_DEEP bold True

    if feedback is None:

        ## 句子 + 空格槽
        frame:
            background Frame("images/ui/panel.png", 44, 44)
            xpos 40
            ypos 146
            xsize 1220
            padding (38, 16)
            at panel_pop

            vbox:
                spacing 12

                hbox:
                    spacing 8
                    yalign 0.5

                    text parts[0] font FONT_CN size sent_size bold True color C_TEXT yalign 0.5

                    for i in range(nslots):

                        if i in spell["fixed"]:
                            button:
                                style "slot_button"
                                background Frame("images/ui/slot_fixed.png", 22, 22)
                                action NullAction()
                                text spell["fixed"][i] style "slot_fixed_text"

                        else:
                            $ tid = spell["slots"][i]
                            if tid is not None:
                                button:
                                    style "slot_button"
                                    background Frame("images/ui/slot_filled.png", 22, 22)
                                    hover_background Frame("images/ui/slot_empty.png", 22, 22)
                                    action [Play("sound", "sfx/click.wav"), Function(spell_remove, i)]
                                    text spell["tiles"][tid]["ch"].upper() style "slot_text"
                            elif i == next_empty:
                                button:
                                    style "slot_button"
                                    background Frame("images/ui/slot_next.png", 22, 22)
                                    action NullAction()
                                    text "" style "slot_text"
                            else:
                                button:
                                    style "slot_button"
                                    background Frame("images/ui/slot_empty.png", 22, 22)
                                    action NullAction()
                                    text "" style "slot_text"

                    if len(parts) > 1:
                        text parts[1] font FONT_CN size sent_size bold True color C_TEXT yalign 0.5

                hbox:
                    spacing 26

                    text "中文：" + q["word_zh"] font FONT_CN size 28 color C_PINK_DEEP bold True

                    if hint == 0:
                        text "点「小提示」，会有魔法帮手来帮忙" font FONT_CN size 26 color C_TEXT_SOFT
                    elif hint == 1:
                        text "首字母：" + ans[0].upper() + "，一共 " + str(letter_count) + " 个字母" font FONT_CN size 26 color C_PURPLE
                    else:
                        text "首字母：" + ans[0].upper() + "，一共 " + str(letter_count) + " 个字母　·　帮手已经来过 " + str(hint) + " 次啦" font FONT_CN size 26 color C_PURPLE

        ## 字母池 + 操作按钮
        frame:
            background Frame("images/ui/panel.png", 44, 44)
            xpos 40
            ypos 352
            xsize 1220
            padding (36, 18)

            vbox:
                spacing 16

                text "散落的魔法字母（里面有捣蛋字母混进来了哦）" font FONT_CN size 26 color C_TEXT bold True

                hbox:
                    spacing 10
                    ysize 100

                    for tid in spell["pool_order"]:
                        $ t = spell["tiles"][tid]
                        if t["used"] or tid in spell["hidden"]:
                            null width 96
                        else:
                            button:
                                style "tile_button"
                                action [Play("sound", "sfx/click.wav"), Function(spell_place, tid)]
                                text t["ch"].upper() style "tile_text"

                hbox:
                    spacing 14

                    textbutton "重排字母":
                        style "spell_button"
                        text_style "spell_button_text"
                        action [Play("sound", "sfx/click.wav"), Function(spell_shuffle)]

                    textbutton "全部退回":
                        style "spell_button"
                        text_style "spell_button_text"
                        action [Play("sound", "sfx/click.wav"), Function(spell_clear)]

                    textbutton "小提示":
                        style "spell_button"
                        text_style "spell_button_text"
                        action [Play("sound", "sfx/click.wav"), Function(spell_hint)]

                    textbutton "施放友谊魔法":
                        style "spell_go_button"
                        text_style "spell_go_button_text"
                        sensitive filled
                        action [Play("sound", "sfx/click.wav"), Function(spell_submit)]

                if filled:
                    text "字母都归位啦！点「施放友谊魔法」，看看信会不会发光～" font FONT_CN size 27 color C_GREEN bold True
                else:
                    text "点字母块放进空格；点已经放好的空格，可以把字母退回来。也可以直接用键盘打字。" font FONT_CN size 25 color C_TEXT_SOFT

        ## 键盘也能玩
        for _ch in "abcdefghijklmnopqrstuvwxyz":
            key _ch action Function(spell_type, _ch)
        key "K_BACKSPACE" action Function(spell_pop)
        key "K_RETURN" action [Play("sound", "sfx/click.wav"), Function(spell_submit)]

    ## 反馈
    else:

        $ is_right = feedback[0] == "right"

        frame:
            background Frame("images/ui/panel.png", 44, 44)
            xpos 40
            ypos 340
            xsize 1220
            ysize 660
            padding (48, 28)
            at panel_pop

            vbox:
                spacing 16

                if is_right:
                    hbox:
                        spacing 18
                        at star_twinkle
                        add "images/ui/check.png" zoom 0.82 yalign 0.5
                        text "魔法单词拼好啦！":
                            font FONT_CN size 50 bold True color C_GREEN yalign 0.5
                else:
                    hbox:
                        spacing 18
                        at spell_shake
                        add "images/ui/cross.png" zoom 0.82 yalign 0.5
                        text "再想一想～":
                            font FONT_CN size 50 bold True color C_RED yalign 0.5

                if is_right:

                    hbox:
                        spacing 12
                        at star_twinkle
                        for _s in range(3):
                            add "images/ui/star_full.png" zoom 0.42

                    text "正确答案：" + ans + "（" + q["word_zh"] + "）":
                        font FONT_CN size 38 bold True color C_TEXT

                    text "跟我读一遍：" + " · ".join(list(ans.upper())):
                        font FONT_CN size 30 color C_PURPLE

                    text q["explain"]:
                        font FONT_CN size 29 color C_TEXT

                    if q.get("tip"):
                        text "小贴士：" + q["tip"]:
                            font FONT_CN size 27 color C_PURPLE

                    text "信上的字母亮了一下，故事又要往前走啦。":
                        font FONT_CN size 26 color C_TEXT_SOFT

                    textbutton "继续":
                        style "kid_button"
                        text_style "kid_button_text"
                        xalign 1.0
                        action [Play("sound", "sfx/star.wav"), Return(("done",))]

                else:

                    text "你拼的是：" + (feedback[1] if feedback[1] else "（空）"):
                        font FONT_CN size 32 color C_TEXT

                    if feedback[2] > 0:
                        text "前 " + str(feedback[2]) + " 个字母已经排对啦！从第 " + str(feedback[2] + 1) + " 个开始再试试～":
                            font FONT_CN size 30 color C_GREEN bold True
                    else:
                        text "顺序有点不一样，字母们跳回池子啦，别着急～":
                            font FONT_CN size 30 color C_RED

                    text "再想想：这个空要填「" + q["word_zh"] + "」，首字母是 " + ans[0].upper() + "，一共 " + str(letter_count) + " 个字母。":
                        font FONT_CN size 29 color C_TEXT

                    if q.get("note"):
                        text q["note"]:
                            font FONT_CN size 27 color C_TEXT_SOFT

                    text "小提示可以帮你点亮字母、把捣蛋字母变走哦。":
                        font FONT_CN size 26 color C_PURPLE

                    textbutton "再试一次":
                        style "kid_button"
                        text_style "kid_button_text"
                        xalign 1.0
                        action [Play("sound", "sfx/click.wav"), Return(("retry",))]

        if is_right:
            key "K_RETURN" action [Play("sound", "sfx/star.wav"), Return(("done",))]
        else:
            key "K_RETURN" action [Play("sound", "sfx/click.wav"), Return(("retry",))]


################################################################################
## 轻互动选择：选一句，小马回一句；不计分
################################################################################

screen pony_choice(question, options):
    modal True
    zorder 56

    add Solid("#2b143577")

    frame:
        background Frame("images/ui/panel.png", 44, 44)
        xalign 0.5
        yalign 0.5
        xsize 1120
        padding (56, 38)
        at panel_pop

        vbox:
            spacing 22

            text "你来选一选" font FONT_CN size 28 color C_PURPLE bold True

            text question font FONT_CN size 40 bold True color C_TEXT

            for i, opt in enumerate(options):
                $ label = opt[0]
                textbutton label:
                    style "kid_button"
                    text_style "kid_button_text"
                    xsize 980
                    action [Play("sound", "sfx/click.wav"), Return(i)]

            text "（选哪一句都可以，故事都会继续～）" font FONT_CN size 24 color C_TEXT_SOFT


################################################################################
## 章末：给宇宙公主的友谊报告
################################################################################

screen friendship_report(ch, title, body):
    modal True
    zorder 58

    add Solid("#2b1435aa")

    frame:
        background Frame("images/ui/panel_pink.png", 44, 44)
        xalign 0.5
        yalign 0.5
        xsize 1340
        padding (66, 46)
        at panel_pop

        vbox:
            spacing 20
            xsize 1200

            text "给宇宙公主的友谊报告 · Friendship Report":
                font FONT_CN size 30 color C_PURPLE bold True

            text title:
                font FONT_CN size 48 bold True color C_PINK_DEEP

            add Solid("#ffb6d4") xsize 1200 ysize 3

            text body:
                font FONT_CN size 32 color C_TEXT xsize 1200 line_spacing 10

            hbox:
                spacing 16
                add "images/ui/star_full.png" zoom 0.5 yalign 0.5
                text "第 " + str(ch["num"]) + " 封 · 信上又亮了一个词":
                    font FONT_CN size 27 color C_GOLD bold True yalign 0.5

            textbutton "收好这封信":
                style "kid_button"
                text_style "kid_button_text"
                xalign 1.0
                action [Play("sound", "sfx/done.wav"), Return()]


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

            if ch.get("loot"):
                text "写好了：" + ch["loot"]:
                    font FONT_CN
                    size 30
                    color C_GOLD
                    xalign 0.5

            use star_row(n=stars, total=ch["qcount"], star_size=1.3)

            if stars == ch["qcount"]:
                text "全部一次答对！你是友谊小使者！":
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

            text "六封友谊报告写完，那封没有署名的信终于补好啦！":
                font FONT_CN
                size 40
                color C_TEXT
                xalign 0.5

            text "一共收集了 " + str(total_stars) + " / " + str(_total_quiz_count()) + " 颗星星":
                font FONT_CN
                size 38
                bold True
                color C_GOLD
                xalign 0.5

            text "宇宙公主说：明年彩虹节见！Goodbye! See you next time!":
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



