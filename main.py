import streamlit as st
from datetime import date

# ---------------------------------------
# 페이지 설정
# ---------------------------------------
st.set_page_config(
    page_title="오늘 뭐 마실까?",
    page_icon="🧋",
    layout="centered"
)

# ---------------------------------------
# 30가지 음료
# ---------------------------------------
drinks = [
    ("🍓", "딸기 라떼", "달콤하고 부드러운 딸기 한 잔", "달콤함"),
    ("🧋", "흑당 버블티", "쫀득한 펄과 진한 흑당의 조합", "즐거움"),
    ("🍵", "말차 라떼", "쌉싸름하고 부드러운 말차의 매력", "차분함"),
    ("🍋", "레몬 에이드", "톡 쏘는 상큼함으로 기분 전환", "상큼함"),
    ("☕", "바닐라 라떼", "은은한 바닐라 향이 가득한 커피", "여유"),
    ("🍑", "복숭아 아이스티", "달콤하고 시원한 복숭아의 맛", "편안함"),
    ("🍫", "초코 밀크", "진하고 달콤한 초콜릿 음료", "행복"),
    ("🫐", "블루베리 요거트", "상큼하고 부드러운 요거트 음료", "산뜻함"),
    ("🍊", "자몽 에이드", "쌉싸름하고 상큼한 자몽 에이드", "새로움"),
    ("🥥", "코코넛 스무디", "시원하고 부드러운 코코넛 스무디", "휴식"),
    ("🫖", "얼그레이 밀크티", "향긋한 얼그레이와 부드러운 우유", "우아함"),
    ("🥭", "망고 스무디", "달콤한 망고가 가득한 스무디", "활력"),
    ("🍎", "애플 시나몬 티", "사과와 시나몬의 포근한 향", "포근함"),
    ("🧊", "아이스 아메리카노", "깔끔하고 시원한 클래식 커피", "집중"),
    ("🍯", "허니 자몽티", "상큼한 자몽과 달콤한 꿀", "균형"),
    ("🍇", "청포도 에이드", "청량하고 산뜻한 청포도 음료", "청량함"),
    ("🌹", "로즈 티", "은은한 장미 향이 매력적인 티", "로맨틱"),
    ("🍌", "바나나 우유", "달콤하고 부드러운 추억의 맛", "편안함"),
    ("🍓", "딸기 요거트 스무디", "딸기와 요거트의 상큼달콤한 조합", "상큼달콤"),
    ("🌿", "자스민 그린티", "은은한 꽃 향기가 느껴지는 녹차", "힐링"),
    ("🍯", "허니 밀크티", "부드러운 밀크티와 달콤한 꿀", "따뜻함"),
    ("🍉", "수박 주스", "시원하고 달콤한 수박 주스", "시원함"),
    ("🍍", "파인애플 에이드", "상큼하고 톡 쏘는 파인애플 음료", "활기"),
    ("🥛", "딸기 초코 우유", "딸기와 초콜릿의 달콤한 만남", "달달함"),
    ("🌼", "캐모마일 티", "은은하고 편안한 향의 허브티", "안정"),
    ("🍒", "체리 에이드", "새콤달콤하고 예쁜 체리 에이드", "사랑스러움"),
    ("🥝", "키위 주스", "톡톡 튀는 상큼한 키위 주스", "상쾌함"),
    ("🍮", "카라멜 마키아토", "진한 커피와 달콤한 카라멜", "달콤한 사치"),
    ("🥤", "콜드브루", "부드럽고 깔끔한 시원한 커피", "깔끔함"),
    ("🌸", "벚꽃 라떼", "핑크빛으로 특별한 분위기의 라떼", "설렘"),
]

# ---------------------------------------
# 기본 CSS
# ---------------------------------------
st.markdown("""
<style>
.stApp {
    background-color: #fffafd;
}

.block-container {
    max-width: 680px;
    padding-top: 40px;
}

.title {
    text-align: center;
    font-size: 42px;
    font-weight: 800;
    color: #222222;
}

.title span {
    color: #ff6f91;
}

.subtitle {
    text-align: center;
    color: #888888;
    font-size: 15px;
    line-height: 1.7;
    margin-bottom: 30px;
}

.card {
    background-color: #ffffff;
    border-radius: 25px;
    padding: 30px;
    text-align: center;
    border: 1px solid #eeeeee;
    box-shadow: 0 8px 25px rgba(0, 0, 0, 0.06);
}

.drink-emoji {
    font-size: 75px;
}

.drink-name {
    font-size: 36px;
    font-weight: 800;
    color: #222222;
    margin: 10px 0;
}

.drink-description {
    color: #666666;
    font-size: 15px;
    margin-bottom: 20px;
}

.keyword {
    display: inline-block;
    background-color: #fff0f5;
    color: #ff6f91;
    border-radius: 20px;
    padding: 8px 16px;
    font-weight: 700;
}

.footer {
    text-align: center;
    color: #aaaaaa;
    font-size: 12px;
    margin-top: 35px;
}
</style>
""", unsafe_allow_html=True)

# ---------------------------------------
# 제목
# ---------------------------------------
st.markdown(
    """
    <div class="title">
        오늘은 <span>뭐 마실까?</span> 🧋
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="subtitle">
        생일을 알려주면<br>
        30가지 음료 중 당신에게 어울리는 한 잔을 찾아드려요 ✨
    </div>
    """,
    unsafe_allow_html=True
)

# ---------------------------------------
# 생일 입력
# ---------------------------------------
st.subheader("🎂 생일을 알려주세요")

birthday = st.date_input(
    "생년월일",
    value=date(2000, 1, 1),
    min_value=date(1920, 1, 1),
    max_value=date.today()
)

# ---------------------------------------
# 추천 버튼
# ---------------------------------------
st.write("")

recommend = st.button(
    "✨ 나의 음료 찾기",
    use_container_width=True
)

# ---------------------------------------
# 추천 결과
# ---------------------------------------
if recommend:

    # 생년월일을 숫자로 변환
    birthday_number = (
        birthday.year * 10000
        + birthday.month * 100
        + birthday.day
    )

    # 0 ~ 29 중 하나 선택
    drink_number = birthday_number % 30

    st.session_state["drink_number"] = drink_number

# ---------------------------------------
# 결과 출력
# ---------------------------------------
if "drink_number" in st.session_state:

    number = st.session_state["drink_number"]

    emoji, name, description, keyword = drinks[number]

    st.write("")

    st.markdown(
        f"""
        <div class="card">

            <div class="drink-emoji">
                {emoji}
            </div>

            <div style="
                color:#999999;
                font-size:12px;
                font-weight:700;
                letter-spacing:2px;
            ">
                TODAY'S DRINK
            </div>

            <div class="drink-name">
                {name}
            </div>

            <div class="drink-description">
                {description}
            </div>

            <div class="keyword">
                ✨ 오늘의 키워드 · {keyword}
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    # 다른 음료 보기
    if st.button(
        "🔄 다른 음료 보기",
        use_container_width=True
    ):

        next_number = (number + 1) % 30
        st.session_state["drink_number"] = next_number

        # rerun 없이도 버튼 클릭 후 아래 결과가 다시 계산되도록
        st.rerun()

else:

    st.info(
        "🎀 생일을 입력하고 '나의 음료 찾기' 버튼을 눌러주세요!"
    )

# ---------------------------------------
# Footer
# ---------------------------------------
st.markdown(
    """
    <div class="footer">
        🧋 오늘도 맛있는 하루 보내세요 ✨
    </div>
    """,
    unsafe_allow_html=True
)
