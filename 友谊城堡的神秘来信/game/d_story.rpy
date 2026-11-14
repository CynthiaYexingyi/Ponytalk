################################################################################
##  《小马宝莉 · 友谊城堡的神秘来信》故事与题库
##  教材：2024 新版 人教 PEP 三年级上册（Unit 1 - Unit 6 + Revision）
##  版本：3.0  全新剧情 · 魔法字母拼拼乐
##
##  ★ 故事设定（My Little Pony: Friendship is Magic 世界观）
##    紫悦公主住在小马谷的友谊城堡，每周都要给宇宙公主寄一封「友谊报告」，
##    由小龙穗龙用龙火吐气送走。今天早上，报告不见了，桌上只剩一封
##    被烧得坑坑洼洼、字母全乱了、还没有署名的信……
##    友谊地图亮起六个光点，指向小马谷的六个地方。每帮一匹小马解决一个
##    「友谊小麻烦」，信上就会浮现一个正确的单词。
##    → 填空环节 = 帮穗龙把信上散落的魔法字母拼回原样。
##
##  ★ 老师改内容只需要改这个文件：
##    PONY      角色名字、颜色、立绘
##    CHAPTERS  七个故事章节（beats = 按顺序播放的节拍）
##
##  beat 种类：
##    ("narr", 中文旁白)
##    ("say", 角色key, 英文台词, 中文译文)
##    ("scene", 背景名)   title / meadow / farm / forest / garden / rainbow / party / ending / friends
##    ("choice", 问题, [(选项文字, 回应旁白), ...])     轻互动，不计分
##    ("report", 报告标题, 报告正文)                    章末「给宇宙公主的友谊报告」信纸
##    ("quiz", 题目字典)                                选句子
##    ("fill", 题目字典)                                拼单词（魔法字母拼拼乐）
##
##  quiz 字段：who / scene / ask / options（3~4 个，含 en, zh, note）
##             answer 正确下标 / explain / tip
##             可选 after = ("narr", 文本) 或 ("say", 角色, 英文, 中文)，答对后推进剧情
##  fill 字段：who / scene / sentence（含 ___）/ answer / word_zh
##             explain / note / tip
##             可选 after / cheer（自定义欢呼旁白）
##
##  ★ 所有文本请只用中文标点「」『』，不要出现英文双引号、方括号、花括号。
################################################################################

init python:

    PONY = {
        "twilight":   {"name": "Twilight 紫悦",      "color": "#7b4fb8", "img": "images/pony/twilight.png"},
        "pinkie":     {"name": "Pinkie 碧琪",        "color": "#e8448f", "img": "images/pony/pinkie.png"},
        "applejack":  {"name": "Applejack 苹果嘉儿",  "color": "#d97b1e", "img": "images/pony/applejack.png"},
        "rainbow":    {"name": "Rainbow 云宝",       "color": "#2d8fd5", "img": "images/pony/rainbow.png"},
        "rarity":     {"name": "Rarity 珍奇",        "color": "#5b4bc4", "img": "images/pony/rarity.png"},
        "fluttershy": {"name": "Fluttershy 柔柔",    "color": "#d4548f", "img": "images/pony/fluttershy.png"},
        "star":       {"name": "友谊之光",           "color": "#e8a409", "img": "images/pony/star.png"},
    }

    CHARS = {}
    for _k, _v in PONY.items():
        CHARS[_k] = Character(_v["name"], color=_v["color"], who_color=_v["color"])


    CHAPTERS = [

        ########################################################################
        ## 第 1 章  Unit 1 Making friends
        ## 地点：方糖角落 Sugarcube Corner ｜ 主角：碧琪、柔柔
        ## 麻烦：欢迎派对还没开始，名牌全撒了，碧琪连怎么打招呼都忘了
        ########################################################################
        {
            "num": 1,
            "unit": "Unit 1  Making friends",
            "title": "方糖角落的欢迎派对",
            "goal": "Hello / I'm … / My name is … / Nice to meet you",
            "bg": "party",
            "loot": "第 1 封友谊报告《A New Friend》",
            "beats": [
                ("scene", "party"),
                ("narr", "彩虹节前一周，小马谷的方糖角落甜品店飘着奶油香。"),
                ("narr", "紫悦公主说，今天要在这里，为刚来小马谷的小马同学 Clover 办一场欢迎派对。"),
                ("narr", "可店门刚推开，彩带、纸杯蛋糕和一叠名牌哗啦一下全撒在了地板上。"),
                ("say", "pinkie", "Oopsie! I jumped too high!", "哎呀！我跳得太高啦！"),
                ("say", "pinkie", "My party plan is all over the floor!", "我的派对计划全撒到地上了！"),
                ("narr", "碧琪从蛋糕堆里探出头，鬃毛上还挂着一颗樱桃，急得原地转了三圈。"),
                ("say", "pinkie", "And I forgot how to say hello…", "而且我连怎么打招呼都忘了……"),
                ("narr", "紫悦从桌边抬起头。她手里还捏着早上那封奇怪的信：纸边焦焦的，字母乱成一团，末尾空空的，没有署名。"),
                ("say", "twilight", "Spike sent my report this morning. But THIS is not my report.", "穗龙今早替我寄了报告。可这封，不是我写的那封。"),
                ("narr", "旁边的小龙穗龙把一封信藏到背后，尾巴尖悄悄冒了一缕烟，假装在看天花板。"),
                ("say", "twilight", "A party always starts with a hello. Let's fix the names first.", "派对总是从一句「你好」开始。我们先把名字补回来吧。"),
                ("say", "twilight", "Clover, this is your first friendship task.", "Clover，这是你的第一个友谊任务。"),

                ("quiz", {
                    "who": "pinkie",
                    "scene": "碧琪举着一块空白名牌，眨眨眼问：「Hello! What's your name?」",
                    "ask": "哪一句是在回答自己的名字？",
                    "options": [
                        {"en": "My name is Clover.", "zh": "我叫 Clover。", "note": ""},
                        {"en": "I'm nine.", "zh": "我九岁。", "note": "「I'm nine.」说的是年龄；别人问名字，要答名字。"},
                        {"en": "I'm fine, thank you.", "zh": "我很好，谢谢。", "note": "这是回答「How are you?」（你好吗）的，不是回答名字。"},
                    ],
                    "answer": 0,
                    "explain": "介绍名字用「My name is …」或「I'm …」。问名字就答名字，别把年龄和名字弄混。",
                    "tip": "I'm + 名字 = 我叫…；I'm + 数字 = 我…岁。",
                    "after": ("say", "pinkie", "My name is Pinkie Pie! See? I remembered!", "我叫碧琪！看！我想起来啦！"),
                }),

                ("narr", "碧琪把名牌一张张捡起来，最上面那张只写着「My ___ is Clover.」，中间空了一格，字母散了一地。"),
                ("say", "pinkie", "Oh no, the letters ran away again!", "不好，字母又跑掉啦！"),

                ("fill", {
                    "who": "pinkie",
                    "scene": "把散落的魔法字母按正确顺序放回句子里，名牌就会重新亮起来。",
                    "sentence": "My ___ is Clover.",
                    "answer": "name",
                    "word_zh": "名字",
                    "explain": "「My name is Clover.」= 我叫 Clover。name 是「名字」，4 个字母。",
                    "note": "「名字」的英文是 n 开头、4 个字母；My 后面要接一个表示「名字」的词。",
                    "tip": "My name is + 名字。／ What's your name? 是问名字。",
                    "after": ("narr", "名牌上的字母一个接一个跳回原位。远处，紫悦口袋里那封神秘信轻轻抖了一下，纸面浮出一个淡淡的字母 H。"),
                }),

                ("narr", "「叮铃」——门上的铃铛响了。柔柔抱着一小束野花，站在门口，小声得几乎听不见。"),
                ("say", "fluttershy", "H-hello… I'm Fluttershy.", "你、你好……我是柔柔。"),
                ("say", "pinkie", "Come in! This is my good friend, Fluttershy.", "快进来！这是我的好朋友，柔柔。"),
                ("narr", "柔柔躲到碧琪身后，只露出一只眼睛。碧琪挠挠头：她好像还不知道，第一次见面之后该说什么。"),

                ("quiz", {
                    "who": "fluttershy",
                    "scene": "柔柔轻轻对你说：「Nice to meet you.」你也想礼貌地回应她。",
                    "ask": "哪一句是最合适的回应？",
                    "options": [
                        {"en": "Nice to meet you, too.", "zh": "我也很高兴认识你。", "note": ""},
                        {"en": "Goodbye! See you!", "zh": "再见！回头见！", "note": "「Goodbye」是分别时说的，刚见面不能说再见。"},
                        {"en": "I'm nine years old.", "zh": "我九岁。", "note": "这是在说年龄，回应见面问候要答「我也很高兴」。"},
                    ],
                    "answer": 0,
                    "explain": "对方先说「Nice to meet you.」，我们回答「Nice to meet you, too.」——句尾加一个 too，表示「我也一样」。",
                    "tip": "too 放在句尾，意思是「也」。",
                }),

                ("narr", "柔柔听见这句，慢慢从碧琪身后走出来，把野花递给你。"),
                ("say", "fluttershy", "Thank you… You are kind.", "谢谢你……你真好。"),
                ("narr", "可碧琪又举起一张名牌，愁眉苦脸：这张上面写着「This is my good ___.」，字母又乱了。"),

                ("fill", {
                    "who": "pinkie",
                    "scene": "碧琪想请你记住：柔柔是她的「好朋友」。把乱掉的字母拼回去吧。",
                    "sentence": "This is my good ___.",
                    "answer": "friend",
                    "word_zh": "朋友",
                    "explain": "「This is my good friend.」= 这是我的好朋友。good 后面接名词 friend（朋友），6 个字母。",
                    "note": "「朋友」的英文是 f 开头、6 个字母的词。",
                    "tip": "good friend = 好朋友；This is my + 人物（用来介绍别人）。",
                }),

                ("choice", "碧琪把最后三张名牌摊在你面前：「先补哪一张呀？」", [
                    ("写「Nice to meet you」的那张", "碧琪拍手：「对！第一次见面，这句话最管用！」"),
                    ("写「Wave your hand」的那张", "碧琪笑得直蹦：「也好！挥挥手，大家就都认识啦！」"),
                    ("偷偷先吃一个纸杯蛋糕", "碧琪瞪大眼睛：「这个主意很 Pinkie！不过……我们还是先把名牌补完吧！」"),
                ]),

                ("narr", "派对终于要开始了。碧琪站到椅子上，宣布第一项：所有人一起挥手问好。"),
                ("say", "pinkie", "Everybody, wave your hand!", "大家，一起挥挥手！"),
                ("narr", "可是她手里那张指令牌上，「hand」这个词的字母又散开了。"),

                ("fill", {
                    "who": "pinkie",
                    "scene": "碧琪举起手挥一挥，让你把口令补完整。",
                    "sentence": "Wave your ___!",
                    "answer": "hand",
                    "word_zh": "手",
                    "explain": "「Wave your hand!」= 挥挥手！hand 是「手」，4 个字母。",
                    "note": "「手」的英文是 h 开头、4 个字母；身体部位的单词要记牢哦。",
                    "tip": "wave 是「挥动」，wave your hand = 挥挥手。",
                    "after": ("narr", "满屋子的马蹄一起挥起来。神秘信上的字母亮了第二个：E。"),
                }),

                ("narr", "派对进行到一半，紫悦看了看窗外的天色：还得赶去下一个光点。"),
                ("say", "twilight", "We have to go. But what do we say?", "我们得走了。可是该说什么呢？"),

                ("quiz", {
                    "who": "twilight",
                    "scene": "要离开方糖角落了，你想对碧琪和柔柔说一句合适的告别。",
                    "ask": "哪一句是合适的告别？",
                    "options": [
                        {"en": "Goodbye! See you!", "zh": "再见！回头见！", "note": ""},
                        {"en": "Hello! I'm Clover.", "zh": "你好！我是 Clover。", "note": "「Hello」是见面打招呼的话，分别时要说 Goodbye。"},
                        {"en": "Nice to meet you, too.", "zh": "我也很高兴认识你。", "note": "这是回应见面问候的话，不是告别。"},
                    ],
                    "answer": 0,
                    "explain": "见面用 Hello / Hi，离开用 Goodbye / See you。两句话意思相反，别用错。",
                    "tip": "See you! = 回头见！",
                }),

                ("say", "pinkie", "Goodbye, Clover! Come back for cake!", "再见，Clover！要回来吃蛋糕哦！"),
                ("narr", "临走前，柔柔小声叫住你。她手里捏着一张被风吹乱的小卡片，上面只剩半句话。"),

                ("fill", {
                    "who": "fluttershy",
                    "scene": "柔柔想完整地说一遍「我也很高兴认识你」，请你把最后一个词拼好。",
                    "sentence": "Nice to meet you, ___!",
                    "answer": "too",
                    "word_zh": "也",
                    "explain": "「Nice to meet you, too!」= 我也很高兴认识你！too 是「也」，3 个字母，放在句尾。",
                    "note": "别人先说，我们回答时要在句尾加一个表示「也」的词，t 开头、3 个字母。",
                    "tip": "too 放句尾 = 也。／ Nice to meet you. → Nice to meet you, too.",
                    "after": ("say", "fluttershy", "Nice to meet you, too!", "我也很高兴认识你！"),
                }),

                ("narr", "六张名牌整整齐齐排好，派对的灯亮了。碧琪端出那个歪歪扭扭、但特别香的欢迎蛋糕。"),
                ("say", "pinkie", "Best party ever! And I said hello ALL by myself!", "最棒的派对！而且「你好」是我自己说出来的！"),
                ("narr", "紫悦展开那封神秘信：原本乱糟糟的纸面上，已经能认出两个字母了——H、E。"),
                ("say", "twilight", "It is writing itself… one word at a time.", "它在自己写字……一次一个单词。"),
                ("report", "第 1 封友谊报告 · A New Friend",
                 "亲爱的宇宙公主：今天我们在方糖角落学会了一件小事——友谊是从一句「Hello」开始的。"
                 "碧琪把名牌弄乱了，可是只要有人愿意先说「My name is …」，再回一句「Nice to meet you, too.」，"
                 "陌生的两匹小马就变成了朋友。信上浮出了两个字母：H、E。"),
                ("narr", "友谊地图上的第一个光点安静下来，第二个光点亮起，指向城外的甜苹果园。"),
                ("narr", "穗龙悄悄跟在队伍最后，把今天拼对的单词，一个一个记在了小本子上。"),
            ],
        },

        ########################################################################
        ## 第 2 章  Unit 2 Different families
        ## 地点：甜苹果园 Sweet Apple Acres ｜ 主角：苹果嘉儿、史密斯婆婆
        ## 麻烦：家庭聚会上的旧全家福被苹果汁弄湿，谁是谁认不出来了
        ########################################################################
        {
            "num": 2,
            "unit": "Unit 2  Different families",
            "title": "甜苹果园的全家福",
            "goal": "This is my … / Is this your …? / I have a big family",
            "bg": "farm",
            "loot": "第 2 封友谊报告《My Big Family》",
            "beats": [
                ("scene", "farm"),
                ("narr", "甜苹果园今天热闹极了：苹果嘉儿一家在办一年一度的家族聚会，长桌上摆了二十七个苹果派。"),
                ("narr", "友谊地图的第二个光点，正落在谷仓门口那张旧相框上。"),
                ("say", "applejack", "Welcome to Sweet Apple Acres, Clover!", "欢迎来甜苹果园，Clover！"),
                ("say", "applejack", "Look! This is my family photo.", "看！这是我的全家福。"),
                ("narr", "话音刚落，小表妹抱着一罐苹果汁跑过来，脚下一滑——哗，半罐果汁全泼在了照片上。"),
                ("say", "applejack", "Whoa! The names are all smudged!", "哇！名字全糊掉啦！"),
                ("narr", "苹果嘉儿一点也不生气，只是把帽子扶正，诚实地说了句：「这下我可认不出谁是谁了。」"),
                ("say", "applejack", "I am honest: I need help.", "我老实说：我得找人帮忙啦。"),
                ("narr", "紫悦蹲下来轻轻擦照片，忽然发现相框背后卡着一角焦黄的纸——和那封神秘信是同一种纸。"),
                ("say", "twilight", "The letter has been here too…", "那封信也来过这儿……"),
                ("narr", "照片里第一位是位笑眯眯的女士。苹果嘉儿想先把她介绍给你。"),

                ("quiz", {
                    "who": "applejack",
                    "scene": "苹果嘉儿指着照片里的女士，想介绍「这是我的妈妈」。",
                    "ask": "哪一句正确？",
                    "options": [
                        {"en": "This is my mum.", "zh": "这是我的妈妈。", "note": ""},
                        {"en": "This is my dad.", "zh": "这是我的爸爸。", "note": "dad 是爸爸；妈妈是 mum（也可以说 mother）。"},
                        {"en": "Is this my mum?", "zh": "这是我的妈妈吗？", "note": "句尾有问号就是提问，不是在介绍别人。"},
                    ],
                    "answer": 0,
                    "explain": "介绍别人用「This is my …」；句尾一加问号，就变成提问了。",
                    "tip": "This is my + 家人（介绍）。",
                    "after": ("say", "applejack", "That's my mum. She makes the best apple pie.", "那是我妈妈。她做的苹果派最棒了。"),
                }),

                ("narr", "果汁顺着相框往下滴，把旁边一行字泡开了：「This is my ___.」，只剩下三个空格。"),

                ("fill", {
                    "who": "applejack",
                    "scene": "你指着照片里戴草帽的男士，学着苹果嘉儿的样子介绍他。",
                    "sentence": "This is my ___.",
                    "answer": "dad",
                    "word_zh": "爸爸",
                    "explain": "「This is my dad.」= 这是我爸爸。dad 是口语里的「爸爸」，3 个字母。",
                    "note": "妈妈的英文是 mum，爸爸的英文是 d 开头、3 个字母。",
                    "tip": "mum = 妈妈，dad = 爸爸。",
                    "after": ("narr", "字母归位，相框边缘闪了一下。神秘信上又多了一个字母：L。"),
                }),

                ("narr", "照片角落里，一个扎蝴蝶结的小姑娘被果汁糊得最厉害。你差点把她认成苹果嘉儿的姐姐。"),
                ("say", "applejack", "Is this your sister?", "这是你的姐姐吗？"),
                ("narr", "苹果嘉儿摇摇头，笑着纠正：那是她的表妹，从苹果鲁萨来参加聚会的。"),

                ("quiz", {
                    "who": "applejack",
                    "scene": "苹果嘉儿问：「Is this your sister?」（这是你的姐姐吗？）其实那不是姐姐，是表妹。",
                    "ask": "你该怎样回答？",
                    "options": [
                        {"en": "No, it's my cousin.", "zh": "不是，她是我的表妹。", "note": ""},
                        {"en": "Yes, it isn't.", "zh": "是的，她不是。", "note": "Yes 和 isn't 自相矛盾：肯定说 Yes, it is.，否定说 No, it isn't."},
                        {"en": "Yes, it is my cousin.", "zh": "是的，她是我的表妹。", "note": "Yes 表示「是」，后面又说 cousin（表妹），前后矛盾。"},
                    ],
                    "answer": 0,
                    "explain": "一般疑问句回答用 Yes, it is. / No, it isn't.。不是姐姐，先答 No，再说出正确的人。",
                    "tip": "cousin = 堂（表）兄弟姐妹。",
                }),

                ("narr", "长桌那头，史密斯婆婆招手让你过去。她身后站着一大家子，数都数不清。"),
                ("say", "applejack", "She's my cousin. And I have a big family!", "她是我表妹。我有一个大家庭！"),

                ("fill", {
                    "who": "applejack",
                    "scene": "苹果嘉儿说她家很大，你也想试着说「我有一个大家庭」。",
                    "sentence": "I have a big ___.",
                    "answer": "family",
                    "word_zh": "家庭",
                    "explain": "「I have a big family.」= 我有一个大家庭。family 是「家庭」，6 个字母。",
                    "note": "「家庭」的英文是 f 开头、6 个字母，和 friend 一样是 f 开头哦。",
                    "tip": "I have a … = 我有一个…",
                }),

                ("choice", "苹果嘉儿递来两块苹果派：「先帮婆婆认照片，还是先尝一口？」", [
                    ("先帮婆婆把照片认完", "婆婆笑得眼睛弯弯：「好孩子，认完人再吃，派会更甜！」"),
                    ("先尝一口苹果派", "苹果嘉儿哈哈大笑：「诚实地说……这派确实香！来，边吃边认！」"),
                ]),

                ("narr", "院子那头，一个戴棒球帽的小马正把苹果筐搬进谷仓。苹果嘉儿抬手指了指远处。"),
                ("say", "applejack", "Is that your brother?", "那是你的弟弟吗？"),
                ("narr", "那个小家伙正巧回头挥了挥蹄子。苹果嘉儿想知道，你会不会回答这句问话。"),

                ("quiz", {
                    "who": "applejack",
                    "scene": "苹果嘉儿指着远处的弟弟问：「Is that your brother?」（那是你的弟弟吗？）你想说「是的」。",
                    "ask": "哪一句回答正确？",
                    "options": [
                        {"en": "Yes, it is.", "zh": "是的。", "note": ""},
                        {"en": "Yes, I am.", "zh": "是的，我是。", "note": "问的是「那是…吗」，要用 it 回答；I am 是回答 Are you…? 的。"},
                        {"en": "No, it is.", "zh": "不是，它是。", "note": "No 和 it is 矛盾，肯定就答 Yes, it is."},
                    ],
                    "answer": 0,
                    "explain": "远处用 that：Is that your brother? 回答 Yes, it is. / No, it isn't.",
                    "tip": "this 指近处；that 指远处。",
                }),

                ("narr", "一家人一起把相框拆开擦干净。你猜怎么着？相框夹层里，真的藏着一小片焦黄的纸。"),
                ("say", "twilight", "Another piece of the letter!", "又一片信纸！"),
                ("narr", "照片终于晾干了。白发苍苍的史密斯婆婆走过来，笑眯眯地摸摸你的头。"),

                ("fill", {
                    "who": "applejack",
                    "scene": "苹果嘉儿把婆婆介绍给你认识。",
                    "sentence": "This is my ___.",
                    "answer": "grandma",
                    "word_zh": "奶奶；姥姥",
                    "explain": "「This is my grandma.」= 这是我奶奶（姥姥）。grandma 是口语里的「奶奶」，7 个字母。",
                    "note": "「奶奶」的英文是 g 开头、7 个字母；爷爷 grandpa 和它是同一个开头。",
                    "tip": "grandma = 奶奶 / 姥姥；grandpa = 爷爷 / 姥爷。",
                    "after": ("narr", "婆婆把一小片信纸递给紫悦。纸上的字母慢慢排整齐：L、O。"),
                }),

                ("narr", "太阳偏西，二十七个苹果派只剩下三个。苹果嘉儿把最后一张全家福摆回壁炉上。"),
                ("say", "applejack", "Grandma says you are a good helper!", "婆婆说你是个好帮手！"),

                ("quiz", {
                    "who": "applejack",
                    "scene": "苹果嘉儿想再确认一次：照片里那位白发婆婆是她的奶奶。她该怎么介绍？",
                    "ask": "哪一句是在「介绍」而不是「提问」？",
                    "options": [
                        {"en": "This is my grandma.", "zh": "这是我的奶奶。", "note": ""},
                        {"en": "Is this your grandma?", "zh": "这是你的奶奶吗？", "note": "有 Is 开头和问号，这是在提问，不是介绍。"},
                        {"en": "Yes, it is.", "zh": "是的。", "note": "这是在回答问题，不是在介绍人物。"},
                    ],
                    "answer": 0,
                    "explain": "陈述句介绍人：This is my …；一般疑问句提问：Is this your …?；回答才用 Yes, it is.",
                    "tip": "This is …（介绍）／ Is this …?（提问）",
                }),

                ("narr", "临走时，苹果嘉儿塞给你一袋苹果。她说，认错人没关系，问一句就清楚了。"),
                ("say", "applejack", "A big family needs a lot of questions!", "一家人丁兴旺，就得多问几句！"),
                ("narr", "紫悦把两片信纸拼在一起：H、E、L、L、O——第一个单词，竟是 HELLO。"),
                ("report", "第 2 封友谊报告 · My Big Family",
                 "亲爱的宇宙公主：今天我们弄湿了一张全家福，却因此认识了苹果嘉儿的妈妈、爸爸、表妹和婆婆。"
                 "她教我们：介绍用「This is my …」，不确定就问「Is this your …?」，回答用「Yes, it is.」。"
                 "原来一家人也会认错人，问清楚就好了。信上的第一个单词拼好了：HELLO。"),
                ("narr", "友谊地图的第二个光点灭了，第三个亮在永恒自由森林边缘，一闪一闪，像在等谁。"),
                ("narr", "穗龙的小本子上又多了四个词。他抬头看了眼紫悦，把本子往背后藏了藏。"),
            ],
        },

        ########################################################################
        ## 第 3 章  Unit 3 Amazing animals
        ## 地点：永恒自由森林 Everfree Forest ｜ 主角：柔柔、云宝（客串）
        ## 麻烦：一只迷路的小动物躲进森林，柔柔不敢大声喊，怕吓到它
        ########################################################################
        {
            "num": 3,
            "unit": "Unit 3  Amazing animals",
            "title": "永恒自由森林的小客人",
            "goal": "What's this / that? / It's a … / Do you have a pet?",
            "bg": "forest",
            "loot": "第 3 封友谊报告《A Quiet Hello》",
            "beats": [
                ("scene", "forest"),
                ("narr", "永恒自由森林的边缘，柔柔的小屋外挂着一排鸟食盒。第三个光点，就落在屋后的灌木丛里。"),
                ("narr", "柔柔蹲在草地上，声音轻得像一片叶子：「嘘……它躲了一早上了，我不敢大声说话。」"),
                ("say", "fluttershy", "Shh… look! A little fox.", "嘘……看！一只小狐狸。"),
                ("narr", "灌木丛里，一只橙红色的小狐狸歪着头看你，尾巴尖一抖一抖。"),
                ("narr", "更糟的是，它嘴里叼着一小片焦黄的纸——又是那封神秘信的一角。"),
                ("say", "fluttershy", "It's scared. Please talk softly.", "它害怕了。请轻轻地说。"),
                ("narr", "柔柔想问你那是什么，可她怕自己的声音太大，就把问题写在了一片叶子上。"),

                ("quiz", {
                    "who": "fluttershy",
                    "scene": "柔柔指着你脚边的小动物，用气音问：「What's this?」（这是什么？）",
                    "ask": "你该怎样回答？",
                    "options": [
                        {"en": "It's a fox.", "zh": "它是一只狐狸。", "note": ""},
                        {"en": "It's a red panda.", "zh": "它是一只小熊猫。", "note": "red panda 是小熊猫，脚边这只是 fox（狐狸）。"},
                        {"en": "Yes, it is.", "zh": "是的。", "note": "这是回答 Is it…? 的；What's this? 问「是什么」，要答 It's a…"},
                    ],
                    "answer": 0,
                    "explain": "问「What's this?」就用「It's a + 动物」回答。近处的东西用 this。",
                    "tip": "What's this? — It's a fox.",
                    "after": ("say", "fluttershy", "Yes… a fox. You said it so gently.", "对……是狐狸。你说得好轻好轻。"),
                }),

                ("narr", "小狐狸忽然一转身，叼着纸片钻进树洞。树洞旁还蹲着一只打哈欠的小猫。"),

                ("fill", {
                    "who": "fluttershy",
                    "scene": "你指着树洞边的小猫，轻轻告诉柔柔：你也有一只这样的小动物。",
                    "sentence": "I have a ___.",
                    "answer": "cat",
                    "word_zh": "猫",
                    "explain": "「I have a cat.」= 我有一只猫。cat 是「猫」，3 个字母。",
                    "note": "「猫」的英文是 c 开头、3 个字母；小狗是 d 开头的 dog。",
                    "tip": "I have a + 动物（单数前面要加 a）。",
                    "after": ("narr", "小猫喵了一声，像是听懂了。信纸碎片上浮出一个字母：F。"),
                }),

                ("narr", "「嗖——」一道蓝影从头顶掠过，云宝一个急转弯停在枝头，翅膀带起的气流把纸片吹上了高高的树杈。"),
                ("say", "rainbow", "Whoops! Did I do that? Awesome landing though.", "哎呀！我吹的？不过落地姿势超帅。"),
                ("say", "fluttershy", "It's… it's okay, Rainbow Dash.", "没……没关系的，云宝。"),
                ("narr", "柔柔只好用她那招「凝视」让树上的小松鼠别乱跑，然后抬头望向高高的树杈。"),
                ("narr", "纸片离得远，她写下一句问话，却把 this 和 that 弄混了。"),

                ("quiz", {
                    "who": "fluttershy",
                    "scene": "纸片在远处高高的树杈上，你想问柔柔「那是什么？」",
                    "ask": "哪一句是「那是什么」？",
                    "options": [
                        {"en": "What's that?", "zh": "那是什么？", "note": ""},
                        {"en": "What's this?", "zh": "这是什么？", "note": "this 指近处；纸片在远处高高的树上，要用 that。"},
                        {"en": "Who's that?", "zh": "那是谁？", "note": "Who 问「谁」，问动物和东西要用 What。"},
                    ],
                    "answer": 0,
                    "explain": "近处用 this，远处用 that；问东西用 What，问人用 Who。",
                    "tip": "What's that? — It's a red panda.",
                }),

                ("say", "fluttershy", "It's a red panda! It took the paper up the tree.", "是小熊猫！它把纸片带上树了。"),
                ("narr", "小熊猫探出头，好奇地打量你们。柔柔忽然小声问起你的家。"),

                ("quiz", {
                    "who": "fluttershy",
                    "scene": "柔柔问：「Do you have a pet?」（你有宠物吗？）你想说「是的，我有一只狗」。",
                    "ask": "哪一句完全正确？",
                    "options": [
                        {"en": "Yes, I do. I have a dog.", "zh": "是的，我有。我有一只狗。", "note": ""},
                        {"en": "Yes, I am. I have a dog.", "zh": "是的，我是。我有一只狗。", "note": "Do you…? 要用 do 回答，am 是回答 Are you…? 的。"},
                        {"en": "Yes, I do. I have dog.", "zh": "是的，我有。我有狗。", "note": "dog 是一只，前面要加 a：I have a dog."},
                    ],
                    "answer": 0,
                    "explain": "「Do you …?」答 Yes, I do. / No, I don't.；可数名词单数前要加 a。",
                    "tip": "I have a cat / a dog / a pet.",
                }),

                ("choice", "云宝在树上喊：「要我飞上去把纸片叼下来吗？」柔柔小声问你怎么办。", [
                    ("请云宝慢慢飞，别吓到小熊猫", "柔柔松了口气：「谢谢你……轻声一点，它就会自己下来。」"),
                    ("大家一起在树下轻轻唱歌", "柔柔轻轻笑了：「好呀，它最喜欢有人小声唱歌了。」"),
                ]),

                ("fill", {
                    "who": "fluttershy",
                    "scene": "柔柔想再确认一次：你家那只小猫算不算「宠物」。她把问题说了一遍。",
                    "sentence": "Do you have a ___?",
                    "answer": "pet",
                    "word_zh": "宠物",
                    "explain": "「Do you have a pet?」= 你有宠物吗？pet 是「宠物」，3 个字母。",
                    "note": "「宠物」的英文是 p 开头、3 个字母。",
                    "tip": "pet = 宠物；dog、cat、bird、fish 都可以是 pet。",
                    "after": ("narr", "小熊猫顺着树干慢慢爬下来，把纸片轻轻放在柔柔的蹄子里。"),
                }),

                ("say", "fluttershy", "It likes you! You are brave AND quiet.", "它喜欢你！你又勇敢又轻声。"),
                ("narr", "林子另一头，一只长颈鹿从树梢上探出脖子，柔柔仰头看了好久。"),

                ("fill", {
                    "who": "fluttershy",
                    "scene": "你抬头看着那只高高的长颈鹿，学着用英语描述它。",
                    "sentence": "The giraffe is ___.",
                    "answer": "tall",
                    "word_zh": "高的",
                    "explain": "「The giraffe is tall.」= 长颈鹿很高。tall 是「高的」，4 个字母。",
                    "note": "「高的」的英文是 t 开头、4 个字母。",
                    "tip": "tall = 高的；fast = 快的；cute = 可爱的。",
                }),

                ("quiz", {
                    "who": "rainbow",
                    "scene": "云宝指着远处一闪而过的蓝色小鸟，想问「那是什么？」",
                    "ask": "哪一句最合适？",
                    "options": [
                        {"en": "What's that? It's a bird.", "zh": "那是什么？是一只鸟。", "note": ""},
                        {"en": "What's this? It's a bird.", "zh": "这是什么？是一只鸟。", "note": "小鸟已经飞远了，远处要用 that。"},
                        {"en": "Who's that? It's a bird.", "zh": "那是谁？是一只鸟。", "note": "问动物用 What，不用 Who。"},
                    ],
                    "answer": 0,
                    "explain": "远处的东西用 that 提问，答句用 It's a + 动物。",
                    "tip": "What's that? — It's a bird.",
                }),

                ("narr", "夕阳照进森林，小狐狸领着小熊猫、小猫和长颈鹿，绕着你们慢慢走了一圈，像在说谢谢。"),
                ("say", "twilight", "Three light spots done. The letter says HELLO, F…", "三个光点完成了。信上写着 HELLO, F……"),
                ("report", "第 3 封友谊报告 · A Quiet Hello",
                 "亲爱的宇宙公主：今天我们学会，和小动物做朋友不一定要大声。"
                 "柔柔用「What's this?」和「What's that?」轻轻问，用「It's a fox.」轻轻答。"
                 "云宝差点把事情搞砸，可她一句「对不起」就让大家又笑了起来。信上多了一个字母：F。"),
                ("narr", "第四个光点亮在城堡的花园里，紫悦的脸微微一红：「那……那是我负责的地方。」"),
                ("narr", "穗龙把小狐狸送的一片羽毛夹进小本子，跟在最后，一路小跑。"),
            ],
        },

        ########################################################################
        ## 第 4 章  Unit 4 Plants around us
        ## 地点：友谊城堡花园 ｜ 主角：紫悦、珍奇
        ## 麻烦：紫悦把花园的花养蔫了，她列了 27 条计划，却忘了最要紧的事
        ########################################################################
        {
            "num": 4,
            "unit": "Unit 4  Plants around us",
            "title": "城堡花园的二十七条计划",
            "goal": "Do you like …? / I like … / We can … / Plants need …",
            "bg": "garden",
            "loot": "第 4 封友谊报告《What Plants Need》",
            "beats": [
                ("scene", "garden"),
                ("narr", "友谊城堡的后花园里，第四个小光点停在一条长椅上。可长椅四周的花，全都垂着脑袋。"),
                ("narr", "紫悦抱着一摞书站在花坛边，纸上密密麻麻，写着整整二十七条「拯救花园计划」。"),
                ("say", "twilight", "Step one: make a list. Step two: make another list…", "第一步：列个清单。第二步：再列一个清单……"),
                ("say", "twilight", "The flowers are thirsty… and I have NO idea why!", "花儿渴了……可我完全想不出为什么！"),
                ("narr", "「亲爱的，」珍奇提着新窗帘从回廊走来，用蹄尖轻轻点了点花坛，「它们要的可不是计划书。」"),
                ("say", "rarity", "Darling, a plant does not read lists.", "亲爱的，植物可不会看清单呀。"),
                ("say", "rarity", "Do you like apples? I picked some for you.", "你喜欢苹果吗？我摘了一些给你。"),
                ("narr", "她把一只红苹果递到你面前，顺口问了一句。"),

                ("quiz", {
                    "who": "twilight",
                    "scene": "紫悦问你：「Do you like apples?」（你喜欢苹果吗？）你很喜欢苹果。",
                    "ask": "你该怎样回答？",
                    "options": [
                        {"en": "Yes, I do.", "zh": "是的，我喜欢。", "note": ""},
                        {"en": "Yes, I like.", "zh": "是的，我喜欢。", "note": "回答 Do you…? 要用 do 代替前面的动词，不能只说 Yes, I like."},
                        {"en": "Yes, I am.", "zh": "是的，我是。", "note": "Do you…? 用 do 回答；am 是回答 Are you…? 的。"},
                    ],
                    "answer": 0,
                    "explain": "「Do you like …?」答 Yes, I do. / No, I don't.",
                    "tip": "Do you…? — Yes, I do. / No, I don't.",
                    "after": ("say", "twilight", "I like bananas. And you?", "我喜欢香蕉。你呢？"),
                }),

                ("fill", {
                    "who": "twilight",
                    "scene": "你想告诉紫悦「我喜欢香蕉」，把句子里的字母拼好。",
                    "sentence": "I like ___.",
                    "answer": "bananas",
                    "word_zh": "香蕉（复数）",
                    "explain": "「I like bananas.」= 我喜欢香蕉。说喜欢一类东西时，可数名词要用复数，结尾加 -s。",
                    "note": "喜欢「香蕉这一类」，要说复数 bananas，结尾有 s，一共 7 个字母。",
                    "tip": "I like apples / bananas / flowers.（泛指一类用复数）",
                }),

                ("narr", "珍奇把窗帘往旁边一搭，蹲下来摸了摸土：「干得像饼干。」紫悦的脸更红了。"),
                ("say", "twilight", "How can we help? I will write step twenty-eight!", "我们能怎么帮忙？我来写第二十八条！"),
                ("say", "rarity", "No more lists. Just water, darling.", "别再列清单啦，亲爱的，浇水就好。"),

                ("quiz", {
                    "who": "twilight",
                    "scene": "紫悦问：「How can we help?」（我们能怎么帮忙？）",
                    "ask": "你该怎样回答？",
                    "options": [
                        {"en": "We can water the flowers.", "zh": "我们可以给花浇水。", "note": ""},
                        {"en": "Yes, we can.", "zh": "是的，我们可以。", "note": "How 问「怎么帮」，要说出具体办法，不能只答 Yes。"},
                        {"en": "We can water flowers are.", "zh": "我们可以浇花是。", "note": "句子结构乱了。说 We can water the flowers. 就好。"},
                    ],
                    "answer": 0,
                    "explain": "「How can we help?」要回答具体办法：We can + 动词 + 东西。",
                    "tip": "We can + 动词 + 东西。",
                }),

                ("narr", "大家提来水桶，一趟一趟地浇。水渗进泥土，花叶慢慢挺了起来。"),
                ("say", "twilight", "Good! Let's water them together.", "好！我们一起给它们浇水。"),
                ("narr", "紫悦一边松土，一边念起植物真正需要的三样东西，可最后一个词被水花打湿了。"),

                ("choice", "珍奇递来两样东西：「帮花园的话，你想先拿哪个？」", [
                    ("小水壶", "珍奇点头：「实用又优雅，选得好！」"),
                    ("她新做的花边窗帘", "珍奇捂住脸：「哦不，这可是给城堡大厅用的！……不过你真有眼光。」"),
                ]),

                ("fill", {
                    "who": "twilight",
                    "scene": "紫悦说：植物需要空气、水和阳光。你把最后一个词填上。",
                    "sentence": "Plants need air, water and ___.",
                    "answer": "sun",
                    "word_zh": "阳光；太阳",
                    "explain": "「Plants need air, water and sun.」= 植物需要空气、水和阳光。sun 是「太阳、阳光」，3 个字母。",
                    "note": "最后一个词是「太阳、阳光」，s 开头、3 个字母。",
                    "tip": "列举三样东西：A, B and C。",
                    "after": ("narr", "阳光正好从云缝里落下来，照在湿漉漉的花瓣上，亮得像撒了一层糖。"),
                }),

                ("narr", "松土的时候，紫悦的蹄子碰到一样硬东西：泥土里埋着一角焦黄的纸，正是信上缺的那一块。"),
                ("say", "twilight", "The letter followed us all the way home!", "那封信一路跟我们回家了！"),

                ("quiz", {
                    "who": "twilight",
                    "scene": "紫悦说「I like flowers.」，你也想告诉她「我喜欢花」——要说一句陈述句。",
                    "ask": "哪一句是「我喜欢花」？",
                    "options": [
                        {"en": "I like flowers.", "zh": "我喜欢花。", "note": ""},
                        {"en": "Do you like flowers?", "zh": "你喜欢花吗？", "note": "有 Do 和问号就是提问，不是陈述。"},
                        {"en": "I like flower?", "zh": "我喜欢花吗？", "note": "句尾问号表示提问；泛指花要用复数 flowers，用句号。"},
                    ],
                    "answer": 0,
                    "explain": "陈述自己喜欢什么：I like + 复数名词，句号结尾，不是问句。",
                    "tip": "I like flowers. ／ Do you like flowers?",
                }),

                ("narr", "珍奇把信纸碎片擦干净，摊在长椅上。她忽然发现，纸背面画着一朵小小的花。"),
                ("say", "rarity", "How lovely! Air, water and sun help it grow.", "真美！空气、水和阳光帮它长大。"),

                ("fill", {
                    "who": "rarity",
                    "scene": "珍奇说：空气、水和阳光帮助植物生长。把最后一个词拼好。",
                    "sentence": "They help plants ___.",
                    "answer": "grow",
                    "word_zh": "生长",
                    "explain": "「They help plants grow.」= 它们帮助植物生长。grow 是「生长」，4 个字母。",
                    "note": "「生长」的英文是 g 开头、4 个字母，和 garden（花园）同一个开头。",
                    "tip": "grow = 生长；help … grow = 帮助…生长。",
                    "after": ("narr", "花坛里最后一朵花抬起了头。信上的字母又亮了一个：R。"),
                }),

                ("quiz", {
                    "who": "rarity",
                    "scene": "珍奇想问你喜不喜欢花，她该怎么说？",
                    "ask": "哪一句是在「提问」？",
                    "options": [
                        {"en": "Do you like flowers?", "zh": "你喜欢花吗？", "note": ""},
                        {"en": "I like flowers.", "zh": "我喜欢花。", "note": "这是陈述句，说的是自己的喜好，不是在问别人。"},
                        {"en": "Yes, I do.", "zh": "是的，我喜欢。", "note": "这是回答，不是提问。"},
                    ],
                    "answer": 0,
                    "explain": "提问用 Do you like …?；陈述用 I like …；回答用 Yes, I do. / No, I don't.",
                    "tip": "Do you like …? → Yes, I do.",
                }),

                ("narr", "紫悦把那二十七条计划折成一只纸鹤，插在花坛边，自己也笑了。"),
                ("say", "twilight", "Four pages… I mean, four reports. The garden is happy again.", "四页……不对，是四封报告。花园又开心起来了。"),
                ("narr", "紫悦把信上认出的字母连起来：HELLO, FR…。她盯着那两个字母，忽然安静了。"),
                ("report", "第 4 封友谊报告 · What Plants Need",
                 "亲爱的宇宙公主：我今天写了二十七条计划，却忘了花最需要的只是空气、水和阳光。"
                 "珍奇提醒我，帮忙不一定要写很多字，「We can water the flowers.」就够了。"
                 "原来最有用的办法，常常是最简单的那一句。信上多了一个字母：R。"),
                ("narr", "第五个光点亮在彩虹瀑布方向。远远地，传来一声闷闷的「轰隆」。"),
                ("narr", "穗龙蹲在花坛边，认真地把「grow」这个词描了三遍，才小跑着追上队伍。"),
            ],
        },

        ########################################################################
        ## 第 5 章  Unit 5 The colourful world
        ## 地点：彩虹瀑布 Rainbow Falls ｜ 主角：云宝、珍奇
        ## 麻烦：云宝练彩虹音爆，把调色盘撞翻了，瀑布褪成灰白色
        ########################################################################
        {
            "num": 5,
            "unit": "Unit 5  The colourful world",
            "title": "彩虹瀑布褪了色",
            "goal": "What colour is it? / What colours do you like? / … make …",
            "bg": "rainbow",
            "loot": "第 5 封友谊报告《Red and Blue Make Purple》",
            "beats": [
                ("scene", "rainbow"),
                ("narr", "彩虹瀑布是彩虹节最重要的地方。可今天，瀑布的水竟变成了灰白色，像被谁把颜色全洗掉了。"),
                ("narr", "云宝正在练习彩虹音爆，一个俯冲没刹住，正好撞翻了岸边的调色盘。"),
                ("say", "rainbow", "Uh… the rainbow was HERE a second ago!", "呃……彩虹一秒钟前还在这儿的！"),
                ("say", "rainbow", "Look at the waterfall! What colour is it?", "看那瀑布！它是什么颜色？"),
                ("narr", "珍奇踩着小碎步冲过来，一看见灰扑扑的水，差点晕在云宝翅膀上。"),
                ("say", "rarity", "Darling! I need those colours for the festival ribbons!", "亲爱的！彩虹节的彩带还等着这些颜色呢！"),
                ("narr", "紫悦摊开信纸：第五个光点落在调色盘里，混在一起的颜色正慢慢往外冒字母。"),
                ("say", "twilight", "Let's put the colours back, one word at a time.", "我们把颜色一个词一个词地放回去吧。"),
                ("narr", "调色盘最下面还剩一道干净的橙色。云宝指着它问你。"),

                ("quiz", {
                    "who": "rainbow",
                    "scene": "云宝指着调色盘最下面的一条问：「What colour is it?」",
                    "ask": "你该怎样回答？",
                    "options": [
                        {"en": "It's orange.", "zh": "它是橙色的。", "note": ""},
                        {"en": "It's a orange.", "zh": "它是一个橙色。", "note": "颜色词是形容词，前面不加 a：It's orange."},
                        {"en": "It's orange colour.", "zh": "它是橙色颜色。", "note": "「它是橙色的」只说 It's orange，不用再加 colour。"},
                        {"en": "It's colour orange.", "zh": "它是颜色橙。", "note": "语序反了：颜色词要放在 It's 后面，colour 不用出现。"},
                    ],
                    "answer": 0,
                    "explain": "问颜色：What colour is it? 答：It's + 颜色。颜色词前面不加 a。",
                    "tip": "It's red / orange / blue.",
                    "after": ("say", "rainbow", "Orange! Okay, one colour down. Five to go!", "橙色！好，一种颜色归位，还差五种！"),
                }),

                ("narr", "珍奇从围裙口袋里掏出一张湿了角的信纸碎片，上面写着半句话：「I like ___ and pink.」"),

                ("fill", {
                    "who": "rarity",
                    "scene": "珍奇想告诉你她喜欢哪两种颜色，把缺的那个颜色词拼回去。",
                    "sentence": "I like ___ and pink.",
                    "answer": "red",
                    "word_zh": "红色",
                    "explain": "「I like red and pink.」= 我喜欢红色和粉色。red 是「红色」，3 个字母。",
                    "note": "「红色」的英文是 r 开头、3 个字母。",
                    "tip": "red 红色；pink 粉色；blue 蓝色。",
                    "after": ("narr", "红色一归位，瀑布底下的水悄悄泛起一层暖暖的粉。"),
                }),

                ("say", "rarity", "With red and blue, we can make purple!", "红色和蓝色能调出紫色！"),
                ("narr", "她把两支颜料一挤，紫色真的在盘子里转开了。云宝看得眼睛都直了。"),

                ("quiz", {
                    "who": "rarity",
                    "scene": "珍奇把红色和蓝色混在一起，变成了紫色。她想把这个秘密讲给你听。",
                    "ask": "哪一句是「红色和蓝色调出紫色」？",
                    "options": [
                        {"en": "Red and blue make purple.", "zh": "红色和蓝色调出紫色。", "note": ""},
                        {"en": "Red and blue is purple.", "zh": "红色和蓝色是紫色。", "note": "两种颜色一起变化，用 make（调出），不用 is。"},
                        {"en": "Red and blue make a purple.", "zh": "红色和蓝色调出一个紫色。", "note": "颜色词前面不加 a：make purple。"},
                    ],
                    "answer": 0,
                    "explain": "两种颜色混合用 make：Red and blue make purple.",
                    "tip": "A and B make C.",
                }),

                ("narr", "云宝把一支蓝色颜料笔塞到你蹄子里，指着最长的那根彩带。"),
                ("say", "rainbow", "Colour it blue! Make it awesome!", "把它涂成蓝色！涂得超帅一点！"),

                ("fill", {
                    "who": "rainbow",
                    "scene": "云宝说：「Colour it blue.」意思是「把它涂成蓝色」。你也跟着拼一遍。",
                    "sentence": "Colour it ___!",
                    "answer": "blue",
                    "word_zh": "蓝色",
                    "explain": "「Colour it blue!」= 把它涂成蓝色！blue 是「蓝色」，4 个字母。",
                    "note": "「蓝色」的英文是 b 开头、4 个字母。",
                    "tip": "colour 当动词：Colour it + 颜色。",
                    "after": ("narr", "蓝彩带一甩上天空，瀑布顶端的灰白裂开一道缝，透出一线蓝。"),
                }),

                ("choice", "珍奇举起两支颜料：「下一种颜色，你来挑！」", [
                    ("先调黄色，像太阳一样", "珍奇眼睛一亮：「黄色！和珍奇的品味一样明亮。」"),
                    ("先调紫色，云宝说最酷", "云宝在空中翻了个跟头：「紫色最酷！我投一票！」"),
                ]),

                ("say", "rainbow", "What colours do you like?", "你喜欢哪些颜色？"),

                ("quiz", {
                    "who": "rainbow",
                    "scene": "云宝问你：「What colours do you like?」你喜欢红色和粉色。",
                    "ask": "你该怎样回答？",
                    "options": [
                        {"en": "I like red and pink.", "zh": "我喜欢红色和粉色。", "note": ""},
                        {"en": "I like a red and pink.", "zh": "我喜欢一个红色和粉色。", "note": "颜色词前面不加 a。"},
                        {"en": "I like red and pink colour.", "zh": "我喜欢红色和粉色颜色。", "note": "说颜色不用再加 colour：I like red and pink."},
                    ],
                    "answer": 0,
                    "explain": "说喜欢什么颜色，直接说颜色词，两个颜色之间用 and。",
                    "tip": "What colours do you like? — I like …",
                }),

                ("narr", "彩带一根根挂起来，瀑布的颜色像被谁从下往上刷了一遍，重新流光溢彩。"),
                ("narr", "你抬头看天，云宝忽然问：那天空该是什么颜色？信纸上正好留着一个空。"),

                ("fill", {
                    "who": "rainbow",
                    "scene": "你抬头看着天空，把这句话补完整。",
                    "sentence": "The ___ is blue.",
                    "answer": "sky",
                    "word_zh": "天空",
                    "explain": "「The sky is blue.」= 天空是蓝色的。sky 是「天空」，3 个字母。",
                    "note": "「天空」的英文是 s 开头、3 个字母；大海是 sea。",
                    "tip": "sky 天空；sea 大海。",
                    "after": ("narr", "最后一道灰退去，彩虹瀑布轰的一声，重新亮成七彩。信上浮出字母：I。"),
                }),

                ("quiz", {
                    "who": "rarity",
                    "scene": "珍奇想问你，那条最长的彩带是什么颜色。",
                    "ask": "哪一句问得最合适？",
                    "options": [
                        {"en": "What colour is it?", "zh": "它是什么颜色？", "note": ""},
                        {"en": "What colours do you like?", "zh": "你喜欢哪些颜色？", "note": "这是在问喜好，不是问某样东西的颜色。"},
                        {"en": "It's blue.", "zh": "它是蓝色的。", "note": "这是回答，不是提问。"},
                    ],
                    "answer": 0,
                    "explain": "问一样东西的颜色：What colour is it?（单数 colour）；答 It's + 颜色。",
                    "tip": "What colour is it? — It's blue.",
                }),

                ("say", "rainbow", "Beautiful! The fifth page is on the waterfall!", "太美了！第五片信纸在瀑布上面！"),
                ("narr", "一片焦黄的纸顺着水花飘下来，稳稳落在珍奇的蹄尖上。"),
                ("say", "rarity", "Six colours. Only one light spot left.", "六种颜色都回来了。只剩最后一个光点了。"),
                ("narr", "紫悦把字母排好：HELLO, FRI…。她小声念了一遍，忽然抬头看向方糖角落的方向。"),
                ("report", "第 5 封友谊报告 · Red and Blue Make Purple",
                 "亲爱的宇宙公主：云宝撞翻了调色盘，彩虹瀑布褪成了灰白色。"
                 "我们一起用「What colour is it?」认颜色，用「Red and blue make purple.」把颜色调回来。"
                 "弄砸了没关系，朋友一起动手，颜色反而比原来更多。信上多了一个字母：I。"),
                ("narr", "天色渐暗，第六个光点在方糖角落的橱窗里一闪一闪，像一支快要点着的蜡烛。"),
                ("narr", "穗龙怀里抱着那片湿信纸，走得比谁都慢，尾巴尖又冒了一小缕烟。"),
            ],
        },

        ########################################################################
        ## 第 6 章  Unit 6 Useful numbers
        ## 地点：方糖角落 Sugarcube Corner ｜ 主角：碧琪、紫悦
        ## 麻烦：彩虹节大蛋糕的订单被面粉糊住，数字全不见了
        ########################################################################
        {
            "num": 6,
            "unit": "Unit 6  Useful numbers",
            "title": "面粉糊住的生日订单",
            "goal": "How old …? / How many …? / Here you are / It's … o'clock",
            "bg": "party",
            "loot": "第 6 封友谊报告《The Big Cake Order》",
            "beats": [
                ("scene", "party"),
                ("narr", "夜里的方糖角落还亮着灯。碧琪系着围裙，正在给彩虹节做一个三层大蛋糕。"),
                ("narr", "第六个光点，就落在柜台那张订单上——可惜整张单子刚被一阵面粉扑了个正着。"),
                ("say", "pinkie", "Welcome! It's my birthday today too!", "欢迎！今天也是我的生日！"),
                ("say", "pinkie", "Oh no! The numbers are GONE! My Pinkie Sense is tingling!", "不好！数字全没啦！我的碧琪预感在跳！"),
                ("narr", "年龄、蜡烛、取蛋糕的时间、价钱，全成了白花花的一片。碧琪急得原地蹦了七下。"),
                ("say", "twilight", "One word at a time. We can read it back.", "一个词一个词来。我们能把它读回来。"),
                ("narr", "碧琪抹开脸上的面粉，先好奇地问起你。"),

                ("quiz", {
                    "who": "pinkie",
                    "scene": "碧琪好奇地问：「How old are you?」（你几岁了？）你今年九岁。",
                    "ask": "你该怎样回答？",
                    "options": [
                        {"en": "I'm nine years old.", "zh": "我九岁。", "note": ""},
                        {"en": "I'm fine, thank you.", "zh": "我很好，谢谢。", "note": "这是回答 How are you?（你好吗）的；问年龄要回答数字。"},
                        {"en": "I'm Clover.", "zh": "我是 Clover。", "note": "这是在说名字；问年龄要说数字。"},
                    ],
                    "answer": 0,
                    "explain": "「How old are you?」问年龄，答「I'm + 数字（+ years old）」。「How are you?」才是问好。",
                    "tip": "How old are you? ≠ How are you?",
                    "after": ("say", "pinkie", "Nine! Same as my little cousin. Cake for everyone!", "九岁！和我小表妹一样。人人都有蛋糕！"),
                }),

                ("narr", "碧琪数了数围裙口袋里的钱，抬起头告诉你有多少。"),

                ("fill", {
                    "who": "pinkie",
                    "scene": "碧琪数了数口袋里的钱，把这句话补完整。",
                    "sentence": "I have ___ yuan.",
                    "answer": "ten",
                    "word_zh": "十",
                    "explain": "「I have ten yuan.」= 我有十元钱。ten 是「十」，3 个字母。",
                    "note": "「十」的英文是 t 开头、3 个字母；「一」是 one。",
                    "tip": "one two three four five six seven eight nine ten",
                    "after": ("narr", "订单上第一个数字亮了回来：10。"),
                }),

                ("narr", "蛋糕上的蜡烛被门口的风吹得晃来晃去。碧琪想数一数，却越数越乱。"),

                ("quiz", {
                    "who": "pinkie",
                    "scene": "碧琪问：「How many candles?」（有几根蜡烛？）蛋糕上插着五根蜡烛。",
                    "ask": "你该怎样回答？",
                    "options": [
                        {"en": "Five.", "zh": "五根。", "note": ""},
                        {"en": "I'm five.", "zh": "我五岁。", "note": "「I'm five.」是在说年龄；问数量要答 Five."},
                        {"en": "Five candles is.", "zh": "五根蜡烛是。", "note": "语序不对。回答数量直接说 Five. 或 There are five."},
                        {"en": "I'm five years.", "zh": "我五岁。", "note": "少了个 old，而且这是在说年龄，不是蜡烛数量。"},
                    ],
                    "answer": 0,
                    "explain": "「How many …?」问数量，直接回答数字，也可以说 There are five.",
                    "tip": "How many + 复数名词。",
                }),

                ("choice", "碧琪举着蜡烛盒：「要不要先猜猜，这盒子里有几根？」", [
                    ("猜五根", "碧琪倒出来一数：「哇，真的五根！你的预感也很准嘛！」"),
                    ("猜十根", "碧琪哗啦一倒：「只有五根！不过十根的蛋糕……我们可以下次做！」"),
                ]),

                ("narr", "店员探出头说，三层大蛋糕要七点才能烤好。时间还早，大家先去挑蜡烛。"),

                ("fill", {
                    "who": "pinkie",
                    "scene": "店员看了看钟，告诉你们蛋糕做好的时间。",
                    "sentence": "It's seven ___.",
                    "answer": "o'clock",
                    "word_zh": "……点钟",
                    "explain": "「It's seven o'clock.」= 七点了。o'clock 表示整点，中间有一个小撇号。",
                    "note": "「整点」的英文是 o 开头，中间有一个小撇号。撇号已经镶在信上，只要把其余字母拼好。",
                    "tip": "It's + 数字 + o'clock.",
                }),

                ("say", "pinkie", "That's ten yuan, please.", "一共十元，请付钱。"),
                ("narr", "你把十元钱递过去，店员笑着把蛋糕盒推回来。"),

                ("quiz", {
                    "who": "pinkie",
                    "scene": "你把十元钱递给店员，店员要告诉你「给你」。",
                    "ask": "哪一句是「给你」？",
                    "options": [
                        {"en": "Here you are.", "zh": "给你。", "note": ""},
                        {"en": "How old are you?", "zh": "你几岁了？", "note": "这是在问年龄，和「给你」没关系。"},
                        {"en": "Here you are ten.", "zh": "给你十。", "note": "「给你」就说 Here you are.，后面不加数字。"},
                    ],
                    "answer": 0,
                    "explain": "递东西给别人时说「Here you are.」；别人说 Thank you 时，你回答 You're welcome.",
                    "tip": "Here you are. = 给你。",
                    "after": ("narr", "蛋糕盒的缝隙里，露出一角焦黄的纸——第六片信纸找到了。"),
                }),

                ("narr", "大家围着三层蛋糕唱起生日歌。碧琪闭眼许愿，蜡烛一齐亮了。"),

                ("fill", {
                    "who": "pinkie",
                    "scene": "你祝碧琪生日快乐，把这句祝福拼完整。",
                    "sentence": "Happy ___!",
                    "answer": "birthday",
                    "word_zh": "生日",
                    "explain": "「Happy birthday!」= 生日快乐！birthday 是「生日」，8 个字母，由 birth 和 day 组成。",
                    "note": "「生日」的英文是 b 开头、8 个字母，由 birth 和 day 两个部分拼成。",
                    "tip": "Happy birthday! — Thank you!",
                    "after": ("say", "pinkie", "Thank you! Best birthday EVER!", "谢谢！最棒的生日！"),
                }),

                ("narr", "订单上的数字一个一个回来了：9、10、5、7、10。碧琪把单子举得高高的，面粉扑簌簌往下掉。"),

                ("quiz", {
                    "who": "twilight",
                    "scene": "紫悦想确认一下蛋糕几点做好，她该怎么问？",
                    "ask": "哪一句是在问「时间」？",
                    "options": [
                        {"en": "What time is it?", "zh": "几点了？", "note": ""},
                        {"en": "How old are you?", "zh": "你几岁了？", "note": "How old 问的是年龄，不是钟点。"},
                        {"en": "How many candles?", "zh": "有几根蜡烛？", "note": "How many 问的是数量，不是时间。"},
                    ],
                    "answer": 0,
                    "explain": "问时间用 What time is it?；回答整点用 It's seven o'clock. 问年龄用 How old，问数量用 How many。",
                    "tip": "What time is it? — It's seven o'clock.",
                }),

                ("say", "pinkie", "Thank you! Six pages! Let's go to the castle!", "谢谢！六片都齐了！我们回城堡吧！"),
                ("say", "twilight", "Six reports. But the letter still has no name on it…", "六封报告都写好了。可信上还是没有署名……"),
                ("narr", "紫悦把六片信纸拼在一起，读出那句话：HELLO, FRIEND… 后面还空着一行。"),
                ("report", "第 6 封友谊报告 · The Big Cake Order",
                 "亲爱的宇宙公主：碧琪把订单弄成了白花花一片，我们却因此把数字全念了一遍——"
                 "「How old are you?」「How many candles?」「It's seven o'clock.」「Here you are.」"
                 "最忙的一晚，也是最香的一晚。信上读到：HELLO, FRIEND…，最后一行还空着。"),
                ("narr", "六个光点一起亮起，在夜空里连成一条回城堡的路。"),
                ("narr", "穗龙走在最后，抱紧了那本写满单词的小本子，一句话也没说。"),
            ],
        },

        ########################################################################
        ## 第 7 章  Revision 友谊城堡 · 真相
        ## 地点：友谊城堡图书馆 ｜ 主角：全体 + 穗龙 + 宇宙公主的回信
        ## 反转：写信的人就是穗龙，一个喷嚏把报告烧乱了
        ########################################################################
        {
            "num": 7,
            "unit": "Revision  Rainbow Festival",
            "title": "城堡里的第七封信",
            "goal": "Unit 1-6 综合复习：问好、家庭、动物、植物、颜色、数字",
            "bg": "ending",
            "loot": "最后一封《Friendship is Magic》",
            "beats": [
                ("scene", "ending"),
                ("narr", "夜色落下来，小马谷的星星一颗接一颗亮了。六匹小马和 Clover 回到友谊城堡的图书馆。"),
                ("narr", "六片信纸拼在长桌上，几乎完整了：HELLO, FRIEND… 最后一行，还差几个词。"),
                ("say", "twilight", "Six reports, and still no name. Who sent this letter?", "六封报告都齐了，还是没有署名。这封信到底是谁寄的？"),
                ("narr", "壁炉边传来「咳咳」两声。穗龙站在那儿，尾巴尖冒了一缕烟，小本子掉在了地上。"),
                ("narr", "紫悦捡起本子：第一页到第六页，工工整整抄着这一路拼对的每一个单词。"),
                ("say", "twilight", "Spike… was it you?", "穗龙……是你吗？"),
                ("narr", "小龙把脸埋进爪子里，点了点头，声音小得几乎听不见。"),
                ("narr", "原来今早他替紫悦给宇宙公主寄友谊报告，一个喷嚏没忍住，龙火把信烧出一串乱七八糟的字母洞。"),
                ("narr", "他不敢说，就悄悄跟着大家走了一整天，把大家说对的每个单词都记下来，想一个一个把信补回去。"),
                ("say", "twilight", "Oh, Spike. You should have told us.", "哦，穗龙。你早点告诉我们就好啦。"),
                ("say", "pinkie", "That's what friends are for! Fixing things together!", "朋友就是干这个的呀！一起把事情补好！"),
                ("narr", "穗龙抬起头，眼睛亮亮的。他小声说：那最后一行，能不能请大家一起拼完？"),
                ("say", "twilight", "Let's read it out loud, from Unit 1 to Unit 6.", "我们把 Unit 1 到 Unit 6，一起大声念一遍吧。"),

                ("quiz", {
                    "who": "twilight",
                    "scene": "复习第一站：刚见面时，紫悦问：「What's your name?」",
                    "ask": "哪一句是在回答名字？",
                    "options": [
                        {"en": "My name is Clover.", "zh": "我叫 Clover。", "note": ""},
                        {"en": "I'm nine.", "zh": "我九岁。", "note": "这是在说年龄，别人问名字时要答名字。"},
                        {"en": "I'm fine.", "zh": "我很好。", "note": "这是回答 How are you? 的，不是名字。"},
                        {"en": "My name Clover.", "zh": "我名字 Clover。", "note": "少了 is：My name is Clover. 不能只说 My name Clover."},
                    ],
                    "answer": 0,
                    "explain": "介绍名字：My name is … 或 I'm …。别忘了中间那个 is。",
                    "tip": "My name is + 名字。",
                }),

                ("fill", {
                    "who": "fluttershy",
                    "scene": "复习第二站：柔柔轻轻说「Nice to meet you.」，你想回应她。",
                    "sentence": "Nice to meet you, ___!",
                    "answer": "too",
                    "word_zh": "也",
                    "explain": "回应别人的见面问候：Nice to meet you, too. 句尾的 too 表示「我也一样」。",
                    "note": "别人先说，回答时在句尾加「也」——t 开头、3 个字母。",
                    "tip": "Nice to meet you. → Nice to meet you, too.",
                    "after": ("narr", "信上第一行的字母稳稳亮了起来。穗龙把本子翻到最后一页。"),
                }),

                ("narr", "苹果嘉儿从门口探进头，手里还拎着那袋苹果；云宝停在窗台上，翅膀上沾着一点蓝颜料。"),

                ("quiz", {
                    "who": "applejack",
                    "scene": "复习第三站：苹果嘉儿指着照片问「Is this your sister?」，那是表妹。",
                    "ask": "哪一句回答正确？",
                    "options": [
                        {"en": "No, it's my cousin.", "zh": "不是，她是我的表妹。", "note": ""},
                        {"en": "Yes, it isn't.", "zh": "是的，她不是。", "note": "Yes 和 isn't 矛盾；否定要说 No, it isn't."},
                        {"en": "Yes, I am.", "zh": "是的，我是。", "note": "问的是「这是…吗」，要用 it 回答。"},
                    ],
                    "answer": 0,
                    "explain": "一般疑问句：先答 No，再说出正确的人；Yes / No 后面别自相矛盾。",
                    "tip": "Is this …? — Yes, it is. / No, it isn't.",
                }),

                ("quiz", {
                    "who": "twilight",
                    "scene": "复习第四站：紫悦问你：「Do you like animals?」（你喜欢小动物吗？）你很喜欢。",
                    "ask": "哪一句回答正确？",
                    "options": [
                        {"en": "Yes, I do.", "zh": "是的，我喜欢。", "note": ""},
                        {"en": "Yes, I am.", "zh": "是的，我是。", "note": "Do you…? 用 do 回答，不能用 am。"},
                        {"en": "Yes, I like.", "zh": "是的，我喜欢。", "note": "回答 Do you…? 要用 do，不能只说 Yes, I like."},
                    ],
                    "answer": 0,
                    "explain": "「Do you …?」答 Yes, I do. / No, I don't.",
                    "tip": "Do you like …? — Yes, I do. / No, I don't.",
                }),

                ("fill", {
                    "who": "twilight",
                    "scene": "复习第五站：你告诉穗龙，植物需要水和阳光。",
                    "sentence": "Plants need water and ___.",
                    "answer": "sun",
                    "word_zh": "阳光",
                    "explain": "「Plants need water and sun.」= 植物需要水和阳光。sun 是「太阳、阳光」，3 个字母。",
                    "note": "「阳光」的英文是 s 开头、3 个字母。",
                    "tip": "Plants need air, water and sun.",
                }),

                ("choice", "碧琪端来最后一块蛋糕：「许愿之前，先说一句话给穗龙听吧？」", [
                    ("「没关系，我们还是好朋友！」", "穗龙鼻子一酸，尾巴尖的烟变成了一颗小爱心。"),
                    ("「下次打喷嚏记得往后一点！」", "穗龙噗嗤笑出来：「我、我一定练习！」"),
                ]),

                ("quiz", {
                    "who": "rarity",
                    "scene": "复习第六站：珍奇把红色和蓝色混在一起，想说「调出紫色」。",
                    "ask": "哪一句正确？",
                    "options": [
                        {"en": "Red and blue make purple.", "zh": "红色和蓝色调出紫色。", "note": ""},
                        {"en": "Red and blue is purple.", "zh": "红色和蓝色是紫色。", "note": "两种颜色混合用 make，不用 is。"},
                        {"en": "Red and blue make a purple.", "zh": "红色和蓝色调出一个紫色。", "note": "颜色词前面不加 a。"},
                    ],
                    "answer": 0,
                    "explain": "两种颜色混合用 make：A and B make C。",
                    "tip": "Red and blue make purple.",
                }),

                ("quiz", {
                    "who": "star",
                    "scene": "复习第七站：小光点从信纸里飞出来，问你：「How old are you?」你九岁。",
                    "ask": "你该怎样回答？",
                    "options": [
                        {"en": "I'm nine years old.", "zh": "我九岁。", "note": ""},
                        {"en": "I'm nine yuan.", "zh": "我九元。", "note": "yuan 是钱，年龄要用 years old。"},
                        {"en": "I'm fine.", "zh": "我很好。", "note": "这是回答 How are you? 的。"},
                    ],
                    "answer": 0,
                    "explain": "问年龄答「I'm + 数字 + years old」；yuan 是钱，不是年龄。",
                    "tip": "I'm nine years old.",
                }),

                ("narr", "六匹小马围成一圈，把这一路说过的话一句句念给信听。信上的字，一行一行亮了起来。"),

                ("fill", {
                    "who": "star",
                    "scene": "最后一行了。你伸出手，想和穗龙、和所有小马做朋友。",
                    "sentence": "Let's be ___!",
                    "answer": "friends",
                    "word_zh": "朋友（复数）",
                    "explain": "「Let's be friends!」= 我们做朋友吧！friends 是 friend 的复数，7 个字母。",
                    "note": "friend 加上表示复数的 s，一共 7 个字母。",
                    "tip": "Let's be friends! = 我们做朋友吧！",
                    "after": ("narr", "最后一个字母落定。整封信亮成金色：HELLO, FRIEND. LET'S BE FRIENDS!"),
                }),

                ("narr", "壁炉里「呼」地腾起一团金色龙火——这次穗龙没打喷嚏。一封盖着太阳印记的信，稳稳落在紫悦手里。"),
                ("say", "twilight", "It's from Princess Celestia!", "是宇宙公主的回信！"),
                ("narr", "信上写着：这封被朋友们一起补好的报告，是她收到过最棒的一封。因为她看见的不是一个不出错的小龙，而是一群愿意一起把错补好的朋友。"),
                ("narr", "宇宙公主还邀请 Clover 成为小马谷的「友谊小使者」，明年彩虹节再来。"),
                ("say", "star", "You did it! The letter is whole again!", "你做到啦！信又完整了！"),
                ("scene", "friends"),
                ("say", "twilight", "Six reports, six friends, and one very brave little dragon.", "六封报告、六个朋友，还有一只很勇敢的小龙。"),
                ("say", "pinkie", "Best Rainbow Festival ever!", "最棒的彩虹节！"),
                ("say", "rainbow", "And no lists this time. Well… maybe one.", "而且这次没有清单。嗯……也许还有一张。"),
                ("narr", "城堡外，彩虹节的灯一盏盏亮起，彩虹从广场一直架到天边。"),
                ("report", "最后一封 · Friendship is Magic",
                 "亲爱的宇宙公主：我们把六封报告都写完了，也终于知道信是谁寄的。"
                 "穗龙一个喷嚏烧乱了报告，却不好意思说；他跟着我们走了一整天，把每个拼对的单词都记在本子上。"
                 "我们学会的不只是 Hello、family、fox、grow、purple 和 seven——还有：弄错了没关系，"
                 "朋友会陪你一个字母一个字母地补回来。友谊，本来就是魔法。"),
                ("narr", "穗龙把小本子递给 Clover，扉页上歪歪扭扭写着一行字：「Thank you, friend.」"),
                ("narr", "大家约好：明年彩虹节，还要一起读故事、拼单词、吃碧琪的蛋糕。"),
                ("narr", "Goodbye! See you next time!　谢谢你，Clover！"),
            ],
        },
    ]

    ## 自动统计：每章题目数、选章卡片用的小马头像
    for _ch in CHAPTERS:
        _q = [b[1] for b in _ch["beats"] if b[0] in ("quiz", "fill")]
        _ch["qcount"] = len(_q)
        _ch["avatar"] = _q[0]["who"]
