# 小马宝莉英语闯关系列（PonyTalk）

> 一套给小学三年级小朋友设计的小马宝莉主题英语句子闯关小游戏。每个游戏是一个独立的小故事，用「对话 + 三选一句子卡」的方式，带孩子边玩边练**人教版（PEP）小学英语三年级上册**的重点句型。

*A collection of kid-friendly English sentence quiz games for 3rd graders, themed with My Little Pony and aligned with the PEP (People's Education Press) Grade-3 Semester-1 textbook.*

---

## 本仓库包含的游戏

| 游戏（故事名） | 版本 | 覆盖内容 | 下载 |
| --- | --- | --- | --- |
| **说对了才能继续** | v1.0 | Unit 1–6（6 章，早期小故事） | [Release v1.0](https://github.com/CynthiaYexingyi/Ponytalk/releases/tag/v1.0) |
| **小马宝莉 · 友谊英语课** | v6.0（最新修复版） | 四册 · 80 课时 · 320 题 · Unit 1–6 + Revision | [Release v6.0](https://github.com/CynthiaYexingyi/Ponytalk/releases/tag/v6.0) |

**v6.0 是最新修复版**，覆盖并取代了旧的 v3.0《友谊城堡的神秘来信》与 v5.0（这两版漏洞较多，已从 Releases 移除）；最早的 v1.0《说对了才能继续》仍保留供下载。

两个游戏玩法一致、剧情与题库各自独立，可分别下载试玩。

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

## 主要角色

- **Sunny（你）**：刚来到小马谷的小朋友，游戏的主角。
- **Twilight 紫悦**：博学的小马，负责开场和引导。
- **Pinkie 碧琪**：活泼好客，带你认识新朋友。
- **Applejack 苹果嘉儿**：农场主，带你认识家人。
- **Fluttershy 柔柔**：温柔善良，陪你在森林里认识动物。
- **Rainbow 云宝**：活泼的飞行小马，出现在彩虹章节。
- **Rarity 珍奇**：出现在派对章节。

## 下载与运行（直接玩）

可玩的安装包以 **GitHub Release** 形式发布，请到对应版本下载：

- **小马宝莉 · 友谊英语课** v6.0（最新修复版）：<https://github.com/CynthiaYexingyi/Ponytalk/releases/tag/v6.0>
- **说对了才能继续** v1.0（早期小故事）：<https://github.com/CynthiaYexingyi/Ponytalk/releases/tag/v1.0>

下载对应版本的 zip（v6.0 为 `PonyTalk-Windows.zip`），解压到任意文件夹，双击 `PonyTalk.exe` 即可在 Windows 上运行（无需安装）。

- **系统要求**：Windows 7 及以上；存档位于 `C:\Users\<用户名>\AppData\Roaming\RenPy\` 下。
- macOS / Linux 用户可通过 Ren'Py 运行（见下方「二次开发」）。

## 二次开发与改内容（老师 / 开发者）

本仓库按「故事」分目录，每个目录都是一个独立的 **Ren'Py 项目**（内含 `game/`）：

```
说对了才能继续/        # 早期小故事（v1.0）
英语学习网站/          # 2024 新版 PEP 三上 单文件学习网站（index.html）
```

**运行 / 试玩**

1. 安装 Ren'Py 官方 SDK（https://www.renpy.org/）。
2. 用 Ren'Py Launcher 打开 `说对了才能继续/` 目录（即包含 `game/` 的那一层）。
3. 点击 **Launch Project** 即可试玩。

**改剧情和题目**

绝大多数修改只需要改对应目录下 **`game/d_story.rpy`** 一个文件：

- `PONY`：角色的名字、颜色和立绘。
- `CHAPTERS`：各单元的故事；每个章节由若干 `beat` 组成：
  - `("narr", 中文旁白)`
  - `("say", 角色key, 英文台词, 中文译文)`
  - `("quiz", 题目字典)` —— 含情境 `scene`、问题 `ask`、三个选项 `options`、正确下标 `answer`、答对讲解 `explanation`、小贴士 `tip`。

界面样式在 `a_theme.rpy` / `b_ui.rpy`，游戏流程在 `c_engine.rpy`，一般无需改动；改内容请集中在 `d_story.rpy`。

**打包成安装包**

在 Ren'Py Launcher 中选择 **Build Distributions**，勾选 PC / Mac / Linux 等目标平台，即可生成可分发版本。

## 英语学习网站（新部分）

仓库中的 `英语学习网站/index.html` 是一个**单文件、零外部依赖**的英语学习网页，对应人教 PEP 2024 三年级上册。双击用浏览器打开即可使用，包含：

- **学一学**：按单元浏览核心句型与单词，配小马插画；
- **测一测 / 错题小测**：选择题练习，答错自动进错题本；
- **拼一拼 / 拖一拖 / 字母拼**：单词拼写与排列互动练习；
- 发音朗读（调用浏览器语音合成）、星星与进度记录（本地保存）。

所有图片已内嵌为 base64，无需联网、无需额外素材文件。

## 项目结构

```
Ponytalk/
├── 说对了才能继续/            # 故事一（v1.0，Unit 1–6，6 章）
│   └── game/                 #   Ren'Py 项目（剧本 / 题库 / 图片 / 音效 / 字体）
├── 英语学习网站/              # 2024 新版 PEP 三上 单文件学习网站（可直接在浏览器打开）
│   └── index.html
├── LICENSE                   # CC BY-NC-SA 4.0
├── README.md
└── .gitignore
```

每个 `game/` 内的主要文件：

```
game/
├── a_theme.rpy            # 主题与样式（粉紫马卡龙配色、对话框、按钮）
├── b_ui.rpy               # 界面（主菜单 / 玩法说明 / 选章 / HUD / 答题卡 / 结算 / 结局）
├── c_engine.rpy           # 游戏流程（章节循环、对话、答题、星星统计）
├── d_story.rpy            # ★ 故事与题库数据（改内容主要改这里）
├── options.rpy            # 游戏配置（名称、版本、存档目录等）
├── screens.rpy / gui.rpy  # Ren'Py 默认界面与 GUI 配置（已被上面自定义覆盖）
├── images/                # 背景(bg)、小马立绘(pony)、UI 元素(ui)
├── sfx/                   # 音效（correct / wrong / star / click / done 等 .wav）
├── gui/                   # 界面默认素材
└── SourceHanSansLite.ttf  # 思源黑体（中文显示）
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
