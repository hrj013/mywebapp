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
        "name": "허니 자몽티",import streamlit as st
from datetime import date

# =========================================================
# 페이지 설정
# =========================================================
st.set_page_config(
    page_title="오늘은 뭐 마실까? 🧋",
    page_icon="🧋",
    layout="centered"
)

# =========================================================
# 30가지 음료 데이터
# =========================================================
drinks = [
    {
        "emoji": "🍓",
        "name": "딸기 라떼",
        "category": "MILK",
        "description": "달콤한 딸기와 부드러운 우유가 만나는 사랑스러운 한 잔.",
        "mood": "달콤한 위로가 필요한 날",
        "keyword": "달콤함",
        "color": "#FFF0F5"
    },
    {
        "emoji": "🧋",
        "name": "흑당 버블티",
        "category": "BUBBLE TEA",
        "description": "쫀득한 펄과 진한 흑당의 매력적인 조합.",
        "mood": "재미있고 신나는 하루를 보내고 싶은 날",
        "keyword": "즐거움",
        "color": "#F8F0E8"
    },
    {
        "emoji": "🍵",
        "name": "말차 라떼",
        "category": "MATCHA",
        "description": "쌉싸름한 말차와 부드러운 우유가 만드는 편안한 맛.",
        "mood": "잠시 모든 것을 내려놓고 쉬고 싶은 날",
        "keyword": "차분함",
        "color": "#EFF8EA"
    },
    {
        "emoji": "🍋",
        "name": "레몬 에이드",
        "category": "ADE",
        "description": "톡 쏘는 상큼함으로 기분까지 산뜻하게 만들어주는 음료.",
        "mood": "새로운 에너지가 필요한 날",
        "keyword": "상큼함",
        "color": "#FFFBE8"
    },
    {
        "emoji": "☕",
        "name": "바닐라 라떼",
        "category": "COFFEE",
        "description": "고소한 커피와 은은한 바닐라 향이 어우러진 클래식.",
        "mood": "느긋한 카페 타임을 즐기고 싶은 날",
        "keyword": "여유",
        "color": "#F8F1EA"
    },
    {
        "emoji": "🍑",
        "name": "복숭아 아이스티",
        "category": "TEA",
        "description": "달콤한 복숭아 향이 가득한 시원하고 산뜻한 음료.",
        "mood": "아무 생각 없이 편안하게 쉬고 싶은 날",
        "keyword": "편안함",
        "color": "#FFF1E8"
    },
    {
        "emoji": "🍫",
        "name": "초코 밀크",
        "category": "CHOCOLATE",
        "description": "진하고 달콤한 초콜릿으로 행복을 충전하는 한 잔.",
        "mood": "오늘은 확실하게 행복해지고 싶은 날",
        "keyword": "행복",
        "color": "#F7EEE9"
    },
    {
        "emoji": "🫐",
        "name": "블루베리 요거트",
        "category
