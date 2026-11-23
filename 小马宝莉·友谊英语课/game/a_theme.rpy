################################################################################
##  主题与样式：马卡龙粉紫 · 儿童友好排版
##  只负责“外观”，不改游戏逻辑。
##
##  v6.0：字体换成 PonySansLite.ttf —— 原来的 SourceHanSansLite.ttf 缺
##  U+00B7 (·) 等符号，游戏里会显示成豆腐块 ⊠。新字体由 tools/fix_font.py
##  生成（把缺字从 DejaVuSans 嫁接进来）。
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

define FONT_CN = "PonySansLite.ttf"


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

## 小星星是飘在空中的，位置比小马高一些
transform pony_star:
    zoom 0.80
    xanchor 0.5
    xpos 1560
    ypos 250

transform pony_star_quiz:
    zoom 0.62
    xanchor 0.5
    xpos 1680
    ypos 430

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


## 字母键盘按钮
style key_button:
    background Frame("images/ui/key.png", 28, 20)
    hover_background Frame("images/ui/key_hover.png", 28, 20)
    xsize 84
    ysize 56
    padding (0, 0)

style key_button_text:
    font FONT_CN
    size 30
    bold True
    color C_TEXT
    hover_color "#ffffff"
    xalign 0.5
    yalign 0.5


################################################################################
## 魔法字母拼拼乐：空格槽 / 字母块 / 操作按钮
################################################################################

style slot_button:
    xsize 88
    ysize 100
    padding (0, 0)

style slot_text:
    font FONT_CN
    size 46
    bold True
    color C_PINK_DEEP
    xalign 0.5
    yalign 0.5

style slot_fixed_text:
    font FONT_CN
    size 46
    bold True
    color C_GOLD
    xalign 0.5
    yalign 0.5

style tile_button:
    background Frame("images/ui/tile.png", 22, 22)
    hover_background Frame("images/ui/tile_hover.png", 22, 22)
    xsize 96
    ysize 100
    padding (0, 0)

style tile_text:
    font FONT_CN
    size 48
    bold True
    color "#7a5a1e"
    hover_color "#3a2a10"
    xalign 0.5
    yalign 0.5

style spell_button:
    background Frame("images/ui/btn_idle.png", 48, 30)
    hover_background Frame("images/ui/btn_hover.png", 48, 30)
    padding (30, 8)
    xminimum 240
    ysize 84

style spell_button_text:
    font FONT_CN
    size 31
    bold True
    color C_TEXT
    hover_color "#ffffff"
    xalign 0.5
    yalign 0.5

style spell_go_button:
    background Frame("images/ui/btn_hover.png", 48, 30)
    hover_background Frame("images/ui/key_hover.png", 28, 20)
    padding (34, 8)
    xminimum 320
    ysize 84

style spell_go_button_text:
    font FONT_CN
    size 32
    bold True
    color "#ffffff"
    insensitive_color "#f3e2ef"
    xalign 0.5
    yalign 0.5


## 拼对：星光弹入；拼错：轻轻晃一晃
transform star_twinkle:
    on show:
        alpha 0.0
        yoffset 26
        easein 0.24 alpha 1.0 yoffset 0
    on hide:
        easeout 0.12 alpha 0.0

transform spell_shake:
    on show:
        alpha 0.0
        easein 0.10 alpha 1.0
        xoffset 0
        linear 0.06 xoffset -14
        linear 0.06 xoffset 12
        linear 0.06 xoffset -8
        linear 0.06 xoffset 6
        linear 0.06 xoffset 0
    on hide:
        easeout 0.12 alpha 0.0


################################################################################
##  v6.0 新增：发光字母 / 倒计时
################################################################################

## 字母亮起来时背后的柔光：一涨一落
transform glow_pulse:
    alpha 0.0
    zoom 0.85
    easein 0.35 alpha 0.95 zoom 1.15
    linear 0.55 alpha 0.75 zoom 1.05
    easeout 0.4 alpha 0.0 zoom 1.25

## 大字母登场：从小弹到正常大小
transform letter_pop:
    alpha 0.0
    zoom 0.3
    rotate -12
    easeout 0.45 alpha 1.0 zoom 1.0 rotate 0

## 两颗小星星：交替闪
transform sparkle_pop:
    alpha 0.0
    zoom 0.2
    linear 0.25 alpha 1.0 zoom 0.9
    linear 0.5 alpha 0.7 zoom 0.7
    easeout 0.3 alpha 0.0 zoom 0.4

transform sparkle_pop2:
    alpha 0.0
    zoom 0.2
    linear 0.35 alpha 1.0 zoom 0.85
    linear 0.55 alpha 0.6 zoom 0.65
    easeout 0.3 alpha 0.0 zoom 0.35

## HUD 上已经点亮的字母格子：轻轻呼吸
transform lit_tile:
    alpha 0.0
    easein 0.18 alpha 1.0
    linear 1.2 alpha 0.88
    linear 1.2 alpha 1.0
    repeat

## 倒计时条：随剩余时间收缩
transform clock_fill:
    easein 0.25 xzoom 1.0 yzoom 1.0


