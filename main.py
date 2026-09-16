import streamlit as st

import streamlit as st

import streamlit as st
from datetime import date

# ==========================================
# 페이지 설정
# ==========================================
st.set_page_config(
    page_title="나의 생일 음료 🧋",
    page_icon="🎂",
    layout="centered"
)

# ==========================================
# 30가지 음료
# ==========================================
drinks = [
    {
        "emoji": "🍓",
        "name": "딸기 라떼",
        "category": "MILK",
        "description": "달콤한 딸기와 부드러운 우유가 만나는 사랑스러운 한 잔.",
        "mood": "오늘은 달콤한 위로가 필요한 날 💗",
        "keyword": "달콤함",
        "color": "#FFF0F5"
    },
    {
        "emoji": "🧋",
        "name": "흑당 버블티",
        "category": "BUBBLE TEA",
        "description": "쫀득한 펄과 진한 흑당의 매력적인 조합.",
        "mood": "재미있고 신나는 하루를 보내고 싶은 날 ✨",
        "keyword": "즐거움",
        "color": "#F8F0E8"
    },
    {
        "emoji": "🍵",
        "name": "말차 라떼",
        "category": "MATCHA",
        "description": "쌉싸름한 말차와 부드러운 우유가 만드는 편안한 맛.",
        "mood": "잠시 모든 걸 내려놓고 쉬고 싶은 날 🌿",
        "keyword": "차분함",
        "color": "#EFF8EA"
    },
    {
        "emoji": "🍋",
        "name": "레몬 에이드",
        "category": "ADE",
        "description": "톡 쏘는 상큼함으로 기분까지 산뜻하게 만들어주는 음료.",
        "mood": "새로운 에너지가 필요한 날 🍋",
        "keyword": "상큼함",
        "color": "#FFFBE8"
    },
    {
        "emoji": "☕",
        "name": "바닐라 라떼",
        "category": "COFFEE",
        "description": "고소한 커피와 은은한 바닐라 향이 어우러진 클래식.",
        "mood": "느긋한 카페 타임을 즐기고 싶은 날 🤎",
        "keyword": "여유",
        "color": "#F8F1EA"
    },
    {
        "emoji": "🍑",
        "name": "복숭아 아이스티",
        "category": "TEA",
        "description": "달콤한 복숭아 향이 가득한 시원하고 산뜻한 음료.",
        "mood": "아무 생각 없이 편안하게 쉬고 싶은 날 🍑",
        "keyword": "편안함",
        "color": "#FFF1E8"
    },
    {
        "emoji": "🍫",
        "name": "초코 밀크",
        "category": "CHOCOLATE",
        "description": "진하고 달콤한 초콜릿으로 행복을 충전하는 한 잔.",
        "mood": "오늘은 확실하게 행복해지고 싶은 날 🍫",
        "keyword": "행복",
        "color": "#F7EEE9"
    },
    {
        "emoji": "🫐",
        "name": "블루베리 요거트",
        "category": "YOGURT",
        "description": "상큼한 블루베리와 부드러운 요거트의 산뜻한 조합.",
        "mood": "가볍고 상쾌한 기분을 원하는 날 💜",
        "keyword": "산뜻함",
        "color": "#F2F0FF"
    },
    {
        "emoji": "🍊",
        "name": "자몽 에이드",
        "category": "ADE",
        "description": "쌉싸름하면서도 상큼한 자몽의 매력을 담은 한 잔.",
        "mood": "평소와 다른 새로운 자극이 필요한 날 🧡",
        "keyword": "새로움",
        "color": "#FFF1EC"
    },
    {
        "emoji": "🥥",
        "name": "코코넛 스무디",
        "category": "SMOOTHIE",
        "description": "시원하고 부드러운 코코넛으로 잠깐의 휴가를 즐겨보세요.",
        "mood": "일상에서 잠시 탈출하고 싶은 날 🏝️",
        "keyword": "휴식",
        "color": "#ECFAF7"
    },
    {
        "emoji": "🍵",
        "name": "얼그레이 밀크티",
        "category": "MILK TEA",
        "description": "은은한 베르가못 향과 부드러운 우유의 우아한 조합.",
        "mood": "조용하고 분위기 있는 시간이 필요한 날 ☁️",
        "keyword": "우아함",
        "color": "#F3F0EA"
    },
    {
        "emoji": "🥭",
        "name": "망고 스무디",
        "category": "SMOOTHIE",
        "description": "잘 익은 망고의 진한 달콤함을 가득 담은 스무디.",
        "mood": "기분을 확 끌어올리고 싶은 날 🌞",
        "keyword": "활력",
        "color": "#FFF5D9"
    },
    {
        "emoji": "🍎",
        "name": "애플 시나몬 티",
        "category": "TEA",
        "description": "사과의 달콤함과 시나몬 향이 포근하게 어우러져요.",
        "mood": "포근한 하루를 보내고 싶은 날 🍂",
        "keyword": "포근함",
        "color": "#FFF1E8"
    },
    {
        "emoji": "🧊",
        "name": "아이스 아메리카노",
        "category": "COFFEE",
        "description": "깔끔하고 시원하게 즐기는 가장 클래식한 커피.",
        "mood": "정신을 번쩍 깨우고 싶은 날 ⚡",
        "keyword": "집중",
        "color": "#EEF4F8"
    },
    {
        "emoji": "🍯",
        "name": "허니 자몽티",
        "category": "TEA",
        "description": "상큼한 자몽에 달콤한 꿀을 더한 기분 좋은 티.",
        "mood": "상쾌하면서도 달콤한 하루가 필요한 날 🍯",
        "keyword": "균형",
        "color": "#FFF8E5"
    },
    {
        "emoji": "🍇",
        "name": "청포도 에이드",
        "category": "ADE",
        "description": "청량한 청포도의 향을 가득 담은 산뜻한 에이드.",
        "mood": "답답한 기분을 날려버리고 싶은 날 💚",
        "keyword": "청량함",
        "color": "#EEFFF1"
    },
    {
        "emoji": "🌹",
        "name": "로즈 티",
        "category": "TEA",
        "description": "은은한 장미 향으로 특별한 분위기를 만들어주는 티.",
        "mood": "오늘은 조금 특별해지고 싶은 날 🌹",
        "keyword": "로맨틱",
        "color": "#FFF0F4"
    },
    {
        "emoji": "🍌",
        "name": "바나나 우유",
        "category": "MILK",
        "description": "달콤하고 부드러운 추억의 맛.",
        "mood": "편안하고 친근한 기분이 필요한 날 💛",
        "keyword": "편안함",
        "color": "#FFFBE8"
    },
    {
        "emoji": "🍓",
        "name": "딸기 요거트 스무디",
        "category": "SMOOTHIE",
        "description": "상큼한 딸기와 부드러운 요거트가 어우러진 달콤한 음료.",
        "mood": "상큼한 행복을 충전하고 싶은 날 💕",
        "keyword": "상큼달콤",
        "color": "#FFF1F6"
    },
    {
        "emoji": "🍵",
        "name": "자스민 그린티",
        "category": "TEA",
        "description": "은은한 꽃 향기가 가볍고 편안하게 퍼지는 차.",
        "mood": "마음의 여유가 필요한 날 🌱",
        "keyword": "힐링",
        "color": "#F0F8EF"
    },
    {
        "emoji": "🍯",
        "name": "허니 밀크티",
        "category": "MILK TEA",
        "description": "부드러운 밀크티에 꿀의 달콤함을 더했어요.",
        "mood": "따뜻한 위로가 필요한 날 🧸",
        "keyword": "따뜻함",
        "color": "#FFF4E5"
    },
    {
        "emoji": "🍉",
        "name": "수박 주스",
        "category": "JUICE",
        "description": "시원하고 달콤한 수박의 맛을 한 잔에 담았어요.",
        "mood": "무더위를 시원하게 날리고 싶은 날 🌊",
        "keyword": "시원함",
        "color": "#FFF1F2"
    },
    {
        "emoji": "🍍",
        "name": "파인애플 에이드",
        "category": "ADE",
        "description": "톡 쏘는 탄산과 상큼한 파인애플의 조합.",
        "mood": "신나는 일이 필요한 날 🎉",
        "keyword": "통통튀는 매력",
        "color": "#FFFBE6"
    },
    {
        "emoji": "🥛",
        "name": "딸기 초코 우유",
        "category": "MILK",
        "description": "딸기의 상큼함과 초콜릿의 달콤함을 한 번에.",
        "mood": "오늘은 달달한 게 무조건 필요한 날 🍫",
        "keyword": "달달함",
        "color": "#FFF0F5"
    },
    {
        "emoji": "🫖",
        "name": "캐모마일 티",
        "category": "TEA",
        "description": "은은하고 부드러운 향으로 편안한 시간을 만들어줘요.",
        "mood": "느긋하게 쉬어가고 싶은 날 🌙",
        "keyword": "안정",
        "color": "#FFFBEF"
    },
    {
        "emoji": "🍒",
        "name": "체리 에이드",
        "category": "ADE",
        "description": "새콤달콤한 체리의 매력을 담은 예쁜 에이드.",
        "mood": "귀엽고 사랑스러운 하루를 보내고 싶은 날 🍒",
        "keyword": "사랑스러움",
        "color": "#FFF0F3"
    },
    {
        "emoji": "🥝",
        "name": "키위 주스",
        "category": "JUICE",
        "description": "톡톡 튀는 키위의 상큼함으로 입안을 깨워보세요.",
        "mood": "새로운 시작이 필요한 날 🥝",
        "keyword": "상쾌함",
        "color": "#F0FFF0"
    },
    {
        "emoji": "🍮",
        "name": "카라멜 마키아토",
        "category": "COFFEE",
        "description": "진한 커피와 달콤한 카라멜이 만들어내는 매력적인 맛.",
        "mood": "오늘은 나에게 작은 사치를 선물하고 싶은 날 ✨",
        "keyword": "달콤한 사치",
        "color": "#FFF3E7"
    },
    {
        "emoji": "🥤",
        "name": "콜드브루",
        "category": "COFFEE",
        "description": "부드럽고 깔끔한 풍미를 가진 시원한 커피.",
        "mood": "깔끔하게 하루를 시작하고 싶은 날 🖤",
        "keyword": "깔끔함",
        "color": "#F1F3F5"
    },
    {
        "emoji": "🌸",
        "name": "벚꽃 라떼",
        "category": "SPECIAL",
        "description": "핑크빛 비주얼과 은은한 달콤함이 매력적인 특별한 라떼.",
        "mood": "예쁜 하루를 보내고 싶은 날 🌸",
        "keyword": "설렘",
        "color": "#FFF1F7"
    }
]

# ==========================================
# CSS
# ==========================================
st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Jua&family=Poppins:wght@400;500;600;700&display=swap');

.stApp {
    background:
        radial-gradient(circle at 5% 5%, #fff1f6 0, transparent 25%),
        radial-gradient(circle at 95% 10%, #eaf8ff 0, transparent 25%),
        linear-gradient(135deg, #ffffff 0%, #fafcff 100%);
}

/* Hero */
.hero {
    text-align: center;
    padding: 38px 10px 25px;
}

.hero-icon {
    font-size: 58px;
}

.hero-title {
    font-family: 'Jua', sans-serif;
    font-size: 44px;
    color: #222;
    margin-top: 5px;
}

.hero-title span {
    color: #FF7190;
}

.hero-subtitle {
    color: #999;
    font-size: 14px;
    margin-top: 8px;
}

/* Input card */
.input-card {
    background: rgba(255,255,255,0.95);
    border: 1px solid #eeeeee;
    border-radius: 25px;
    padding: 28px;
    box-shadow: 0 12px 35px rgba(30,40,60,0.07);
}

/* Result card */
.result-card {
    border-radius: 30px;
    padding: 35px 25px;
    text-align: center;
    margin-top: 25px;
    box-shadow: 0 15px 40px rgba(30,40,60,0.08);
}

.result-emoji {
    font-size: 85px;
}

.result-small {
    color: #999;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 2px;
}

.result-name {
    font-family: 'Jua', sans-serif;
    font-size: 40px;
    color: #222;
    margin: 8px 0;
}

.result-description {
    color: #666;
    font-size: 15px;
    margin-bottom: 22px;
}

.mood-box {
    background: rgba(255,255,255,0.75);
    border-radius: 18px;
    padding: 17px;
    color: #555;
    font-size: 14px;
}

.keyword {
    display: inline-block;
    background: white;
    padding: 7px 15px;
    border-radius: 20px;
    color: #FF7190;
    font-weight: 700;
    margin-top: 12px;
}

.footer {
    text-align: center;
    color: #aaa;
    font-size: 12px;
    margin: 35px 0 15px;
}

div.stButton > button {
    border-radius: 15px;
    border: 1px solid #eeeeee;
    background: white;
    color: #444;
    font-weight: 700;
    transition: 0.2s;
}

div.stButton > button:hover {
    border-color: #ff7190;
    color: #ff7190;
    box-shadow: 0 6px 18px rgba(255,113,144,0.15);
}

</style>
""", unsafe_allow_html=True)

# ==========================================
# 제목
# ==========================================
st.markdown("""
<div class="hero">
    <div class="hero-icon">🎂</div>

    <div class="hero-title">
        나의 <span>생일 음료</span>
    </div>

    <div class="hero-subtitle">
        생일을 입력하면 30가지 음료 중 하나를 골라드려요 🧋
    </div>
</div>
""", unsafe_allow_html=True)

# ==========================================
# 생일 입력
# ==========================================
st.markdown('<div class="input-card">', unsafe_allow_html=True)

st.markdown(
    """
    <div style="
        text-align:center;
        color:#555;
        font-weight:600;
        margin-bottom:12px;
    ">
        🎀 당신의 생일은 언제인가요?
    </div>
    """,
    unsafe_allow_html=True
)

birthday = st.date_input(
    "생년월일",
    value=date(2000, 1, 1),
    min_value=date(1920, 1, 1),
    max_value=date.today(),
    format="YYYY-MM-DD"
)

st.markdown(
    f"""
    <div style="
        text-align:center;
        color:#FF7190;
        font-size:13px;
        font-weight:600;
        margin-top:8px;
    ">
        🎁 {birthday.strftime('%Y년 %m월 %d일')}에 태어난 당신
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# 추천 버튼
# ==========================================
st.write("")

_, center, _ = st.columns([1, 2, 1])

with center:
    recommend = st.button(
        "✨ 나의 음료 확인하기",
        use_container_width=True
    )

# ==========================================
# 생일 → 30가지 음료 중 하나 선택
# ==========================================
if recommend:

    # 생년월일의 모든 숫자를 이용해 결과 결정
    birthday_number = int(
        birthday.strftime("%Y%m%d")
    )

    drink_index = birthday_number % len(drinks)

    st.session_state["drink"] = drinks[drink_index]
    st.session_state["birthday"] = birthday

# ==========================================
# 결과
# ==========================================
if "drink" in st.session_state:

    drink = st.session_state["drink"]

    st.markdown(
        f"""
        <div class="result-card" style="background:{drink['color']}">

            <div class="result-emoji">
                {drink['emoji']}
            </div>

            <div class="result-small">
                YOUR BIRTHDAY DRINK · {drink['category']}
            </div>

            <div class="result-name">
                {drink['name']}
            </div>

            <div class="result-description">
                {drink['description']}
            </div>

            <div class="mood-box">
                💗 <b>오늘의 음료 처방</b><br><br>
                {drink['mood']}
            </div>

            <div class="keyword">
                ✨ {drink['keyword']}
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    if st.button(
        "🔄 다른 음료도 궁금해!",
        use_container_width=True
    ):
        current_index = drinks.index(drink)
        next_index = (current_index + 1) % len(drinks)

        st.session_state["drink"] = drinks[next_index]

        st.rerun()

else:

    st.markdown(
        """
        <div style="
            text-align:center;
            color:#aaa;
            padding:40px 10px;
            font-size:14px;
        ">
            🎀 생일을 입력하고 버튼을 눌러주세요<br><br>
            <span style="font-size:12px;">
                30가지 음료 중 당신에게 어울리는 한 잔을 찾아드릴게요 🧋
            </span>
        </div>
        """,
        unsafe_allow_html=True
    )

# ==========================================
# Footer
# ==========================================
st.markdown("""
<div class="footer">
    Made with 🧋 & a little birthday magic ✨
</div>
""", unsafe_allow_html=True)
