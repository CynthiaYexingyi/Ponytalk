################################################################################
##  界面：主菜单 / 玩法说明 / 选课程册 / 选课时 / HUD / 答题卡 / 结果页 / 结算 / 结局
##
##  v6.0（2026-11 重做）
##  ------------------------------------------------------------------
##  · HUD 重新分层：单元标签 / 课时标题 / 册名 各占一行，不再挤成一坨；
##    右上角独立显示「发光字母」和星星、得分。
##  · 答题拆成两步：pony_quiz（只负责选）+ pony_quiz_result（只负责反馈），
##    选句子与拼词都是这样。答完必定出现「答对啦 / 再想一想」，不会没反应。
##  · 每题顶部有倒计时条；答得快有速度加分，结果页会写明用了多久。
##  · 答对一题就播一次「字母亮起来」的小动画，并点亮 HUD 上的一个字母。
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
## 公用：发光字母格子（一个字一个格子，点亮的会发光）
################################################################################

##  注意（踩过的坑）：Ren'Py 的 xsize / ysize 如果给的是「浮点数」，会被当成
##  「占父容器宽度的百分比」，而不是像素！所以 96 * 0.52 = 49.92 这种写法会让
##  每个字母格子被撑成半个屏幕宽的巨块。这里一律先用 int() 兜成整数像素。
screen letter_tiles(word, lit, tile_zoom=0.62, gap=6):
    $ tw = int(96 * tile_zoom)
    $ th = int(112 * tile_zoom)
    $ fs = int(46 * tile_zoom)

    hbox:
        spacing gap

        for i, ch in enumerate(word):
            if i < lit:
                frame:
                    background Frame("images/ui/slot_lit.png", 22, 22)
                    xsize tw
                    ysize th
                    at lit_tile
                    text ch:
                        font FONT_CN
                        size fs
                        bold True
                        color "#7a5a1e"
                        xalign 0.5
                        yalign 0.5
            else:
                frame:
                    background Frame("images/ui/slot_dim.png", 22, 22)
                    xsize tw
                    ysize th
                    text ch:
                        font FONT_CN
                        size fs
                        bold True
                        color C_TEXT_SOFT
                        xalign 0.5
                        yalign 0.5


################################################################################
## 公用：倒计时条
################################################################################

screen timer_bar(kind, limit):
    $ left = time_left(kind)
    $ ratio = max(0.0, min(1.0, left / float(limit)))
    $ warn = ratio < 0.3

    frame:
        background Frame("images/ui/timer_bg.png", 14, 14)
        xsize 1000
        ysize 26
        padding (0, 0)

        add "images/ui/timer_fill.png":
            xsize int(1000 * ratio)
            ysize 26
            at clock_fill

    hbox:
        xpos 40
        ypos 140
        spacing 16

        text "剩 " + str(int(left)) + " 秒":
            font FONT_CN
            size 26
            bold True
            color (C_RED if warn else C_PURPLE)
            yalign 0.5

        if warn:
            text "快一点，光速答对有加分！":
                font FONT_CN
                size 22
                color C_TEXT_SOFT
                yalign 0.5

    timer 0.2 repeat True action Function(tick_timer, kind)


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

        text "小马宝莉　友谊英语课":
            font FONT_CN
            size 62
            bold True
            color "#ffe8f3"
            outlines [(5, "#b23a72", 0, 0)]

        text "人教 PEP 三年级上册　四册故事 · 80 课时 · 每课时都有新句子":
            font FONT_CN
            size 32
            color "#ffffffdd"

        text "选句子 + 魔法字母拼拼乐 + 倒计时 + 发光字母":
            font FONT_CN
            size 28
            color "#ffffffcc"

    vbox:
        xpos 140
        ypos 436
        spacing 12
        style_prefix "mm"

        textbutton "开始上课" action Start()
        textbutton "选择课时" action Start("lesson_hub")
        textbutton "玩法说明" action ShowMenu("how_to_play")
        textbutton "设置" action ShowMenu("preferences")
        textbutton "退出" action Quit(confirm=False)

    text "四册故事各 20 课时，按 Unit 1–6 + Revision 编排；每册知识点不重复，进度分开保存":
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
        xsize 1420
        padding (70, 46)

        vbox:
            spacing 22

            text "怎么玩？" font FONT_CN size 60 bold True color C_PINK_DEEP

            text "四册故事各 20 课时，按 Unit 1–6 的 Part A / B / C 递进，最后 2 节是综合复习。" font FONT_CN size 29 color C_PURPLE
            text "每一课都有一个小剧情，题目就藏在剧情里 —— 读懂故事，答案就在眼前。" font FONT_CN size 29 color C_PURPLE

            text "① 跟着小马读故事：英文台词下面有中文，看不懂也没关系。" font FONT_CN size 30 color C_TEXT
            text "② 选句子：读 3～4 个句子，选出最合适的那一句，鼠标点或按 1 / 2 / 3 / 4。" font FONT_CN size 32 color C_TEXT
            text "③ 魔法字母拼拼乐：句子空了一个单词，下面有一堆打乱的字母块（混着 1～2 个捣蛋字母）。" font FONT_CN size 32 color C_TEXT
            text "　 点字母放进空格，点空格可以退回；也可以直接用键盘打字。拼满后点「施放友谊魔法」。" font FONT_CN size 30 color C_TEXT
            text "④ 拼不出来就点「小提示」：会给首字母、帮你点亮字母，还会把捣蛋字母变走。" font FONT_CN size 32 color C_TEXT
            text "⑤ 每题都有倒计时。答得快，除了星星还能多拿速度分；答错不扣星，会告诉你错在哪。" font FONT_CN size 32 color C_TEXT
            text "⑥ 一次答对，就会点亮一个发光字母。整册的字母集齐，故事也会有大惊喜！" font FONT_CN size 32 color C_TEXT

            textbutton "我知道啦":
                action Return()
                style "kid_button"
                text_style "kid_button_text"
                xalign 0.5


################################################################################
## 选择课程册：四册故事并存，进度各自独立
################################################################################

screen pack_pick():
    modal True

    add "images/bg/title.png"
    add Solid("#2b1435aa")

    text "选择课程册":
        xalign 0.5
        ypos 18
        font FONT_CN
        size 56
        bold True
        color "#ffffff"
        outlines [(6, "#e0407f", 0, 0)]

    text "四册全新的小马宝莉故事 · 都按人教 PEP（2024 版）三年级上册 Unit 1–6 编排，知识点互不重复":
        xalign 0.5
        ypos 96
        font FONT_CN
        size 26
        color "#ffffffdd"

    vpgrid:
        cols 2
        xalign 0.5
        ypos 150
        spacing 28
        draggable False
        mousewheel False

        for p in STORY_PACKS:

            button:
                xsize 800
                ysize 382
                background Frame("images/ui/card_idle.png", 40, 40)
                hover_background Frame("images/ui/card_hover.png", 40, 40)
                padding (40, 22)
                action [Play("sound", "sfx/click.wav"), Return(p["id"])]

                vbox:
                    spacing 8
                    xsize 710

                    text p["title"]:
                        font FONT_CN size 38 bold True color C_PINK_DEEP

                    text p["subtitle"]:
                        font FONT_CN size 24 color C_TEXT

                    add Solid("#ffb6d4") xsize 700 ysize 3

                    text p["tagline"]:
                        font FONT_CN size 23 color C_PURPLE bold True

                    text p["pick_note"]:
                        font FONT_CN size 21 color C_TEXT_SOFT xsize 620

                    text "已完成 " + str(pack_done_count(p["id"])) + " / " + str(len(p["lessons"])) + " 课时　·　" + str(pack_total_stars(p["id"])) + " 颗星":
                        font FONT_CN size 24 color C_GOLD bold True

                    textbutton "进入这一册":
                        style "kid_button"
                        text_style "kid_button_text"
                        action [Play("sound", "sfx/click.wav"), Return(p["id"])]

                add ("images/pony/" + p["avatar"] + ".png"):
                    xalign 1.0
                    yalign 1.0
                    xoffset 10
                    yoffset 8
                    zoom 0.18

    textbutton "返回标题":
        style "kid_button"
        text_style "kid_button_text"
        xalign 0.5
        yalign 0.965
        action Return("back")

    key "game_menu" action Return("back")


################################################################################
## 选择课时：当前册 20 节课（6 单元 × 3 + 2 复习）
################################################################################

screen lesson_pick():
    modal True

    add "images/bg/title.png"
    add Solid("#2b1435aa")

    $ pack = cur_pack()

    text "选择课时":
        xalign 0.5
        ypos 12
        font FONT_CN
        size 56
        bold True
        color "#ffffff"
        outlines [(6, "#e0407f", 0, 0)]

    text pack["title"] + "　·　" + pack["tagline"]:
        xalign 0.5
        ypos 82
        font FONT_CN
        size 27
        color "#ffffffdd"

    text "已完成 " + str(pack_done_count()) + " / " + str(len(pack["lessons"])) + " 课时　·　" + str(pack_total_stars()) + " / " + str(pack["qcount"]) + " 颗星":
        xalign 0.5
        ypos 124
        font FONT_CN
        size 25
        color "#ffe9a8"

    textbutton "切换课程册":
        style "spell_button"
        text_style "spell_button_text"
        xalign 0.985
        ypos 26
        action [Play("sound", "sfx/click.wav"), Return("switch")]

    vpgrid:
        cols 5
        xalign 0.5
        ypos 168
        spacing 12
        draggable False
        mousewheel False

        for L in pack["lessons"]:

            button:
                xsize 340
                ysize 170
                background Frame("images/ui/card_idle.png", 40, 40)
                hover_background Frame("images/ui/card_hover.png", 40, 40)
                padding (20, 12)
                action [Play("sound", "sfx/click.wav"), Return(L["num"])]

                vbox:
                    spacing 2
                    xsize 236

                    text "第 " + str(L["num"]) + " 课时":
                        font FONT_CN size 22 bold True color C_PINK_DEEP

                    text L["unit"]:
                        font FONT_CN size 17 color C_TEXT_SOFT

                    text L["title"]:
                        font FONT_CN size 27 bold True color C_TEXT

                    text L["goal"]:
                        font FONT_CN size 16 color C_TEXT_SOFT xsize 230

                    if lesson_done(L["num"]):
                        text "✓ 已上过":
                            font FONT_CN size 17 color C_GREEN bold True
                    else:
                        text "尚未开始":
                            font FONT_CN size 17 color C_TEXT_SOFT

                    use star_row(n=lesson_stars(L["num"]), total=L["qcount"], star_size=0.5)

                add ("images/pony/" + L["avatar"] + ".png"):
                    xalign 1.0
                    yalign 1.0
                    xoffset 6
                    yoffset 6
                    zoom 0.12

    textbutton "返回标题":
        style "kid_button"
        text_style "kid_button_text"
        xalign 0.5
        yalign 0.965
        action Return("back")

    key "game_menu" action Return("back")


################################################################################
## HUD：左上角是「我在上哪一课」，右上角是「点亮了什么、得了多少分」
##      —— 两块分开，不再把单元 / 标题 / 册名挤在一起
################################################################################

screen hud(pack, ch, star_now, star_total, score_now, word, q_index):
    zorder 40

    ## ---------- 左上：课时身份（分层显示） ----------
    frame:
        background Frame("images/ui/ribbon.png", 40, 40)
        xpos 40
        ypos 20
        xsize 1000
        padding (36, 12, 30, 12)

        vbox:
            spacing 4

            hbox:
                spacing 16

                ## 单元做成一个小胶囊，和标题区分开
                frame:
                    background Frame("images/ui/btn_idle.png", 24, 16)
                    padding (18, 4)
                    yalign 0.5
                    text ch["unit"]:
                        font FONT_CN size 22 bold True color C_PURPLE

                text ch["title"]:
                    font FONT_CN
                    size 36
                    bold True
                    color C_TEXT
                    yalign 0.5

            text pack["title"]:
                font FONT_CN
                size 21
                color C_TEXT_SOFT

    ## ---------- 右上：发光字母 + 星星 + 得分 ----------
    ##  宽度按内容收紧（4 个字母格 + 星星/得分列 ≈ 340px），不要撑成一大片空白
    frame:
        background Frame("images/ui/panel.png", 44, 44)
        xpos 1440
        ypos 20
        xsize 440
        padding (26, 10, 26, 10)

        hbox:
            spacing 22

            vbox:
                spacing 2
                yalign 0.5

                text "发光字母":
                    font FONT_CN size 19 color C_TEXT_SOFT

                use letter_tiles(word=word, lit=star_now, tile_zoom=0.62, gap=5)

            vbox:
                spacing 2
                yalign 0.5

                hbox:
                    spacing 8
                    add "images/ui/star_full.png" zoom 0.55 yalign 0.5
                    text str(star_now) + "/" + str(star_total):
                        font FONT_CN size 30 color C_TEXT bold True yalign 0.5

                hbox:
                    spacing 8
                    text "得分":
                        font FONT_CN size 21 color C_TEXT_SOFT yalign 0.5
                    text str(score_now):
                        font FONT_CN size 30 color C_GOLD bold True yalign 0.5


################################################################################
## 选句子题：只负责「选」，反馈交给结果页
################################################################################

init python:

    def _card_bg(idx, chosen, answer):
        if chosen is not None and idx == chosen:
            if idx == answer:
                return "images/ui/card_correct.png"
            return "images/ui/card_wrong.png"
        if chosen is not None and idx == answer:
            return "images/ui/card_correct.png"
        return "images/ui/card_idle.png"


screen pony_quiz(ch, q):
    modal True
    zorder 55

    add Solid("#2b143566")

    ## ---------- 倒计时 ----------
    use timer_bar("quiz", TIME_QUIZ)

    ## ---------- 情境 + 问题 ----------
    frame:
        background Frame("images/ui/panel.png", 44, 44)
        xpos 40
        ypos 196
        xsize 1180
        padding (46, 22)

        vbox:
            spacing 12

            text "情 境":
                font FONT_CN
                size 20
                color C_TEXT_SOFT

            text q["scene"]:
                font FONT_CN
                size 33
                color C_TEXT

            add Solid("#ffb6d4") xsize 1080 ysize 3

            text q["ask"]:
                font FONT_CN
                size 40
                color C_PINK_DEEP
                bold True

    ## ---------- 句子卡 ----------
    vbox:
        xpos 40
        ypos 452
        spacing 16

        for i, opt in enumerate(q["options"]):

            button:
                xsize 1180
                ysize 132
                background Frame("images/ui/card_idle.png", 40, 40)
                hover_background Frame("images/ui/card_hover.png", 40, 40)
                padding (44, 14)
                action [Play("sound", "sfx/click.wav"), Return(("pick", i))]

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

    ## ---------- 数字键 1 / 2 / 3 / 4 ----------
    key "1" action [Play("sound", "sfx/click.wav"), Return(("pick", 0))]
    key "2" action [Play("sound", "sfx/click.wav"), Return(("pick", 1))]
    key "3" action [Play("sound", "sfx/click.wav"), Return(("pick", 2))]
    if len(q["options"]) > 3:
        key "4" action [Play("sound", "sfx/click.wav"), Return(("pick", 3))]

    ## ---------- 超时提示 ----------
    if time_left("quiz") <= 0:
        frame:
            background Frame("images/ui/panel_pink.png", 44, 44)
            xalign 0.5
            yalign 0.5
            xsize 720
            padding (50, 40)
            at panel_pop

            vbox:
                spacing 18
                xalign 0.5

                text "时间到啦！":
                    font FONT_CN size 52 bold True color C_PINK_DEEP xalign 0.5

                text "没关系，我们一起看看正确答案～":
                    font FONT_CN size 28 color C_TEXT xalign 0.5

                textbutton "看看答案":
                    style "kid_button"
                    text_style "kid_button_text"
                    xalign 0.5
                    action Return(("timeout",))


################################################################################
## 选句子题 · 结果页：答完一定会来到这里
################################################################################

screen pony_quiz_result(q, ok, timeout, picked, used, limit, score):
    modal True
    zorder 60

    add Solid("#2b1435aa")

    $ right = q["options"][q["answer"]]

    frame:
        background Frame("images/ui/panel.png", 44, 44)
        xalign 0.5
        yalign 0.5
        xsize 1320
        padding (56, 38)
        at panel_pop

        vbox:
            spacing 16
            xsize 1200

            ## ---- 大标题 ----
            hbox:
                spacing 20
                yalign 0.5

                if ok:
                    add "images/ui/check.png" zoom 0.9 yalign 0.5
                    text "答对啦！":
                        font FONT_CN size 58 bold True color C_GREEN yalign 0.5
                elif timeout:
                    add "images/ui/cross.png" zoom 0.9 yalign 0.5
                    text "时间到啦～":
                        font FONT_CN size 58 bold True color C_PINK_DEEP yalign 0.5
                else:
                    add "images/ui/cross.png" zoom 0.9 yalign 0.5
                    text "再想一想～":
                        font FONT_CN size 58 bold True color C_RED yalign 0.5

                if ok:
                    text "用时 " + ("%.1f" % used) + " 秒　·　得分 " + str(score):
                        font FONT_CN size 28 color C_GOLD bold True yalign 0.5
                else:
                    text "用时 " + ("%.1f" % used) + " 秒":
                        font FONT_CN size 28 color C_TEXT_SOFT yalign 0.5

            add Solid("#ffb6d4") xsize 1200 ysize 3

            if ok:
                ## ---- 答对：把正确的句子讲清楚 ----
                text right["en"]:
                    font FONT_CN size 46 bold True color C_TEXT

                text right["zh"]:
                    font FONT_CN size 32 color C_TEXT_SOFT

                text q["explain"]:
                    font FONT_CN size 30 color C_TEXT

                if q.get("tip"):
                    text "小贴士：" + q["tip"]:
                        font FONT_CN size 28 color C_PURPLE

                text "一次答对，点亮一个字母，还得到 " + str(score) + " 分！":
                    font FONT_CN size 28 color C_GREEN bold True

                textbutton "继续":
                    style "kid_button"
                    text_style "kid_button_text"
                    xalign 1.0
                    action [Play("sound", "sfx/star.wav"), Return()]

            else:
                ## ---- 答错 / 超时：告诉小朋友错在哪 ----
                if timeout:
                    text "正确答案是这一句：":
                        font FONT_CN size 34 color C_TEXT
                else:
                    $ picked_opt = q["options"][picked]
                    text "你选的是：" + picked_opt["en"] + "（" + picked_opt["zh"] + "）":
                        font FONT_CN size 34 color C_TEXT

                    if picked_opt.get("note"):
                        text picked_opt["note"]:
                            font FONT_CN size 30 color C_RED

                text "应该选：" + right["en"] + "（" + right["zh"] + "）":
                    font FONT_CN size 36 bold True color C_GREEN

                text q["explain"]:
                    font FONT_CN size 30 color C_TEXT

                if q.get("tip"):
                    text "小贴士：" + q["tip"]:
                        font FONT_CN size 28 color C_PURPLE

                if timeout:
                    textbutton "知道啦，继续":
                        style "kid_button"
                        text_style "kid_button_text"
                        xalign 1.0
                        action [Play("sound", "sfx/click.wav"), Return()]
                else:
                    textbutton "再试一次":
                        style "kid_button"
                        text_style "kid_button_text"
                        xalign 1.0
                        action [Play("sound", "sfx/click.wav"), Return()]


################################################################################
## 填单词卡：只负责「拼」，反馈交给结果页
################################################################################

screen pony_fill(ch, q, spell):
    modal True
    zorder 55

    add Solid("#2b143566")

    $ ans = spell["answer"]
    $ parts = q["sentence"].split("___")
    $ nslots = len(ans)
    $ sent_size = 38 if nslots >= 7 else 44
    $ filled = spell_filled()
    $ hint = spell["hint"]
    $ letter_count = len([c for c in ans if c.isalpha()])
    $ next_empty = next((j for j in range(nslots) if j not in spell["fixed"] and spell["slots"][j] is None), -1)

    ## ---------- 倒计时 ----------
    use timer_bar("fill", TIME_FILL)

    ## ---------- 情境 ----------
    frame:
        background Frame("images/ui/panel.png", 44, 44)
        xpos 40
        ypos 196
        xsize 1180
        padding (40, 18)

        vbox:
            spacing 8

            text q["scene"]:
                font FONT_CN size 30 color C_TEXT

            text "魔法字母拼拼乐 · 把散落的字母按正确顺序放回这一句":
                font FONT_CN size 24 color C_PINK_DEEP bold True

    ## ---------- 句子 + 空格槽 ----------
    frame:
        background Frame("images/ui/panel.png", 44, 44)
        xpos 40
        ypos 356
        xsize 1180
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

    ## ---------- 字母池 + 操作按钮 ----------
    frame:
        background Frame("images/ui/panel.png", 44, 44)
        xpos 40
        ypos 560
        xsize 1180
        padding (36, 18)

        vbox:
            spacing 14

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
                    action [Play("sound", "sfx/click.wav"), Return(("submit", spell_guess()))]

            if filled:
                text "字母都归位啦！点「施放友谊魔法」，看看这一页会不会发光～" font FONT_CN size 27 color C_GREEN bold True
            else:
                text "点字母块放进空格；点已经放好的空格，可以把字母退回来。也可以直接用键盘打字。" font FONT_CN size 25 color C_TEXT_SOFT

    ## ---------- 键盘也能玩 ----------
    for _ch in "abcdefghijklmnopqrstuvwxyz":
        key _ch action Function(spell_type, _ch)
    key "K_BACKSPACE" action Function(spell_pop)
    key "K_RETURN" action [Play("sound", "sfx/click.wav"), Return(("submit", spell_guess()))]

    ## ---------- 超时提示 ----------
    if time_left("fill") <= 0:
        frame:
            background Frame("images/ui/panel_pink.png", 44, 44)
            xalign 0.5
            yalign 0.5
            xsize 720
            padding (50, 40)
            at panel_pop

            vbox:
                spacing 18
                xalign 0.5

                text "时间到啦！":
                    font FONT_CN size 52 bold True color C_PINK_DEEP xalign 0.5

                text "没关系，我们一起看看正确的单词～":
                    font FONT_CN size 28 color C_TEXT xalign 0.5

                textbutton "看看答案":
                    style "kid_button"
                    text_style "kid_button_text"
                    xalign 0.5
                    action Return(("timeout",))


################################################################################
## 填单词卡 · 结果页
################################################################################

screen pony_fill_result(q, ok, timeout, guess, prefix, used, limit, score):
    modal True
    zorder 60

    add Solid("#2b1435aa")

    $ ans = q["answer"]
    $ letter_count = len([c for c in ans if c.isalpha()])

    frame:
        background Frame("images/ui/panel.png", 44, 44)
        xalign 0.5
        yalign 0.5
        xsize 1320
        padding (56, 38)
        at panel_pop

        vbox:
            spacing 16
            xsize 1200

            hbox:
                spacing 20
                yalign 0.5

                if ok:
                    add "images/ui/check.png" zoom 0.9 yalign 0.5
                    text "魔法单词拼好啦！":
                        font FONT_CN size 54 bold True color C_GREEN yalign 0.5
                elif timeout:
                    add "images/ui/cross.png" zoom 0.9 yalign 0.5
                    text "时间到啦～":
                        font FONT_CN size 54 bold True color C_PINK_DEEP yalign 0.5
                else:
                    add "images/ui/cross.png" zoom 0.9 yalign 0.5
                    text "再想一想～":
                        font FONT_CN size 54 bold True color C_RED yalign 0.5

                if ok:
                    text "用时 " + ("%.1f" % used) + " 秒　·　得分 " + str(score):
                        font FONT_CN size 28 color C_GOLD bold True yalign 0.5
                else:
                    text "用时 " + ("%.1f" % used) + " 秒":
                        font FONT_CN size 28 color C_TEXT_SOFT yalign 0.5

            add Solid("#ffb6d4") xsize 1200 ysize 3

            if ok:
                hbox:
                    spacing 12
                    for _s in range(3):
                        add "images/ui/star_full.png" zoom 0.42

                text "正确答案：" + ans + "（" + q["word_zh"] + "）":
                    font FONT_CN size 42 bold True color C_TEXT

                text "跟我读一遍：" + " · ".join(list(ans.upper())):
                    font FONT_CN size 30 color C_PURPLE

                text q["explain"]:
                    font FONT_CN size 30 color C_TEXT

                if q.get("tip"):
                    text "小贴士：" + q["tip"]:
                        font FONT_CN size 28 color C_PURPLE

                text "纸上的字母亮了一下，故事又要往前走啦。":
                    font FONT_CN size 27 color C_TEXT_SOFT

                textbutton "继续":
                    style "kid_button"
                    text_style "kid_button_text"
                    xalign 1.0
                    action [Play("sound", "sfx/star.wav"), Return()]

            else:
                if timeout:
                    text "正确的单词是：":
                        font FONT_CN size 32 color C_TEXT
                else:
                    text "你拼的是：" + (guess if guess else "（空）"):
                        font FONT_CN size 32 color C_TEXT

                    if prefix > 0:
                        text "前 " + str(prefix) + " 个字母已经排对啦！从第 " + str(prefix + 1) + " 个开始再试试～":
                            font FONT_CN size 30 color C_GREEN bold True
                    else:
                        text "顺序有点不一样，字母们跳回池子啦，别着急～":
                            font FONT_CN size 30 color C_RED

                text "应该拼的是：" + ans + "（" + q["word_zh"] + "）":
                    font FONT_CN size 40 bold True color C_GREEN

                text "这个词一共有 " + str(letter_count) + " 个字母，首字母是 " + ans[0].upper() + "。":
                    font FONT_CN size 29 color C_TEXT

                text q["explain"]:
                    font FONT_CN size 29 color C_TEXT

                if q.get("tip"):
                    text "小贴士：" + q["tip"]:
                        font FONT_CN size 27 color C_PURPLE

                textbutton "再试一次":
                    style "kid_button"
                    text_style "kid_button_text"
                    xalign 1.0
                    action [Play("sound", "sfx/click.wav"), Return()]


################################################################################
## 发光字母：答对一题就播一次
################################################################################

screen letter_glow(ch, letter, index, total):
    modal True
    zorder 70

    add Solid("#2b143577")

    add "images/ui/glow.png":
        xalign 0.5
        yalign 0.46
        zoom 1.15
        at glow_pulse

    text letter:
        xalign 0.5
        yalign 0.46
        yoffset -14
        font FONT_CN
        size 230
        bold True
        color "#fff8e0"
        outlines [(8, "#e8a409", 0, 0)]
        at letter_pop

    add "images/ui/sparkle.png":
        xalign 0.36
        yalign 0.34
        zoom 0.55
        at sparkle_pop

    add "images/ui/sparkle.png":
        xalign 0.64
        yalign 0.58
        zoom 0.42
        at sparkle_pop2

    add "images/ui/sparkle.png":
        xalign 0.56
        yalign 0.28
        zoom 0.30
        at sparkle_pop

    text "第 " + str(index + 1) + " 个字母亮起来啦！":
        xalign 0.5
        ypos 720
        font FONT_CN
        size 46
        bold True
        color "#ffffff"
        outlines [(5, "#e0407f", 0, 0)]

    text ch.get("loot", ""):
        xalign 0.5
        ypos 782
        font FONT_CN
        size 26
        color "#ffe8f3"

    timer 1.7 action Return()
    key "K_RETURN" action Return()
    key "K_SPACE" action Return()


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

screen friendship_report(pack, ch, title, body):
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

            text pack["report_head"]:
                font FONT_CN size 30 color C_PURPLE bold True

            text title:
                font FONT_CN size 48 bold True color C_PINK_DEEP

            add Solid("#ffb6d4") xsize 1200 ysize 3

            text body:
                font FONT_CN size 32 color C_TEXT xsize 1200 line_spacing 10

            hbox:
                spacing 16
                add "images/ui/star_full.png" zoom 0.5 yalign 0.5
                text pack["report_foot"]:
                    font FONT_CN size 27 color C_GOLD bold True yalign 0.5

            textbutton "收好这一页":
                style "kid_button"
                text_style "kid_button_text"
                xalign 1.0
                action [Play("sound", "sfx/done.wav"), Return()]


################################################################################
## 课时结算：得分、每题用时明细、点亮后的单词
################################################################################

screen lesson_done(pack, ch, stars, score, results, word):
    modal True
    zorder 60

    add Solid("#2b143599")

    frame:
        background Frame("images/ui/panel.png", 44, 44)
        xalign 0.5
        yalign 0.5
        xsize 1200
        padding (56, 36)
        at panel_pop

        vbox:
            spacing 16
            xalign 0.5

            text "第 " + str(ch["num"]) + " 课时 完成！":
                font FONT_CN
                size 60
                bold True
                color C_PINK_DEEP
                xalign 0.5

            text ch["title"]:
                font FONT_CN
                size 32
                color C_TEXT
                xalign 0.5

            use star_row(n=stars, total=ch["qcount"], star_size=1.25)

            ## ---- 点亮的单词 ----
            frame:
                background Frame("images/ui/panel_pink.png", 44, 44)
                xalign 0.5
                xsize 900
                padding (20, 12)

                vbox:
                    spacing 4
                    xalign 0.5

                    text "本课的字母拼成了：":
                        font FONT_CN size 22 color C_TEXT_SOFT xalign 0.5

                    use letter_tiles(word=word, lit=stars, tile_zoom=0.78, gap=8)

            ## ---- 得分 ----
            hbox:
                spacing 30
                xalign 0.5

                text "总得分":
                    font FONT_CN size 28 color C_TEXT_SOFT yalign 0.5

                text str(score):
                    font FONT_CN size 44 bold True color C_GOLD yalign 0.5

                text "一次答对 " + str(stars) + " / " + str(ch["qcount"]) + " 题":
                    font FONT_CN size 28 color C_TEXT yalign 0.5

            ## ---- 每题明细 ----
            frame:
                background Frame("images/ui/panel.png", 44, 44)
                xalign 0.5
                xsize 1000
                padding (26, 16)

                vbox:
                    spacing 8

                    for r in results:
                        hbox:
                            spacing 18
                            xalign 0.5

                            text ("第 " + str(r["no"]) + " 题"):
                                font FONT_CN size 24 color C_TEXT xsize 110

                            if r["right"]:
                                add "images/ui/check.png" zoom 0.36 yalign 0.5
                                text "答对":
                                    font FONT_CN size 24 color C_GREEN bold True xsize 90 yalign 0.5
                            elif r["timeout"]:
                                add "images/ui/cross.png" zoom 0.36 yalign 0.5
                                text "超时":
                                    font FONT_CN size 24 color C_PINK_DEEP bold True xsize 90 yalign 0.5
                            else:
                                add "images/ui/cross.png" zoom 0.36 yalign 0.5
                                text "再想想":
                                    font FONT_CN size 24 color C_RED bold True xsize 90 yalign 0.5

                            text ("用时 " + ("%.1f" % r["used"]) + " 秒"):
                                font FONT_CN size 24 color C_TEXT_SOFT xsize 170 yalign 0.5

                            text ("得分 " + str(r["score"])):
                                font FONT_CN size 24 color C_GOLD bold True yalign 0.5

            if stars == ch["qcount"]:
                text "全部一次答对！你是友谊小使者！":
                    font FONT_CN
                    size 32
                    bold True
                    color C_GOLD
                    xalign 0.5
            elif stars >= 2:
                text "很棒！再读一遍故事，下次一定更快。":
                    font FONT_CN
                    size 30
                    color C_TEXT
                    xalign 0.5
            else:
                text "没关系，我们把这几句再读一遍，就会记住啦。":
                    font FONT_CN
                    size 30
                    color C_TEXT
                    xalign 0.5

            text "这一册已上完 " + str(pack_done_count()) + " / " + str(len(pack["lessons"])) + " 课时":
                font FONT_CN
                size 24
                color C_TEXT_SOFT
                xalign 0.5

            textbutton "继续":
                style "kid_button"
                text_style "kid_button_text"
                xalign 0.5
                action [Play("sound", "sfx/done.wav"), Return()]


################################################################################
## 本册结局
################################################################################

screen the_end(pack, total_stars):
    modal True

    add "images/bg/friends.png"
    add Solid("#1d0f2aaa")

    frame:
        background Frame("images/ui/panel.png", 44, 44)
        xalign 0.5
        yalign 0.5
        xsize 1320
        padding (60, 40)
        at panel_pop

        vbox:
            spacing 16
            xalign 0.5

            text pack["title"] + "　全册通关！":
                font FONT_CN
                size 60
                bold True
                color C_PINK_DEEP
                xalign 0.5

            text pack["ending"]["title"]:
                font FONT_CN
                size 40
                bold True
                color C_PURPLE
                xalign 0.5

            for line in pack["ending"]["lines"]:
                text line:
                    font FONT_CN
                    size 28
                    color C_TEXT
                    xsize 1180
                    xalign 0.5

            text pack["end_line"]:
                font FONT_CN
                size 30
                color C_TEXT
                xalign 0.5

            text "这一册收集了 " + str(total_stars) + " 颗星星":
                font FONT_CN
                size 36
                bold True
                color C_GOLD
                xalign 0.5

            text pack["ending"]["cheer"]:
                font FONT_CN
                size 30
                color C_GREEN
                xalign 0.5

            hbox:
                spacing 26
                xalign 0.5

                textbutton "再玩这一册":
                    style "kid_button"
                    text_style "kid_button_text"
                    action Return("again")

                textbutton "换一册故事":
                    style "kid_button"
                    text_style "kid_button_text"
                    action Return("switch")

                textbutton "回到标题":
                    style "kid_button"
                    text_style "kid_button_text"
                    action Return("title")
