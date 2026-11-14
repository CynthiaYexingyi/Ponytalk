################################################################################
##  主题与样式：马卡龙粉紫 · 儿童友好排版
##  只负责“外观”，不改游戏逻辑。
################################################################################

init offset = 2

define C_PINK      = "#ff5fa2"
define C_PINK_DEEP = "#e0407f"
define C_PINK_SOFT = "#ffd8e9"
define C_PURPLE    = "#6b4fa0"
define C_TEXT      = "#4a3a5a"
define C_TEXT_SOFT = "#8b7f96"
define C_GREEN     = "#1f9d5b"
define C_RED       = "#d93b57"
define C_GOLD      = "#e8a409"

define FONT_CN = "SourceHanSansLite.ttf"


################################################################################
## 主菜单背景（覆盖 gui.rpy 的默认值）
################################################################################

init python:
    gui.main_menu_background = "images/bg/title.png"
    gui.game_menu_background = "images/bg/ending.png"
    gui.title_text_size = 96
    gui.accent_color = "#e0407f"
    gui.hover_color = "#e0407f"


################################################################################
## 对话框
################################################################################

style pony_window is window

style pony_window:
    xalign 0.5
    yalign 1.0
    xsize 1800
    ysize 300
    background Frame("images/ui/panel.png", 44, 44)
    padding (66, 28, 66, 24)

style pony_name is default

style pony_name:
    font FONT_CN
    size 44
    color C_PINK_DEEP
    bold True
    xalign 0.0
    line_spacing 2

style pony_text is default

style pony_text:
    font FONT_CN
    size 42
    color C_TEXT
    xalign 0.0
    line_spacing 8


screen say(who, what):
    window:
        id "window"
        style "pony_window"

        vbox:
            spacing 10
            xfill True

            if who is not None:
                text who id "who" style "pony_name"

            text what id "what" style "pony_text"


################################################################################
## 快捷菜单：只留存档 / 读档 / 设置
################################################################################

screen quick_menu():
    zorder 100

    if quick_menu:
        hbox:
            xalign 1.0
            yalign 1.0
            xoffset -16
            yoffset -8
            spacing 10

            textbutton "存档" action ShowMenu("save") style "quick_button"
            textbutton "读档" action ShowMenu("load") style "quick_button"
            textbutton "设置" action ShowMenu("preferences") style "quick_button"

style quick_button:
    background None
    padding (12, 4)

style quick_button_text:
    font FONT_CN
    size 26
    color "#ffffffcc"
    hover_color "#ffffff"


################################################################################
## 按钮样式
################################################################################

style mm_button:
    background Frame("images/ui/btn_idle.png", 48, 30)
    hover_background Frame("images/ui/btn_hover.png", 48, 30)
    xsize 460
    ysize 92
    padding (30, 8)

style mm_button_text:
    font FONT_CN
    size 40
    color C_TEXT
    hover_color "#ffffff"
    bold True
    xalign 0.5
    yalign 0.5

style kid_button:
    background Frame("images/ui/btn_idle.png", 48, 30)
    hover_background Frame("images/ui/btn_hover.png", 48, 30)
    padding (44, 10)
    xminimum 300
    ysize 90

style kid_button_text:
    font FONT_CN
    size 34
    color C_TEXT
    hover_color "#ffffff"
    bold True
    xalign 0.5
    yalign 0.5


################################################################################
## 立绘位置 / 动画
################################################################################

transform pony_right:
    zoom 0.80
    xanchor 0.5
    xpos 1480
    yalign 1.0
    yoffset 40

transform pony_right_quiz:
    zoom 0.58
    xanchor 0.5
    xpos 1620
    yalign 1.0
    yoffset 30

transform card_pop:
    on show:
        alpha 0.0
        yoffset 20
        easein 0.20 alpha 1.0 yoffset 0
    on hide:
        easeout 0.12 alpha 0.0

transform panel_pop:
    on show:
        alpha 0.0
        zoom 0.97
        easein 0.18 alpha 1.0 zoom 1.0
