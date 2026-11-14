import streamlit as st
import random

# 設定手機版面配置
st.set_page_config(page_title="專屬情侶互動小遊戲", page_icon="❤️", layout="centered")

st.title("❤️ 專屬情侶互動小遊戲")
st.write("輪流按下按鈕，看看今天誰要接受甜蜜挑戰，或是一鍵決定澳門約會吃什麼！")

# 使用分頁切換不同遊戲模式（把你原本最習慣的真心話大冒險放第一個！）
tab1, tab2, tab3, tab4 = st.tabs([
    "🎲 真心話大冒險", 
    "🍽️ 今天約會吃什麼", 
    "🗺️ 今天去哪裡約會", 
    "✨ 懶人半日遊"
])

# ==========================================
# 遊戲一：真心話大冒險
# ==========================================
with tab1:
    st.subheader("輪到誰抽牌了？")
    
    truths = [
        "【真心話】第一次見到我時，心裡的第一印象是什麼？",
        "【真心話】說出三個你覺得我最可愛的地方！",
        "【真心話】我們在一起後，哪一件事讓你覺得最感動？",
        "【真心話】老實說，有沒有哪一次其實在吃醋但沒說出口？",
        "【真心話】你最喜歡我們一起去過的哪一個約會地點？為什麼？",
        "【真心話】如果我們可以馬上飛去任何一個國家旅行，你最想帶我去哪裡？",
        "【真心話】我做過哪一個小動作，會讓你瞬間覺得心動？",
        "【真心話】你覺得我們兩個人之間，最默契的事情是什麼？",
        "【真心話】有沒有什麼話是一直想對我說，但平時不好意思開口的？",
        "【真心話】如果用一種食物來形容我，你覺得我是什麼？為什麼？",
        "【真心話】最近一次在 IG 看到什麼好笑或可愛的東西時，第一個想到要傳給我？",
        "【真心話】在你心目中，我們兩個最像哪一對動漫或電影情侶？"
    ]
    
    dares = [
        "【大冒險】深情看著對方的眼睛 10 秒鐘不能笑！",
        "【大冒險】給對方一個大大的擁抱，並說出「我愛你」。",
        "【大冒險】幫對方按摩肩膀 1 分鐘。",
        "【大冒險】現在立刻拍一張兩人的搞怪合照！",
        "【大冒險】用最撒嬌的語氣對對方說：「今天全聽你的！」",
        "【大冒險】在對方臉頰上親一下，並誇獎對方今天很好看。",
        "【大冒險】模仿對方平時最常做的一個表情或口頭禪。",
        "【大冒險】打開手機相簿，找出一張你最喜歡的對方照片並說出原因。",
        "【大冒險】牽著對方的手十指緊扣，維持到下一輪抽牌結束！",
        "【大冒險】幫對方拍一張「男友/女友視角」的網美/帥照，拍到滿意為止。",
        "【大冒險】對著對方唱兩句你覺得最浪漫的情歌。",
        "【大冒險】下一杯飲料或小吃，由抽到這張牌的人負責幫對方買單或跑腿！"
    ]

    col1, col2 = st.columns(2)
    with col1:
        if st.button("💬 抽一張真心話", use_container_width=True):
            st.info(random.choice(truths))
    with col2:
        if st.button("🔥 抽一張大冒險", use_container_width=True):
            st.warning(random.choice(dares))

# ==========================================
# 遊戲二：今天約會吃什麼（全按鈕設計，無下拉選單）
# ==========================================
with tab2:
    st.subheader("解決情侶世紀難題：等一下吃什麼？")
    
    fast_foods = [
        "McDonald's 麥當勞 🍔（澳門半島 / 氹仔）",
        "KFC 肯德基 🍗（澳門半島 / 氹仔）",
        "Jollibee 快樂蜂 🍗（議事亭前地｜必點樂脆雞、甜醬意粉）",
        "火滾 Fire Roll 🌯（澳門半島｜必點招牌炙燒卷物）",
        "轉角 Corner ☕（澳門半島｜必點精品咖啡、特色甜品）",
        "飄亭 Flutter 🥤（澳門半島｜必點特色飲品、打卡輕食）",
        "Dino Burger 手工漢堡 🍔（氹仔｜必點雙層和牛芝士堡）",
        "Shake Shack 🍔（路氹城倫敦人｜必點招牌牛肉漢堡、奶昔）",
        "BHC 韓國炸雞 🍗（路氹城｜全智賢代言芝士粉炸雞）",
        "gaga Macau 🥗（路氹城銀河｜必點鮮果茶、和牛千層麵）"
    ]

    local_cafes = [
        "馬慶康南天咖啡室 🍳（澳門半島｜必點叉燒煎雙蛋飯、西多士）",
        "喜蓮咖啡 🍜（氹仔｜必點牛尾湯通粉、炸雲吞）",
        "南屏雅敘 🥪（澳門半島｜必點叉燒蛋治、沙翁）",
        "勝利茶餐室 🥖（澳門半島｜必點巨無霸豬扒包、焗豬扒飯）",
        "澳葡茶餐廳 🍍（澳門半島｜必點花生醬豬扒菠蘿包）",
        "翻撻冰室 🥧（澳門半島｜必點方形葡撻、咖喱雞扒滑蛋飯）",
        "世記咖啡 🥪（氹仔｜必點厚蛋豬扒包、瓦煲奶茶）",
        "梳打冰室 🍜（氹仔｜必點豬頸肉喇沙、炸雞髀）",
        "新鴻發咖啡美食 🍞（澳門半島｜必點超厚切西多士、乾炒牛河）",
        "華嫂冰室 🍍（路氹城銀河｜余文樂力捧招牌菠蘿包）",
        "聯記麵家 🍜（澳門半島｜必點鮮蝦雲吞撈麵、艇仔粥）",
        "梁慶記粥舖 🍲（澳門半島｜必點生滾蟹粥、豬大腸麵）",
        "祥記麵家 🍜（澳門半島｜港星光顧招牌蝦子撈麵）",
        "榮記荳腐麵食 🍮（澳門半島｜必點滑豆腐花、咖喱關東煮）",
        "倫記軟滑腸粉 🥢（澳門半島｜必點即拉蔥花雞蛋腸粉）",
        "雅馨緬甸餐廳 🍜（澳門半島｜必點椰汁雞麵、招牌魚湯粉）",
        "真點心 🥟（澳門半島｜必點鳳爪排骨煲仔飯、雪山叉燒包）",
        "添好運 Tim Ho Wan 🥟（路氹城｜必點酥皮焗叉燒包）",
        "一風堂 Ippudo 🍜（路氹城｜必點白丸/赤丸拉麵）",
        "千鳥 Shabu Shabu 🍲（澳門半島｜一人日式壽喜燒）"
    ]

    portuguese_and_celeb = [
        "番茄屋葡式美食 🍛（澳門半島｜必點葡式焗豬扒飯、木糠布甸）",
        "利多澳門餐 🍛（澳門半島｜必點家常免治豬肉飯）",
        "3 Sardines 三沙丁 🐙（澳門半島｜IG復古風葡國菜）",
        "My Messy Kitchen 🦆（氹仔｜必點免治豬扒包、焗鴨飯）",
        "A Lorcha 船屋葡國餐廳 🦪（澳門半島｜必點蒜蓉白酒炒蜆）",
        "Alma 葡景軒 🥘（氹仔｜必點葡式海鮮濕飯）",
        "Casa Maquista 土生公館 🥩（氹仔｜必點葡式焗肉餅）",
        "ALBERGUE 1601 婆仔屋 🦆（澳門半島｜必點葡式焗鴨飯）",
        "法蘭度餐廳 Fernando's 🐷（路環黑沙｜必點葡式烤乳豬）",
        "Brown & Friends Cafe 🐻（路氹城｜LINE FRIENDS主題餐廳）",
        "Vivienne Westwood Café ☕（路氹城上葡京｜英倫風下午茶）",
        "Gordon Ramsay Pub & Grill 🥩（路氹城倫敦人｜地獄廚神威靈頓牛柳）",
        "淮揚曉宴 🍲（路氹城倫敦人｜貝克漢姆光顧名廚餐廳）",
        "協成海鮮火鍋 🦞（路氹城銀河｜生猛海鮮火鍋）",
        "自助山 The Grand Buffet 🦞（路氹城上葡京｜環球自助餐）"
    ]

    desserts_and_icecream = [
        "好好記手工雪糕 🍨（澳門半島｜必點開心果雪糕、港式奶茶雪糕）",
        "檸檬車露 LemonCello 🍋（氹仔｜必點檸檬車露、榴槤雪糕）",
        "Kika Gelato 🍵（澳門半島｜必點宇治抹茶雪糕、海鹽焦糖）",
        "冰堂 PengTong Gelato 🍨（氹仔｜必點薑汁撞奶雪糕、開心果）",
        "莫義記 🍨（氹仔官也街｜必點貓山王榴槤雪糕、木糠布甸）",
        "禮記雪糕 🍦（澳門半島｜必點懷舊雪糕三文治、紅豆雪條）",
        "義順牛奶公司 🥛（澳門半島｜必點馳名雙皮燉奶、薑汁撞奶）",
        "洪馨椰子 🥥（澳門半島｜必點手工原味椰子雪糕）",
        "澤賢記 🧇（澳門半島 / 氹仔｜IG爆紅葡撻雞蛋仔）",
        "鐵餅號 🧇（澳門半島｜IG人氣拉絲麻糬雞蛋仔）",
        "BAMU 八目烘焙 🥧（澳門半島｜必點焦糖酥皮蛋撻）",
        "PANPAN 🥧（澳門半島｜IG大熱開心果巴斯克蛋撻）",
        "瑪嘉烈蛋撻店 🥧（澳門半島｜必點酥皮葡式蛋撻）",
        "安德魯餅店 🥧（路環｜必點原味葡式蛋撻）",
        "曼撻格利亞 Manteigaria 🥧（澳門半島｜正宗里斯本葡撻）",
        "國華雞蛋仔 🧇（澳門半島｜原味雞蛋仔、花生醬格仔餅）",
        "榮記牛雜 🍢（澳門半島｜大三巴旁明星光顧咖喱牛雜）",
        "長洲平記糯米糍 🥭（氹仔官也街｜特大芒果糯米糍）"
    ]

    all_foods = fast_foods + local_cafes + portuguese_and_celeb + desserts_and_icecream

    if st.button("🎰 全澳門隨機盲抽一間！", use_container_width=True):
        chosen = random.choice(all_foods)
        st.balloons()
        st.success(f"決定就是它了：**{chosen}**！")

    col_f1, col_f2 = st.columns(2)
    with col_f1:
        if st.button("🍔 快餐 / 輕食小店", use_container_width=True):
            chosen = random.choice(fast_foods)
            st.balloons()
            st.success(f"決定吃：**{chosen}**！")
        if st.button("🍛 葡國菜 / 名人名店", use_container_width=True):
            chosen = random.choice(portuguese_and_celeb)
            st.balloons()
            st.success(f"決定吃：**{chosen}**！")

    with col_f2:
        if st.button("🍜 茶餐廳 / 粉麵點心", use_container_width=True):
            chosen = random.choice(local_cafes)
            st.balloons()
            st.success(f"決定吃：**{chosen}**！")
        if st.button("🍨 雪糕 / 甜品掃街", use_container_width=True):
            chosen = random.choice(desserts_and_icecream)
            st.balloons()
            st.success(f"決定吃：**{chosen}**！")

# ==========================================
# 遊戲三：今天去哪裡約會（純按鈕設計）
# ==========================================
with tab3:
    st.subheader("吃飽後不知道去哪？按按鈕決定！")
    
    outdoor_places = [
        "龍環葡韻 & 嘉模聖母堂（氹仔｜文青拍照、浪漫歐陸風情）",
        "瘋堂斜巷 & 婆仔屋（澳門半島｜葡式黃色建築、牽手漫步）",
        "主教山小堂（澳門半島｜俯瞰旅遊塔與南灣湖日落夜景）",
        "黑沙海灘 & 龍爪角海岸徑（路環｜聽海浪聲、吹海風散步）",
        "路環十月初五馬路 & 聖方濟各聖堂（路環｜韓劇《宮》取景地、慢活散步）",
        "大潭山郊野公園斜行升降機（氹仔｜搭透明升降機看金光大道夜景）",
        "巴黎人鐵塔觀景台 & 愛情鎖橋（路氹城｜夜晚燈光秀超浪漫）",
        "戀愛巷 & 大三巴牌坊夜景（澳門半島｜粉紅牆壁情侶打卡）",
        "關前正街文創區（澳門半島｜尋寶特色小店、順路掃街）"
    ]

    indoor_places = [
        "teamLab 超自然空間（威尼斯人｜沉浸式光影藝術展、互拍大片）",
        "澳門藝術博物館 & 文化中心廣場（澳門半島｜安靜看展覽、吹冷氣）",
        "永利皇宮免費觀光纜車 & 音樂噴泉（路氹城｜傍晚搭免費纜車看噴泉）",
        "大賽車博物館（澳門半島｜互動模擬賽車體驗、好拍又好玩）",
        "室內夾公仔 / 遊戲機中心（星皓廣場 / 葡京人｜比賽夾公仔、玩雙人街機）"
    ]

    if st.button("🧭 隨機抽出約會好去處！", use_container_width=True):
        chosen_p = random.choice(outdoor_places + indoor_places)
        st.snow()
        st.success(f"出發去：**{chosen_p}**！")

    col_p1, col_p2 = st.columns(2)
    with col_p1:
        if st.button("🌤️ 戶外散步打卡", use_container_width=True):
            chosen_p = random.choice(outdoor_places)
            st.snow()
            st.success(f"出發去：**{chosen_p}**！")
    with col_p2:
        if st.button("❄️ 室內冷氣約會", use_container_width=True):
            chosen_p = random.choice(indoor_places)
            st.snow()
            st.success(f"出發去：**{chosen_p}**！")

# ==========================================
# 遊戲四：懶人半日遊（一鍵按鈕）
# ==========================================
with tab4:
    st.subheader("不想動腦？一鍵生成半日約會路線！")
    
    if st.button("🪄 一鍵生成今日約會組合！", use_container_width=True):
        p_pick = random.choice(outdoor_places + indoor_places)
        m_pick = random.choice(fast_foods + local_cafes + portuguese_and_celeb)
        d_pick = random.choice(desserts_and_icecream)

        st.balloons()
        st.success("💕 今日專屬約會路線出爐！")
        st.info(f"**1️⃣ 第一站（散步打卡）**：{p_pick}")
        st.info(f"**2️⃣ 第二站（醫肚正餐）**：{m_pick}")
        st.info(f"**3️⃣ 第三站（甜蜜收尾）**：{d_pick}")

