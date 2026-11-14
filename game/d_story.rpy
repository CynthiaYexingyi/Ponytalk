################################################################################
##  story_data.rpy
##  故事与题库数据（老师改内容只需要改这个文件）
##
##  PONY      ：角色名字、颜色、立绘
##  CHAPTERS  ：六个单元的故事
##
##  beat 种类：
##    ("narr", 中文旁白)
##    ("say", 角色key, 英文台词, 中文译文)
##    ("quiz", 题目字典)
##
##  quiz 字段：who 出题小马 / scene 情境 / ask 问题 / options 三个选项
##             answer 正确下标 / explain 答对讲解 / tip 小贴士
################################################################################

init python:

    PONY = {
        "twilight":   {"name": "Twilight 紫悦",    "color": "#7b4fb8", "img": "images/pony/twilight.png"},
        "pinkie":     {"name": "Pinkie 碧琪",      "color": "#e8448f", "img": "images/pony/pinkie.png"},
        "applejack":  {"name": "Applejack 苹果嘉儿", "color": "#d97b1e", "img": "images/pony/applejack.png"},
        "rainbow":    {"name": "Rainbow 云宝",     "color": "#2d8fd5", "img": "images/pony/rainbow.png"},
        "rarity":     {"name": "Rarity 珍奇",      "color": "#5b4bc4", "img": "images/pony/rarity.png"},
        "fluttershy": {"name": "Fluttershy 柔柔",  "color": "#d4548f", "img": "images/pony/fluttershy.png"},
    }

    CHARS = {}
    for _k, _v in PONY.items():
        CHARS[_k] = Character(_v["name"], color=_v["color"], who_color=_v["color"])


    CHAPTERS = [

        ########################################################################
        ## 第 1 章  Unit 1 Making friends
        ########################################################################
        {
            "num": 1,
            "unit": "Unit 1  Making friends",
            "title": "新朋友",
            "goal": "Hello / I'm ... / My name is ... / Nice to meet you",
            "bg": "meadow",
            "beats": [
                ("narr", "今天是你第一天来到小马谷。你叫 Sunny，心里有点紧张。"),
                ("narr", "忽然，一只粉色的小马蹦到你面前！"),
                ("say", "pinkie", "Hi! I'm Pinkie Pie.", "嗨！我是碧琪。"),
                ("say", "pinkie", "What's your name?", "你叫什么名字呀？"),
                ("quiz", {
                    "who": "pinkie",
                    "scene": "碧琪在问你的名字。你叫 Sunny。",
                    "ask": "哪一句是在说「我叫 Sunny」？",
                    "options": [
                        {"en": "My name is Sunny.", "zh": "我叫 Sunny。", "note": ""},
                        {"en": "I'm nine.", "zh": "我九岁。", "note": "「I'm nine.」是在回答「How old are you?」（你几岁），不是在说名字。"},
                        {"en": "I'm fine, thank you.", "zh": "我很好，谢谢。", "note": "「I'm fine.」是回答「How are you?」（你好吗）的。"},
                    ],
                    "answer": 0,
                    "explain": "介绍名字用「My name is …」或「I'm …」。问名字就答名字，别把年龄和名字弄混。",
                    "tip": "I'm + 名字 = 我叫…；I'm + 数字 = 我…岁。",
                }),
                ("say", "pinkie", "Nice to meet you, Sunny!", "很高兴认识你，Sunny！"),
                ("quiz", {
                    "who": "pinkie",
                    "scene": "第一次见面，碧琪对你说：「Nice to meet you.」（很高兴认识你。）",
                    "ask": "你该回答哪一句？",
                    "options": [
                        {"en": "Nice to meet you, too.", "zh": "我也很高兴认识你。", "note": ""},
                        {"en": "Nice to meet you.", "zh": "很高兴认识你。", "note": "少了 too，听起来像你又先自我介绍了一次。别人先说，我们回答时要加 too。"},
                        {"en": "Goodbye!", "zh": "再见！", "note": "「Goodbye!」是分别时说的。刚见面就说再见，碧琪会伤心的。"},
                    ],
                    "answer": 0,
                    "explain": "对方说「Nice to meet you.」，我们回答「Nice to meet you, too.」——加一个 too，表示「我也」。",
                    "tip": "too 放在句尾，意思是「也」。",
                }),
                ("say", "pinkie", "Let's be friends! Wave your hand!", "我们做朋友吧！挥一挥你的手！"),
                ("quiz", {
                    "who": "pinkie",
                    "scene": "碧琪举起手，一边挥一边大声说：「Hello!」",
                    "ask": "你也想打招呼，该说哪一句？",
                    "options": [
                        {"en": "Hello! I'm Sunny.", "zh": "你好！我是 Sunny。", "note": ""},
                        {"en": "Goodbye! I'm Sunny.", "zh": "再见！我是 Sunny。", "note": "「Goodbye」是告别的话；见面打招呼要说 Hello 或 Hi。"},
                        {"en": "Thank you! I'm Sunny.", "zh": "谢谢你！我是 Sunny。", "note": "「Thank you」是道谢；打招呼时用 Hello / Hi。"},
                    ],
                    "answer": 0,
                    "explain": "见面用 Hello / Hi，离开用 Goodbye / Bye。两句话意思完全相反，别用错哦。",
                    "tip": "Hello = 你好（见面）；Goodbye = 再见（分开）。",
                }),
                ("say", "pinkie", "Oh! I have to go now.", "哦！我现在得走啦。"),
                ("quiz", {
                    "who": "pinkie",
                    "scene": "碧琪要回家了。她一边走一边朝你挥手说：「Goodbye!」",
                    "ask": "你该说什么？",
                    "options": [
                        {"en": "Goodbye! See you!", "zh": "再见！回头见！", "note": ""},
                        {"en": "Hello! See you!", "zh": "你好！回头见！", "note": "「Hello」是见面时说的，分别时要说 Goodbye。"},
                        {"en": "Nice to meet you.", "zh": "很高兴认识你。", "note": "这句话用在刚见面的时候；现在要分别了，说再见才对。"},
                    ],
                    "answer": 0,
                    "explain": "别人说 Goodbye，你也说 Goodbye 或 See you，这样才是有礼貌的告别。",
                    "tip": "See you! = 回头见！",
                }),
                ("narr", "你交到了在小马谷的第一个朋友。"),
                ("say", "pinkie", "See you tomorrow, Sunny!", "明天见，Sunny！"),
            ],
        },

        ########################################################################
        ## 第 2 章  Unit 2 Different families
        ########################################################################
        {
            "num": 2,
            "unit": "Unit 2  Different families",
            "title": "苹果嘉儿的家",
            "goal": "This is my ... / Is this your ...? / I have a big family",
            "bg": "farm",
            "beats": [
                ("narr", "第二天，你来到苹果嘉儿的农场。"),
                ("say", "applejack", "Welcome to my farm, Sunny!", "欢迎来到我的农场，Sunny！"),
                ("say", "applejack", "Look! This is my family.", "看！这是我的全家福。"),
                ("narr", "照片里有很多人，苹果嘉儿开始一个一个地介绍。"),
                ("quiz", {
                    "who": "applejack",
                    "scene": "苹果嘉儿指着照片里的一位女士，想介绍「这是我的妈妈」。",
                    "ask": "哪一句是在介绍妈妈？",
                    "options": [
                        {"en": "This is my mum.", "zh": "这是我的妈妈。", "note": ""},
                        {"en": "This is my dad.", "zh": "这是我的爸爸。", "note": "dad 是爸爸；妈妈是 mum（也可以说 mother）。"},
                        {"en": "Is this my mum?", "zh": "这是我的妈妈吗？", "note": "句尾有问号，说明是在提问，不是在介绍。"},
                    ],
                    "answer": 0,
                    "explain": "介绍别人用「This is my …」；句尾是问号就变成提问了。",
                    "tip": "This is my + 家人（介绍）；Is this your …?（提问）",
                }),
                ("say", "applejack", "Is this your sister?", "这是你的姐姐吗？"),
                ("narr", "照片里的女孩不是你的姐姐，是你的表妹。"),
                ("quiz", {
                    "who": "applejack",
                    "scene": "苹果嘉儿问你：「Is this your sister?」照片里的女孩不是姐姐，是表妹。",
                    "ask": "你该怎样回答？",
                    "options": [
                        {"en": "No, it's my cousin.", "zh": "不是，她是我的表妹。", "note": ""},
                        {"en": "Yes, it isn't.", "zh": "", "note": "Yes 和 isn't 是矛盾的：要说 Yes, it is. 或 No, it isn't.，不能混着用。"},
                        {"en": "Yes, it is my cousin.", "zh": "", "note": "Yes 表示「是」，可后面又说 cousin（表妹），前后矛盾。"},
                    ],
                    "answer": 0,
                    "explain": "一般疑问句的回答：Yes, it is. 或 No, it isn't. 不是姐姐，就答 No，再说出正确的人。",
                    "tip": "cousin = 表兄弟姐妹。",
                }),
                ("say", "applejack", "And look! Is that your brother?", "再看那边！那是你的弟弟吗？"),
                ("narr", "远处那个男孩确实是你的弟弟。"),
                ("quiz", {
                    "who": "applejack",
                    "scene": "苹果嘉儿指着远处的男孩问：「Is that your brother?」（那是你的弟弟吗？）他确实是你的弟弟。",
                    "ask": "你该怎样回答？",
                    "options": [
                        {"en": "Yes, it is.", "zh": "是的。", "note": ""},
                        {"en": "Yes, I am.", "zh": "是的，我是。", "note": "问的是「那是…吗」，要用 it 回答；I am 是回答「Are you …?」的。"},
                        {"en": "No, it is.", "zh": "", "note": "No 和 it is 矛盾；肯定就答 Yes, it is."},
                    ],
                    "answer": 0,
                    "explain": "远处用 that：Is that your brother? 回答 Yes, it is. 或 No, it isn't.",
                    "tip": "this 近处 / that 远处。",
                }),
                ("say", "applejack", "My family is big. I have a big family!", "我的家很大。我有一个大家庭！"),
                ("quiz", {
                    "who": "applejack",
                    "scene": "你想告诉苹果嘉儿「我有一个大家庭」。",
                    "ask": "哪一句是「我有一个大家庭」？",
                    "options": [
                        {"en": "I have a big family.", "zh": "我有一个大家庭。", "note": ""},
                        {"en": "I have big family.", "zh": "我有大家庭。", "note": "family 是一个，前面要加 a：a big family。"},
                        {"en": "I have a family big.", "zh": "", "note": "英语里形容词要放在名词前面：a big family。"},
                    ],
                    "answer": 0,
                    "explain": "「我有一…」用 I have a …；形容词放在名词前面：a big family。",
                    "tip": "a + 形容词 + 名词。",
                }),
                ("narr", "你学会了介绍家人，也学会了用 he、she、it 回答问题。"),
            ],
        },

        ########################################################################
        ## 第 3 章  Unit 3 Amazing animals
        ########################################################################
        {
            "num": 3,
            "unit": "Unit 3  Amazing animals",
            "title": "森林里的小动物",
            "goal": "What's this / that? / It's a ... / Do you have a pet?",
            "bg": "forest",
            "beats": [
                ("narr", "你走进小马谷的森林。柔柔正在和小动物们玩。"),
                ("say", "fluttershy", "Shh... Look! A little fox.", "嘘…看！一只小狐狸。"),
                ("narr", "小狐狸就在你的脚边。"),
                ("quiz", {
                    "who": "fluttershy",
                    "scene": "柔柔指着你脚边的小动物问：「What's this?」（这是什么？）",
                    "ask": "你该怎样回答？",
                    "options": [
                        {"en": "It's a fox.", "zh": "它是一只狐狸。", "note": ""},
                        {"en": "It's a red panda.", "zh": "它是一只小熊猫。", "note": "red panda 是小熊猫，脚边这只是 fox（狐狸）。"},
                        {"en": "Yes, it is.", "zh": "是的。", "note": "这是回答「Is it …?」的；「What's this?」问「是什么」，要答「It's a …」。"},
                    ],
                    "answer": 0,
                    "explain": "问「What's this?」就用「It's a + 动物」回答。问是什么，就要说是什么。",
                    "tip": "What's this? — It's a fox.",
                }),
                ("say", "fluttershy", "And look over there!", "再看那边！"),
                ("narr", "远处的大树旁，有一头高高的长颈鹿。"),
                ("quiz", {
                    "who": "fluttershy",
                    "scene": "长颈鹿离你们很远。你想问柔柔「那是什么？」，该怎么说？",
                    "ask": "哪一句是「那是什么」？",
                    "options": [
                        {"en": "What's that?", "zh": "那是什么？", "note": ""},
                        {"en": "What's this?", "zh": "这是什么？", "note": "this 指近处的东西；长颈鹿在远处，要用 that。"},
                        {"en": "Who's that?", "zh": "那是谁？", "note": "Who 是问「谁」，问东西或动物要用 What。"},
                    ],
                    "answer": 0,
                    "explain": "近处用 this，远处用 that；问东西用 What，问人用 Who。",
                    "tip": "What's that? — It's a giraffe.",
                }),
                ("quiz", {
                    "who": "fluttershy",
                    "scene": "柔柔问你：「Do you have a pet?」（你有宠物吗？）你家里有一只猫。",
                    "ask": "你该怎样回答？",
                    "options": [
                        {"en": "Yes, I do. I have a cat.", "zh": "是的，我有。我有一只猫。", "note": ""},
                        {"en": "Yes, I am.", "zh": "是的，我是。", "note": "「Do you …?」要用 do 回答；am 是回答「Are you …?」的。"},
                        {"en": "I have cat.", "zh": "我有猫。", "note": "cat 是一只，前面要加 a：I have a cat."},
                    ],
                    "answer": 0,
                    "explain": "「Do you …?」的答语是 Yes, I do. 或 No, I don't.，不是 Yes, I am.",
                    "tip": "Do you have a pet? — Yes, I do. / No, I don't.",
                }),
                ("say", "fluttershy", "Your cat is so cute!", "你的猫好可爱呀！"),
                ("quiz", {
                    "who": "fluttershy",
                    "scene": "你想对柔柔说「我喜欢你的狗」。",
                    "ask": "哪一句是「我喜欢你的狗」？",
                    "options": [
                        {"en": "I like your dog.", "zh": "我喜欢你的狗。", "note": ""},
                        {"en": "I like you dog.", "zh": "", "note": "「你的」是 your；you 是「你」，后面不能直接跟名词。"},
                        {"en": "I like your dogs.", "zh": "我喜欢你的狗（好几只）。", "note": "柔柔只有一只狗，要用单数 dog。"},
                    ],
                    "answer": 0,
                    "explain": "「你的」用 your；一只狗用 dog，几只狗用 dogs。",
                    "tip": "your = 你的；you = 你。",
                }),
                ("narr", "柔柔悄悄告诉你：小动物也喜欢听好听的话。"),
            ],
        },

        ########################################################################
        ## 第 4 章  Unit 4 Plants around us
        ########################################################################
        {
            "num": 4,
            "unit": "Unit 4  Plants around us",
            "title": "小马谷的花园",
            "goal": "Do you like ...? / I like ... / We can ... / Plants need ...",
            "bg": "garden",
            "beats": [
                ("narr", "今天你来到小马谷的花园。紫悦正在给植物浇水。"),
                ("say", "twilight", "Welcome to my garden, Sunny!", "欢迎来我的花园，Sunny！"),
                ("say", "twilight", "Do you like apples?", "你喜欢苹果吗？"),
                ("quiz", {
                    "who": "twilight",
                    "scene": "紫悦举着一个苹果问你：「Do you like apples?」（你喜欢苹果吗？）你很喜欢。",
                    "ask": "你该怎样回答？",
                    "options": [
                        {"en": "Yes, I do.", "zh": "是的，我喜欢。", "note": ""},
                        {"en": "Yes, I like.", "zh": "", "note": "回答「Do you …?」时，要用 do 来代替前面的动词，不能只说 Yes, I like."},
                        {"en": "Yes, I am.", "zh": "是的，我是。", "note": "「Do you …?」用 do 回答；am 是回答「Are you …?」的。"},
                    ],
                    "answer": 0,
                    "explain": "「Do you like …?」的答语是 Yes, I do. 或 No, I don't.",
                    "tip": "问 Do you…? 就答 Yes, I do. / No, I don't.",
                }),
                ("say", "twilight", "I like bananas. And you?", "我喜欢香蕉。你呢？"),
                ("quiz", {
                    "who": "twilight",
                    "scene": "你想告诉紫悦「我喜欢香蕉」。",
                    "ask": "哪一句是「我喜欢香蕉」？",
                    "options": [
                        {"en": "I like bananas.", "zh": "我喜欢香蕉。", "note": ""},
                        {"en": "I like banana.", "zh": "", "note": "泛指香蕉这一类东西，要用复数 bananas。"},
                        {"en": "I like a bananas.", "zh": "", "note": "a 后面只能跟单数名词；这里要用复数 bananas，前面不加 a。"},
                    ],
                    "answer": 0,
                    "explain": "「I like + 复数名词」表示喜欢这一类东西：I like bananas / I like apples.",
                    "tip": "喜欢一类东西，名词用复数。",
                }),
                ("narr", "花园的花有点渴了。"),
                ("say", "twilight", "The flowers are thirsty. How can we help?", "花儿渴了。我们能怎么帮忙呢？"),
                ("quiz", {
                    "who": "twilight",
                    "scene": "紫悦问你：「How can we help?」（我们能怎么帮忙？）",
                    "ask": "你该怎样回答？",
                    "options": [
                        {"en": "We can water the flowers.", "zh": "我们可以给花浇水。", "note": ""},
                        {"en": "We can water flowers are.", "zh": "", "note": "句子结构乱了。说 We can water the flowers. 就好。"},
                        {"en": "Yes, we can.", "zh": "是的，我们可以。", "note": "「How can we help?」是在问「怎么帮」，要说出办法，不能只回答 Yes。"},
                    ],
                    "answer": 0,
                    "explain": "「How can we help?」要回答具体的办法：We can water the flowers.",
                    "tip": "We can + 动词 + 东西。",
                }),
                ("say", "twilight", "Plants need air, water and sun.", "植物需要空气、水和阳光。"),
                ("quiz", {
                    "who": "twilight",
                    "scene": "紫悦在教你植物需要什么：空气、水和阳光。",
                    "ask": "哪一句是「植物需要空气、水和阳光」？",
                    "options": [
                        {"en": "Plants need air, water and sun.", "zh": "植物需要空气、水和阳光。", "note": ""},
                        {"en": "Plants need air, water or sun.", "zh": "", "note": "肯定句里列举用 and；or 用在否定句或疑问句里。"},
                        {"en": "Plants needs air, water and sun.", "zh": "", "note": "Plants 是复数，后面的动词不加 s：plants need。"},
                    ],
                    "answer": 0,
                    "explain": "复数主语 plants + need；列举三个东西，最后两个之间用 and。",
                    "tip": "plants need；A, B and C。",
                }),
                ("narr", "浇完水，花儿好像更精神了。"),
                ("say", "twilight", "Thank you, Sunny! You are a good helper.", "谢谢你，Sunny！你真是个好帮手。"),
            ],
        },

        ########################################################################
        ## 第 5 章  Unit 5 The colourful world
        ########################################################################
        {
            "num": 5,
            "unit": "Unit 5  The colourful world",
            "title": "雨后的彩虹",
            "goal": "What colour is it? / It's ... / Red and blue make ...",
            "bg": "rainbow",
            "beats": [
                ("narr", "雨停了，天空出现了一道美丽的彩虹。云宝从云上飞了下来。"),
                ("say", "rainbow", "Wow! Look at the rainbow!", "哇！你看那道彩虹！"),
                ("quiz", {
                    "who": "rainbow",
                    "scene": "云宝指着彩虹的一条问：「What colour is it?」（它是什么颜色？）那是橙色。",
                    "ask": "你该怎样回答？",
                    "options": [
                        {"en": "It's orange.", "zh": "它是橙色的。", "note": ""},
                        {"en": "It's a orange.", "zh": "", "note": "颜色词是形容词，前面不加 a：It's orange。"},
                        {"en": "It's orange colour.", "zh": "", "note": "「它是橙色的」只说 It's orange；colour 是名词，问颜色时才用 What colour…"},
                    ],
                    "answer": 0,
                    "explain": "问颜色：What colour is it? 答：It's + 颜色。颜色词前面不加 a。",
                    "tip": "It's red / It's orange / It's blue.",
                }),
                ("say", "rainbow", "What colours do you like?", "你喜欢哪些颜色？"),
                ("quiz", {
                    "who": "rainbow",
                    "scene": "云宝问你：「What colours do you like?」（你喜欢哪些颜色？）你喜欢红色和粉色。",
                    "ask": "你该怎样回答？",
                    "options": [
                        {"en": "I like red and pink.", "zh": "我喜欢红色和粉色。", "note": ""},
                        {"en": "I like a red and pink.", "zh": "", "note": "颜色词前面不加 a。"},
                        {"en": "I like red and pink colour.", "zh": "", "note": "说颜色不用再加 colour：I like red and pink."},
                    ],
                    "answer": 0,
                    "explain": "说喜欢什么颜色，直接说颜色词；两个颜色之间用 and。",
                    "tip": "What colours do you like? — I like ...",
                }),
                ("say", "rainbow", "Red and blue make purple!", "红色加蓝色变成紫色！"),
                ("quiz", {
                    "who": "rainbow",
                    "scene": "云宝把红色和蓝色混在一起，变成了紫色。她想告诉你这个秘密。",
                    "ask": "哪一句是「红色加蓝色变成紫色」？",
                    "options": [
                        {"en": "Red and blue make purple.", "zh": "红色加蓝色变成紫色。", "note": ""},
                        {"en": "Red and blue is purple.", "zh": "", "note": "两种颜色一起，用 make（变成）；is 在这里不合适。"},
                        {"en": "Red and blue make a purple.", "zh": "", "note": "颜色词前面不加 a：make purple。"},
                    ],
                    "answer": 0,
                    "explain": "两种颜色混合用 make：Red and blue make purple.",
                    "tip": "A and B make C.",
                }),
                ("say", "rainbow", "Let's draw some red and pink flowers!", "我们来画一些红色和粉色的花吧！"),
                ("quiz", {
                    "who": "rainbow",
                    "scene": "云宝递给你一支画笔，说：「Let's draw some red and pink flowers!」（我们来画红色和粉色的花吧！）",
                    "ask": "你很高兴地答应了，该说哪一句？",
                    "options": [
                        {"en": "Great! Let's draw.", "zh": "太棒了！我们画吧。", "note": ""},
                        {"en": "Yes, I am.", "zh": "是的，我是。", "note": "「Let's …」是邀请，不是问「你是…吗」，不能用 Yes, I am. 回答。"},
                        {"en": "No, I don't.", "zh": "不，我不。", "note": "「No, I don't.」是回答「Do you …?」的；这里是邀请，不想去可以说 No, thanks."},
                    ],
                    "answer": 0,
                    "explain": "「Let's …」是「我们一起…吧」。同意可以说 Great! / Good idea! / OK!",
                    "tip": "Let's = Let us（我们一起）。",
                }),
                ("narr", "彩虹有七种颜色，你学会用英语说出它们的名字了。"),
            ],
        },

        ########################################################################
        ## 第 6 章  Unit 6 Useful numbers
        ########################################################################
        {
            "num": 6,
            "unit": "Unit 6  Useful numbers",
            "title": "碧琪的生日派对",
            "goal": "How old are you? / How many ...? / It's seven o'clock.",
            "bg": "party",
            "beats": [
                ("narr", "今天是碧琪的生日，她办了一个热闹的派对。"),
                ("say", "pinkie", "Welcome to my birthday party!", "欢迎来我的生日派对！"),
                ("quiz", {
                    "who": "pinkie",
                    "scene": "碧琪好奇地问你：「How old are you?」（你几岁了？）你今年九岁。",
                    "ask": "你该怎样回答？",
                    "options": [
                        {"en": "I'm nine years old.", "zh": "我九岁。", "note": ""},
                        {"en": "I'm fine.", "zh": "我很好。", "note": "「I'm fine.」是回答「How are you?」（你好吗）的；问年龄要回答数字。"},
                        {"en": "I'm Sunny.", "zh": "我是 Sunny。", "note": "这是在说名字；问年龄要说数字。"},
                    ],
                    "answer": 0,
                    "explain": "「How old are you?」问年龄，答「I'm + 数字（+ years old）」。「How are you?」才是问好。",
                    "tip": "How old are you? ≠ How are you?（问年龄 ≠ 问好）",
                }),
                ("say", "pinkie", "Look at my cake! So many candles!", "看我的蛋糕！好多蜡烛！"),
                ("quiz", {
                    "who": "pinkie",
                    "scene": "蛋糕上插着五根蜡烛。碧琪问你：「How many candles?」（有几根蜡烛？）",
                    "ask": "你该怎样回答？",
                    "options": [
                        {"en": "Five.", "zh": "五根。", "note": ""},
                        {"en": "I'm five.", "zh": "我五岁。", "note": "「I'm five.」是在说年龄；问数量要答 Five."},
                        {"en": "Five candles is.", "zh": "", "note": "这是中文语序。回答数量直接说 Five. 或 There are five."},
                    ],
                    "answer": 0,
                    "explain": "「How many …?」问数量，直接回答数字，也可以说 There are five.",
                    "tip": "How many + 复数名词。",
                }),
                ("narr", "碧琪还想买一支铅笔，她带你来到小马谷的小商店。"),
                ("say", "pinkie", "I have ten yuan. That's ten yuan, please.", "我有十元。一共十元，请付钱。"),
                ("quiz", {
                    "who": "pinkie",
                    "scene": "你把钱递给碧琪，她该怎样说「给你」？",
                    "ask": "哪一句是「给你」？",
                    "options": [
                        {"en": "Here you are.", "zh": "给你。", "note": ""},
                        {"en": "How old are you?", "zh": "你几岁了？", "note": "这是在问年龄，和「给你」没关系。"},
                        {"en": "Here you are ten.", "zh": "", "note": "「给你」就说 Here you are. 后面不加数字。"},
                    ],
                    "answer": 0,
                    "explain": "递东西给别人时说「Here you are.」；别人对你说 Thank you 时，你回答「You're welcome.」",
                    "tip": "Here you are. = 给你。",
                }),
                ("narr", "天黑了，派对要结束了。"),
                ("say", "pinkie", "It's seven o'clock. Time to go home!", "七点了。该回家啦！"),
                ("quiz", {
                    "who": "pinkie",
                    "scene": "碧琪看着钟问你：「What time is it?」（几点了？）钟上写着 7。",
                    "ask": "你该怎样回答？",
                    "options": [
                        {"en": "It's seven o'clock.", "zh": "七点了。", "note": ""},
                        {"en": "It's seven clock.", "zh": "", "note": "「几点」要用 o'clock；seven clock 是中式说法。"},
                        {"en": "It's o'clock seven.", "zh": "", "note": "顺序反了：数字在前，o'clock 在后。"},
                    ],
                    "answer": 0,
                    "explain": "说时间用「It's + 数字 + o'clock.」",
                    "tip": "It's seven o'clock. = 七点了。",
                }),
                ("say", "pinkie", "This is the best party ever! Thank you, Sunny!", "这是最棒的派对！谢谢你，Sunny！"),
                ("quiz", {
                    "who": "pinkie",
                    "scene": "你对碧琪说：「Happy birthday!」（生日快乐！）",
                    "ask": "碧琪该怎样回答你？",
                    "options": [
                        {"en": "Thank you!", "zh": "谢谢你！", "note": ""},
                        {"en": "Happy birthday!", "zh": "生日快乐！", "note": "别人祝你生日快乐，要道谢，不用把祝福再说回去。"},
                        {"en": "You're welcome.", "zh": "不客气。", "note": "「You're welcome.」是别人对你说 Thank you 之后的回答。"},
                    ],
                    "answer": 0,
                    "explain": "收到祝福要说 Thank you；别人向你道谢时，我们才说 You're welcome.",
                    "tip": "Happy birthday! — Thank you!",
                }),
                ("narr", "六个单元的故事都结束啦。你已经是小马谷的句子小达人！"),
            ],
        },
    ]

    ## 选章卡片右上角的小头像：取该章第一题的出题小马
    for _ch in CHAPTERS:
        _ch["avatar"] = [b for b in _ch["beats"] if b[0] == "quiz"][0][1]["who"]
        _ch["qcount"] = len([b for b in _ch["beats"] if b[0] == "quiz"])

