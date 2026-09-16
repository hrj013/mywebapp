import streamlit as st

import streamlit as st

st.set_page_config(
    page_title="MBTI 여행처방 🌷",
    page_icon="🌷",
    layout="centered"
)

# -----------------------------
# 데이터
# -----------------------------
destinations = {
    "ISTJ": {
        "emoji": "🏛️",
        "place": "교토, 일본",
        "color": "#E8F5E9",
        "description": "차분하게 계획을 세우고 하나씩 둘러보는 여행",
        "reason": "정돈된 거리와 전통문화, 예측 가능한 동선이 잘 어울려요.",
        "tips": ["교토역 → 기요미즈데라 → 기온 코스", "아침 일찍 관광하기", "맛집은 미리 예약하기"],
    },
    "ISFJ": {
        "emoji": "🌷",
        "place": "파리, 프랑스",
        "color": "#FFF0F5",
        "description": "예쁜 풍경과 따뜻한 분위기를 천천히 즐기는 여행",
        "reason": "아기자기한 카페와 골목, 예술과 낭만을 편안하게 즐길 수 있어요.",
        "tips": ["동네 카페에서 여유 즐기기", "센강 산책하기", "작은 미술관 찾아보기"],
    },
    "INFJ": {
        "emoji": "🌙",
        "place": "아이슬란드",
        "color": "#E8F4FF",
        "description": "고요한 자연 속에서 생각과 감성을 충전하는 여행",
        "reason": "압도적인 자연 풍경과 한적한 분위기가 깊은 휴식을 선물해요.",
        "tips": ["골든서클 방문", "온천에서 쉬기", "밤에는 오로라 관측하기"],
    },
    "INTJ": {
        "emoji": "🔭",
        "place": "스위스",
        "color": "#EEF0FF",
        "description": "효율적인 일정으로 자연과 도시를 모두 정복하는 여행",
        "reason": "정확한 교통 시스템과 아름다운 자연을 체계적으로 즐길 수 있어요.",
        "tips": ["스위스패스 활용", "융프라우요흐 방문", "열차 시간 미리 체크"],
    },
    "ISTP": {
        "emoji": "🏄",
        "place": "제주도",
        "color": "#E6FAF5",
        "description": "정해진 계획보다는 발길 닿는 대로 즐기는 여행",
        "reason": "드라이브, 액티비티, 맛집 탐방까지 자유롭게 조합할 수 있어요.",
        "tips": ["렌터카로 해안도로 달리기", "서핑 도전하기", "즉흥 맛집 탐방"],
    },
    "ISFP": {
        "emoji": "🌿",
        "place": "다낭, 베트남",
        "color": "#F0FFF4",
        "description": "예쁜 풍경과 맛있는 음식으로 오감을 만족시키는 여행",
        "reason": "바다, 카페, 마사지, 맛있는 음식까지 느긋하게 즐기기 좋아요.",
        "tips": ["해변에서 일몰 보기", "로컬 카페 탐방", "마사지로 하루 마무리"],
    },
    "INFP": {
        "emoji": "🧚",
        "place": "포르투, 포르투갈",
        "color": "#FFF5E6",
        "description": "골목과 노을 속에서 나만의 이야기를 만드는 여행",
        "reason": "낭만적인 골목과 오래된 건물, 아름다운 노을이 감성을 자극해요.",
        "tips": ["도우루강 노을 감상", "골목 사진 찍기", "서점과 작은 카페 방문"],
    },
    "INTP": {
        "emoji": "🪐",
        "place": "런던, 영국",
        "color": "#F3F0FF",
        "description": "호기심 가득하게 도시 곳곳을 탐험하는 여행",
        "reason": "박물관, 과학, 역사, 독특한 서점 등 탐구할 거리가 정말 많아요.",
        "tips": ["자연사박물관 방문", "서점 투어", "동네별 테마를 정해 탐험"],
    },
    "ESTP": {
        "emoji": "🎢",
        "place": "방콕, 태국",
        "color": "#FFF1E6",
        "description": "먹고 놀고 돌아다니며 순간순간을 즐기는 여행",
        "reason": "활기찬 거리와 맛있는 음식, 다양한 액티비티가 기다리고 있어요.",
        "tips": ["야시장 탐방", "길거리 음식 먹기", "툭툭 타보기"],
    },
    "ESFP": {
        "emoji": "🍹",
        "place": "하와이, 미국",
        "color": "#E6F9FF",
        "description": "햇살 아래에서 신나게 놀고 예쁜 사진도 남기는 여행",
        "reason": "해변, 쇼핑, 액티비티, 맛집까지 즐거운 요소가 가득해요.",
        "tips": ["와이키키 해변", "스노클링", "선셋 사진 남기기"],
    },
    "ENFP": {
        "emoji": "🌈",
        "place": "바르셀로나, 스페인",
        "color": "#FFF0F6",
        "description": "새로운 사람과 장소를 만나며 즉흥적으로 즐기는 여행",
        "reason": "예술적인 건축물과 활기찬 거리, 맛있는 음식이 여행의 재미를 더해요.",
        "tips": ["가우디 건축 투어", "보케리아 시장", "골목길 즉흥 탐험"],
    },
    "ENTP": {
        "emoji": "🚀",
        "place": "뉴욕, 미국",
        "color": "#F0F4FF",
        "description": "새로운 자극과 재미있는 아이디어를 찾아 떠나는 여행",
        "reason": "문화, 음식, 예술, 사람까지 매 순간 새로운 것을 발견할 수 있어요.",
        "tips": ["브루클린 탐방", "전시회 찾아가기", "현지인 추천 장소 도전"],
    },
    "ESTJ": {
        "emoji": "🗺️",
        "place": "싱가포르",
        "color": "#EFFFF5",
        "description": "알찬 일정으로 핵심 명소를 빠르게 즐기는 여행",
        "reason": "교통이 편리하고 도시가 깔끔해 효율적으로 여행하기 좋아요.",
        "tips": ["마리나베이 방문", "가든스 바이 더 베이", "동선을 미리 정하기"],
    },
    "ESFJ": {
        "emoji": "💐",
        "place": "타이베이, 대만",
        "color": "#FFF8E8",
        "description": "맛있는 음식과 따뜻한 사람들을 만나는 여행",
        "reason": "맛집, 야시장, 카페가 풍부하고 비교적 편안하게 돌아다닐 수 있어요.",
        "tips": ["스린 야시장", "딤섬 먹기", "근교 온천 여행"],
    },
    "ENFJ": {
        "emoji": "💛",
        "place": "로마, 이탈리아",
        "color": "#FFF0E0",
        "description": "사람들과 추억을 만들며 역사와 문화를 즐기는 여행",
        "reason": "이야기가 가득한 유적과 광장, 맛있는 음식이 함께하는 여행이에요.",
        "tips": ["콜로세움 방문", "트레비 분수", "현지 레스토랑에서 식사"],
    },
    "ENTJ": {
        "emoji": "👑",
        "place": "두바이, UAE",
        "color": "#F2EEFF",
        "description": "화려한 도시에서 새로운 경험을 빠르게 흡수하는 여행",
        "reason": "현대적인 건축과 쇼핑, 미식, 다양한 체험을 한 번에 즐길 수 있어요.",
        "tips": ["부르즈 할리파", "사막 사파리", "두바이몰 탐방"],
    },
}

# -----------------------------
# CSS
# -----------------------------
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #FFF9FC 0%, #F3FAFF 100%);
    }

    .main-title {
        text-align: center;
        font-size: 42px;
        font-weight: 800;
        color: #FF6F91;
        margin-top: 20px;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        color: #777;
        font-size: 17px;
        margin-bottom: 30px;
    }

    .card {
        padding: 30px;
        border-radius: 28px;
        background: white;
        box-shadow: 0 8px 30px rgba(255, 111, 145, 0.12);
        text-align: center;
        margin-top: 25px;
    }

    .place {
        font-size: 34px;
        font-weight: 800;
        color: #444;
        margin: 8px 0;
    }

    .description {
        color: #777;
        font-size: 16px;
        margin-bottom: 20px;
    }

    .reason {
        background: #FFF5F8;
        border-radius: 18px;
        padding: 18px;
        color: #555;
        line-height: 1.6;
    }

    .tip {
        background: #F5FAFF;
        border-radius: 14px;
        padding: 12px;
        margin: 7px 0;
        color: #555;
    }

    .footer {
        text-align: center;
        color: #aaa;
        margin-top: 35px;
        font-size: 13px;
    }
</style>
""", unsafe_allow_html=True)

# -----------------------------
# 화면
# -----------------------------
st.markdown(
    '<div class="main-title">🌷 MBTI 여행처방</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">나의 MBTI에 딱 맞는 여행지를 찾아볼까요? ✈️</div>',
    unsafe_allow_html=True
)

mbti = st.selectbox(
    "💌 나의 MBTI를 골라주세요",
    ["MBTI를 선택해주세요"] + list(destinations.keys())
)

if mbti != "MBTI를 선택해주세요":
    data = destinations[mbti]

    st.markdown(
        f"""
        <div class="card" style="background:{data['color']}">
            <div style="font-size:65px;">{data['emoji']}</div>
            <div style="font-size:18px;color:#FF6F91;font-weight:700;">
                {mbti}에게 추천하는 여행지
            </div>
            <div class="place">{data['place']}</div>
            <div class="description">{data['description']}</div>
            <div class="reason">
                💡 <b>추천 이유</b><br>
                {data['reason']}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("### 🧳 여행 처방전")

    for tip in data["tips"]:
        st.markdown(
            f'<div class="tip">🌼 {tip}</div>',
            unsafe_allow_html=True
        )

    st.markdown(
        '<div class="footer">당신의 다음 여행이 조금 더 설레기를 💕</div>',
        unsafe_allow_html=True
    )
else:
    st.info("👆 위에서 MBTI를 선택하면 여행지가 나타나요!")
