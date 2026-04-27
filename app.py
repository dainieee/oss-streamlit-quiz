import streamlit as st

st.set_page_config(
    page_title="Cinema Villain Test",
    page_icon="🎬",
    layout="centered"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Noto+Sans+KR:wght@300;400;500;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Noto Sans KR', sans-serif;
    background-color: #0a0a0a;
    color: #f0f0f0;
}

.stApp {
    background: #0a0a0a;
}

.block-container {
    max-width: 820px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

.poster-wrap {
    border: 1px solid #222222;
    background: #111111;
    padding: 2rem;
    border-radius: 14px;
    box-shadow: 0 0 0 1px rgba(139, 0, 0, 0.08);
}

.poster-kicker {
    color: #888888;
    letter-spacing: 0.18em;
    font-size: 0.78rem;
    margin-bottom: 0.7rem;
}

.poster-title {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 4rem;
    letter-spacing: 0.08em;
    line-height: 0.95;
    margin-bottom: 0.8rem;
    color: #f0f0f0;
    text-transform: uppercase;
}

.poster-sub {
    color: #888888;
    font-size: 1rem;
    font-style: italic;
    margin-bottom: 0.4rem;
}

.poster-meta {
    color: #888888;
    font-size: 0.92rem;
}

.section-title {
    font-family: 'Bebas Neue', sans-serif;
    letter-spacing: 0.08em;
    font-size: 1.6rem;
    color: #f0f0f0;
    margin: 1rem 0 0.9rem;
    text-transform: uppercase;
}

.question-text {
    font-size: 1.2rem;
    line-height: 1.7;
    color: #f0f0f0;
    font-weight: 500;
}

.result-card {
    border: 1px solid #2a2a2a;
    background: #161616;
    padding: 2rem;
    border-radius: 14px;
    box-shadow: 0 0 0 1px rgba(139, 0, 0, 0.08);
}

.result-name {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 2.8rem;
    letter-spacing: 0.05em;
    color: #f0f0f0;
    margin-bottom: 0.15rem;
    text-transform: uppercase;
}

.result-type {
    color: #8b0000;
    letter-spacing: 0.16em;
    font-size: 0.9rem;
    margin-bottom: 1.1rem;
    text-transform: uppercase;
}

.result-desc {
    font-size: 1rem;
    line-height: 1.9;
    color: #f0f0f0;
    margin-bottom: 1.2rem;
}

.keyword-box {
    margin: 1rem 0 1.2rem;
}

.keyword-tag {
    display: inline-block;
    border: 1px solid #8b0000;
    color: #f0f0f0;
    background: transparent;
    padding: 0.28rem 0.7rem;
    border-radius: 999px;
    font-size: 0.86rem;
    margin-right: 0.45rem;
    margin-bottom: 0.45rem;
}

.quote-box {
    border-top: 1px solid #2a2a2a;
    margin-top: 1rem;
    padding-top: 1rem;
}

.quote-line {
    font-style: italic;
    color: #f0f0f0;
    font-size: 1rem;
    margin-bottom: 0.35rem;
}

.quote-film {
    color: #9a9a9a;
    font-size: 0.92rem;
}

div.stButton > button {
    width: 100%;
    background: #8b0000;
    color: #f0f0f0;
    border: 1px solid #8b0000;
    border-radius: 10px;
    padding: 0.78rem 1rem;
    font-weight: 600;
}

div.stButton > button:hover {
    background: #a30000;
    border: 1px solid #a30000;
    color: #f0f0f0;
}

div[data-baseweb="input"] input {
    background-color: #111111 !important;
    color: #f0f0f0 !important;
    border: 1px solid #222222 !important;
}

div[data-baseweb="input"] input:focus {
    border: 1px solid #8b0000 !important;
    box-shadow: none !important;
}

.stTextInput label {
    color: #f0f0f0 !important;
    font-weight: 500;
}

div[role="radiogroup"] > label:hover {
    background-color: rgba(139, 0, 0, 0.08);
    border-radius: 8px;
}

div[role="radiogroup"] label,
div[role="radiogroup"] label p {
    color: #f0f0f0 !important;
    font-size: 1.05rem !important;
    font-weight: 400 !important;
    opacity: 1 !important;
}

[data-testid="stExpander"] {
    border: 1px solid #222222;
    border-radius: 12px;
    background: #0d0d0d;
}

.score-row {
    margin-bottom: 0.7rem;
}

.score-label {
    color: #f0f0f0;
    font-size: 0.95rem;
    margin-bottom: 0.2rem;
}

.score-bar-bg {
    width: 100%;
    height: 8px;
    background: #222222;
    border-radius: 999px;
    overflow: hidden;
}

.score-bar-fill {
    height: 8px;
    background: #8b0000;
    border-radius: 999px;
}

.small-note {
    color: #888888;
    font-size: 0.9rem;
    margin-top: 0.5rem;
}
</style>
""", unsafe_allow_html=True)

@st.cache_data
def load_results():
    return {
        "조커": {
            "type": "혼돈의 광대",
            "desc": "당신은 계획보다 순간을 즐기는 타입이에요. 규칙이 답답하고, 틀을 깨는 게 쾌감이 되죠. 세상이 당신을 이해 못 해도 괜찮아요. 그게 당신의 힘이니까요.",
            "quote": "Some men just want to watch the world burn.",
            "film": "다크나이트",
            "keywords": ["혼돈", "충동", "파격"]
        },
        "타노스": {
            "type": "냉혹한 이상주의자",
            "desc": "감정보다 논리, 개인보다 전체를 먼저 생각해요. 신념 하나로 끝까지 밀고 나가는 타입이죠. 냉혹해 보이지만 누구보다 진지하게 세상을 고민하는 사람이에요.",
            "quote": "I am inevitable.",
            "film": "어벤져스: 엔드게임",
            "keywords": ["신념", "질서", "냉정"]
        },
        "한니발 렉터": {
            "type": "우아한 지성파",
            "desc": "취향이 확고하고, 무례함을 가장 참지 못하는 타입이에요. 말 한마디에 무게가 있고, 항상 상황을 조용히 지배하죠.",
            "quote": "I'm having an old friend for dinner.",
            "film": "양들의 침묵",
            "keywords": ["지성", "품격", "통제"]
        },
        "금자씨": {
            "type": "우아한 복수의 화신",
            "desc": "겉은 차분하고 우아하지만 속엔 절대 꺼지지 않는 불씨가 있어요. 오래 기다릴 줄 알고, 때가 되면 흔들림 없이 실행하죠.",
            "quote": "착하게 살아요.",
            "film": "친절한 금자씨",
            "keywords": ["복수", "인내", "결단"]
        },
        "닥터 옥토퍼스": {
            "type": "집착하는 천재",
            "desc": "한 번 꽂히면 절대 못 놓는 타입이에요. 천재적인 두뇌와 집요한 실행력을 가졌지만, 그 집착이 스스로를 옥죄기도 해요.",
            "quote": "Intelligence is not a privilege, it's a gift.",
            "film": "스파이더맨 2",
            "keywords": ["집착", "천재성", "실행력"]
        },
        "패트릭 베이트먼": {
            "type": "겉멀쩡 속광기",
            "desc": "겉으로는 완벽해 보이지만, 내면엔 아무도 모르는 또 다른 자신이 있어요. 자존심이 강하고 통제 욕구도 강한 편이에요.",
            "quote": "I have to return some videotapes.",
            "film": "아메리칸 사이코",
            "keywords": ["허영", "통제", "이중성"]
        },
        "빌": {
            "type": "카리스마 지배자",
            "desc": "말 한마디, 눈빛 하나로 분위기를 바꾸는 타입이에요. 존재 자체가 하나의 권위이고, 이미 이긴 사람의 여유를 갖고 있어요.",
            "quote": "Now... I'm going to ask you questions.",
            "film": "킬 빌",
            "keywords": ["카리스마", "권위", "지배력"]
        },
        "베놈": {
            "type": "공생하는 야수",
            "desc": "평소엔 조용하지만 건드리면 걷잡을 수 없는 타입이에요. 내면이 복잡하고, 나름의 코드가 있는 악당이죠.",
            "quote": "We are Venom.",
            "film": "베놈",
            "keywords": ["본능", "양면성", "폭발력"]
        }
    }

@st.cache_data
def load_questions():
    return [
        {
            "q": "Q1. 나는 목표를 이룰 때 어떤 방식을 선호한다?",
            "options": [
                ("A) 치밀하게 계획을 세우고 단계별로 실행한다", ["닥터 옥토퍼스", "타노스"]),
                ("B) 즉흥적으로 상황을 즐기면서 간다", ["조커", "베놈"]),
                ("C) 아무도 눈치채지 못하게 조용히 해나간다", ["한니발 렉터", "금자씨"]),
                ("D) 기세 하나로 밀어붙인다", ["빌", "패트릭 베이트먼"]),
            ],
        },
        {
            "q": "Q2. 친구가 나를 배신했다. 나의 반응은?",
            "options": [
                ("A) 즉시 응징한다. 봐주는 건 없다", ["빌", "금자씨"]),
                ("B) 배신? 오히려 흥미롭다. 이용할 방법을 찾는다", ["한니발 렉터", "패트릭 베이트먼"]),
                ("C) 세상이 원래 그런 거지 뭐, 신경 안 쓴다", ["조커", "베놈"]),
                ("D) 이 세상 시스템 자체가 문제다", ["타노스", "닥터 옥토퍼스"]),
            ],
        },
        {
            "q": "Q3. 나의 패션 스타일은?",
            "options": [
                ("A) 올블랙, 심플하게 핏 하나로 승부한다", ["빌", "한니발 렉터"]),
                ("B) 화려하고 눈에 띄는 스타일이 좋다", ["조커", "금자씨"]),
                ("C) 항상 깔끔하게, 흠잡을 데 없이 차려입는다", ["패트릭 베이트먼", "타노스"]),
                ("D) 난 그런 거 신경 안 씀. 내가 입고 싶은 거 입는다", ["베놈", "닥터 옥토퍼스"]),
            ],
        },
        {
            "q": "Q4. 나에게 가장 중요한 가치는?",
            "options": [
                ("A) 신념과 철학 — 옳다고 믿으면 끝까지 간다", ["타노스", "닥터 옥토퍼스"]),
                ("B) 자유 — 아무도 날 가둬둘 수 없다", ["조커", "베놈"]),
                ("C) 복수 — 반드시 되갚아준다", ["금자씨", "빌"]),
                ("D) 완벽함 — 나는 최고여야 한다", ["패트릭 베이트먼", "한니발 렉터"]),
            ],
        },
        {
            "q": "Q5. 나의 약점은?",
            "options": [
                ("A) 집착이 너무 심하다", ["닥터 옥토퍼스", "금자씨"]),
                ("B) 충동적으로 행동할 때가 있다", ["조커", "베놈"]),
                ("C) 자존심이 너무 강하다", ["빌", "패트릭 베이트먼"]),
                ("D) 감정을 잘 드러내지 않는다", ["한니발 렉터", "타노스"]),
            ],
        },
        {
            "q": "Q6. 나는 혼자일 때 주로 뭘 하나?",
            "options": [
                ("A) 일정을 정리하며 다음 계획을 세운다", ["타노스", "닥터 옥토퍼스"]),
                ("B) 예술, 음악, 독서 등 취미를 즐긴다", ["한니발 렉터", "패트릭 베이트먼"]),
                ("C) 그냥 아무 생각 없이 하고 싶은 거 한다", ["조커", "베놈"]),
                ("D) 과거를 회상하며 동기를 다진다", ["금자씨", "빌"]),
            ],
        },
        {
            "q": "Q7. 누군가 나에게 대들면?",
            "options": [
                ("A) 미소 지으며 더 무섭게 응한다", ["한니발 렉터", "빌"]),
                ("B) 그 자리에서 바로 화를 낸다", ["베놈", "조커"]),
                ("C) 상대할 가치가 없으니 무시한다", ["타노스", "패트릭 베이트먼"]),
                ("D) 일단 넘어가지만 마음에 담아둔다", ["금자씨", "닥터 옥토퍼스"]),
            ],
        },
        {
            "q": "Q8. 내가 악당이 된 이유는?",
            "options": [
                ("A) 세상이 먼저 나를 버렸다", ["조커", "닥터 옥토퍼스"]),
                ("B) 더 큰 선을 위해서다", ["타노스"]),
                ("C) 당한 만큼 돌려줄 뿐이다", ["금자씨", "빌"]),
                ("D) 그냥... 이게 나니까", ["한니발 렉터", "패트릭 베이트먼", "베놈"]),
            ],
        },
        {
            "q": "Q9. 나의 리더십 스타일은?",
            "options": [
                ("A) 카리스마 있게 사람을 끌어당긴다", ["빌", "타노스"]),
                ("B) 두려움으로 복종하게 만든다", ["한니발 렉터", "패트릭 베이트먼"]),
                ("C) 리더? 난 혼자가 편하다", ["조커", "베놈"]),
                ("D) 치밀한 전략으로 조직을 움직인다", ["닥터 옥토퍼스", "금자씨"]),
            ],
        },
        {
            "q": "Q10. 마지막으로, 나의 최후는?",
            "options": [
                ("A) 끝까지 신념을 지키다 쓰러진다", ["타노스", "닥터 옥토퍼스"]),
                ("B) 웃으면서 모든 걸 즐긴다", ["조커", "베놈"]),
                ("C) 복수를 완성하고 조용히 사라진다", ["금자씨", "빌"]),
                ("D) 나는 절대 지지 않는다", ["한니발 렉터", "패트릭 베이트먼"]),
            ],
        },
    ]

RESULTS = load_results()
questions = load_questions()

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "current_q" not in st.session_state:
    st.session_state.current_q = 0
if "scores" not in st.session_state:
    st.session_state.scores = {name: 0 for name in RESULTS.keys()}

st.markdown("""
<div class="poster-wrap">
    <div class="poster-kicker">PSYCHOLOGICAL TEST</div>
    <div class="poster-title">CINEMA VILLAIN TEST</div>
    <div class="poster-sub">내가 스크린 속 악당이라면?</div>
    <div class="poster-meta">학번 2025404016 · 송다인</div>
</div>
""", unsafe_allow_html=True)

st.write("")

if not st.session_state.logged_in:
    st.markdown('<div class="section-title">로그인</div>', unsafe_allow_html=True)

    with st.form("login_form"):
        username = st.text_input("아이디")
        password = st.text_input("비밀번호", type="password")
        submitted = st.form_submit_button("입장하기")

    if submitted:
        if username == "dain" and password == "1234":
            st.session_state.logged_in = True
            st.rerun()
        else:
            st.error("아이디 또는 비밀번호가 올바르지 않습니다.")
else:
    if st.session_state.current_q < len(questions):
        current = st.session_state.current_q
        qdata = questions[current]

        st.markdown('<div class="section-title">질문</div>', unsafe_allow_html=True)
        st.progress((current + 1) / len(questions), text=f"{current + 1} / {len(questions)}")

        st.markdown(f"""
        <div class="poster-wrap" style="margin-top: 1rem;">
            <div class="poster-kicker">SCENE {current + 1}</div>
            <div class="question-text">{qdata["q"]}</div>
        </div>
        """, unsafe_allow_html=True)

        choice = st.radio(
            "선택지",
            [opt[0] for opt in qdata["options"]],
            label_visibility="collapsed",
            key=f"q_{current}"
        )

        if st.button("다음 문제"):
            for text, targets in qdata["options"]:
                if text == choice:
                    for t in targets:
                        st.session_state.scores[t] += 1
                    break

            st.session_state.current_q += 1
            st.rerun()

    else:
        result = max(st.session_state.scores, key=st.session_state.scores.get)
        info = RESULTS[result]
        keyword_html = "".join([f'<span class="keyword-tag">{k}</span>' for k in info["keywords"]])

        st.markdown('<div class="section-title">테스트 결과</div>', unsafe_allow_html=True)

        st.markdown(f"""
        <div class="result-card">
            <div class="poster-kicker">RESULT</div>
            <div class="result-name">{result}</div>
            <div class="result-type">{info["type"]}</div>
            <div class="result-desc">{info["desc"]}</div>
            <div class="keyword-box">{keyword_html}</div>
            <div class="quote-box">
                <div class="quote-line">"{info["quote"]}"</div>
                <div class="quote-film">— {info["film"]}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        with st.expander("점수 상세 보기"):
            max_score = max(st.session_state.scores.values()) if max(st.session_state.scores.values()) > 0 else 1
            for name, score in sorted(st.session_state.scores.items(), key=lambda x: x[1], reverse=True):
                width = int((score / max_score) * 100)
                st.markdown(f"""
                <div class="score-row">
                    <div class="score-label">{name} · {score}점</div>
                    <div class="score-bar-bg">
                        <div class="score-bar-fill" style="width:{width}%;"></div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
            st.markdown('<div class="small-note">각 문항의 선택에 따라 캐릭터 점수가 누적됩니다.</div>', unsafe_allow_html=True)

        if st.button("다시하기"):
            st.session_state.logged_in = False
            st.session_state.current_q = 0
            st.session_state.scores = {name: 0 for name in RESULTS.keys()}
            st.rerun()