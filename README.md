# 小马宝莉 · 说对了才能继续（PonyTalk）

> 一个给小学三年级小朋友设计的英语句子闯关小游戏。以《小马宝莉》为主题，用「对话 + 三选一句子卡」的方式，带孩子边玩边练**人教版（PEP）小学英语三年级上册 Unit 1–6** 的重点句型。内容与课本单元同步，循序渐进。

*A kid-friendly English sentence quiz game for 3rd graders, themed with My Little Pony and aligned with the PEP (People's Education Press) Grade-3 Semester-1 textbook, Units 1–6.*

当前版本：**v1.0**，覆盖三年级上册 Unit 1–6。

---

## 游戏简介

你是刚来到小马谷的小朋友 **Sunny**。六只小马会轮流用英语和你对话，每句英文下面都配有中文翻译，看不懂也没关系。

- 轮到你回答时，会弹出 **3 张句子卡**，读一读，选出最合适的一句，故事才能继续往下讲。
- 选错了不要紧，小马会告诉你这几句话「哪里不一样」，再试一次就好。
- 一次就答对，得 **1 颗星**；每章集满星星，就能看到结局。

游戏鼓励孩子「大胆开口、不怕选错」，把课本里的句子放到真实的小情境里反复体会。

## 怎么玩

1. 听小马们说话：英文句子下面有中文，理解大意即可。
2. 轮到你时，出现 3 张句子卡，选出最合适的那一句。
3. 选对就继续；选错会有讲解，再试一次。
4. 一次答对得 1 颗星，每题最多 1 颗。

**操作方式**：用鼠标点击句子卡作答；也可以直接按键盘 **1 / 2 / 3** 选择对应的句子卡。

## 六个章节

| 章节 | 课本单元 | 标题 | 场景 | 学习目标（重点句型） |
| --- | --- | --- | --- | --- |
| 1 | Unit 1 Making friends | 新朋友 | 草地 | Hello / I'm … / My name is … / Nice to meet you |
| 2 | Unit 2 Different families | 苹果嘉儿的家 | 农场 | This is my … / Is this your …? / I have a big family |
| 3 | Unit 3 Amazing animals | 森林里的小动物 | 森林 | What's this / that? / It's a … / Do you have a pet? |
| 4 | Unit 4 Plants around us | 小马谷的花园 | 花园 | Do you like …? / I like … / We can … / Plants need … |
| 5 | Unit 5 The colourful world | 雨后的彩虹 | 彩虹 | What colour is it? / It's … / Red and blue make … |
| 6 | Unit 6 Useful numbers | 碧琪的生日派对 | 派对 | How old are you? / How many …? / It's seven o'clock. |

## 主要角色

- **Sunny（你）**：刚来到小马谷的小朋友，游戏的主角。
- **Twilight 紫悦**：博学的小马，负责开场和引导。
- **Pinkie 碧琪**：活泼好客，带你认识新朋友（Unit 1）。
- **Applejack 苹果嘉儿**：农场主，带你认识家人（Unit 2）。
- **Fluttershy 柔柔**：温柔善良，陪你在森林里认识动物（Unit 3）。
- **Rainbow 云宝**：活泼的飞行小马，出现在彩虹章节（Unit 5）。
- **Rarity 珍奇**：出现在派对章节（Unit 6）。

## 下载与运行（直接玩）

可玩的安装包以 **GitHub Release** 形式发布，请到 Releases 页面下载：

**下载地址：https://github.com/CynthiaYexingyi/Ponytalk/releases/latest**

1. 下载 `PonyTalk-pc.zip`。
2. 解压到任意文件夹。
3. 双击 `PonyTalk.exe` 即可在 Windows 上运行。

- **系统要求**：Windows 7 及以上；无需安装，解压即玩。
- 存档位置：Windows 下位于 `C:\Users\<用户名>\AppData\Roaming\RenPy\Mylittlepony-1793319893`。
- macOS / Linux 用户可通过 Ren'Py 运行（见下方「二次开发」）。

## 二次开发与改内容（老师 / 开发者）

本仓库只保存**游戏源码与素材**（`game/` 目录），不包含 Ren'Py 运行环境；可玩的安装包请见 Releases。

**运行 / 试玩**

1. 安装 Ren'Py 官方 SDK（https://www.renpy.org/）。
2. 用 Ren'Py Launcher 打开本仓库目录（或直接把 `game/` 放到一个 Ren'Py 项目里）。
3. 点击 **Launch Project** 即可试玩。

**改剧情和题目**

绝大多数修改只需要改 **`game/d_story.rpy`** 一个文件：

- `PONY`：角色的名字、颜色和立绘。
- `CHAPTERS`：六个单元的故事；每个章节由若干 `beat` 组成：
  - `("narr", 中文旁白)`
  - `("say", 角色key, 英文台词, 中文译文)`
  - `("quiz", 题目字典)` —— 含情境 `scene`、问题 `ask`、三个选项 `options`、正确下标 `answer`、答对讲解 `explanation`、小贴士 `tip`。

界面样式在 `a_theme.rpy` / `b_ui.rpy`，游戏流程在 `c_engine.rpy`，一般无需改动；改内容请集中在 `d_story.rpy`。

**打包成安装包**

在 Ren'Py Launcher 中选择 **Build Distributions**，勾选 PC / Mac / Linux 等目标平台，即可生成可分发版本。

## 项目结构

```
Ponytalk/
├── game/                      # 游戏内容（剧本、题库、图片、音效、字体）
│   ├── a_theme.rpy            # 主题与样式（粉紫马卡龙配色、对话框、按钮）
│   ├── b_ui.rpy               # 界面（主菜单 / 玩法说明 / 选章 / HUD / 答题卡 / 结算 / 结局）
│   ├── c_engine.rpy           # 游戏流程（章节循环、对话、答题、星星统计）
│   ├── d_story.rpy            # ★ 故事与题库数据（改内容主要改这里）
│   ├── options.rpy            # 游戏配置（名称、版本、存档目录等）
│   ├── screens.rpy / gui.rpy  # Ren'Py 默认界面与 GUI 配置（已被上面自定义覆盖）
│   ├── images/                # 背景(bg)、小马立绘(pony)、UI 元素(ui)
│   ├── sfx/                   # 音效（correct / wrong / star / click / done 等 .wav）
│   ├── gui/                   # 界面默认素材
│   └── SourceHanSansLite.ttf  # 思源黑体（中文显示）
├── LICENSE                    # CC BY-NC-SA 4.0
├── README.md
└── .gitignore
```

> 说明：`.rpyc` / `.rpyb` 等编译产物与本地存档已被 `.gitignore` 忽略，Ren'Py 启动时会自动重新生成，无需纳入版本管理。

## 许可证

本作品采用 **Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International（CC BY-NC-SA 4.0）** 许可，详见 `LICENSE` 文件。

- **署名（BY）**：使用或分发时请保留作者署名与许可声明。
- **非商业（NC）**：不得用于商业用途。
- **相同方式共享（SA）**：在他人基础上改编后，须以相同或兼容的许可发布。

《小马宝莉》（My Little Pony）角色版权归 **Hasbro** 所有。本项目为**教学用途的同人 / 二创作品**，非官方出品，并声明**非商业使用**。

## 致谢

- 游戏基于 **Ren'Py** 视觉小说引擎构建（Ren'Py 采用 MIT 许可）。
- 中文显示使用 **思源黑体（Source Han Sans / Noto Sans CJK）**。
- 角色与故事创意来自《小马宝莉》，用于小学英语情境教学。
