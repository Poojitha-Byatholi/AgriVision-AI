import streamlit as st
import time
from chatbot.chatbot import get_response
from utils.language import t  # ✅ ADD THIS


# ==========================================================
# 🎨 STYLES (UNCHANGED)
# ==========================================================
st.markdown("""<style>
.status-container {
    display: flex;
    align-items: center;
    gap: 8px;
    margin-bottom: 5px;
}
.status-dot {
    height: 10px;
    width: 10px;
    background-color: #00ff88;
    border-radius: 50%;
    animation: pulse 1.5s infinite;
}
@keyframes pulse {
    0% { box-shadow: 0 0 0 0 rgba(0,255,136,0.7); }
    70% { box-shadow: 0 0 0 8px rgba(0,255,136,0); }
    100% { box-shadow: 0 0 0 0 rgba(0,255,136,0); }
}
.typing-cursor {
    font-weight: bold;
    animation: blink 1s infinite;
}
@keyframes blink {
    0% { opacity: 1; }
    50% { opacity: 0; }
    100% { opacity: 1; }
}
.suggestion-btn {
    background-color: #f0f2f6;
    border-radius: 20px;
    padding: 6px 14px;
    margin: 4px;
}
</style>""", unsafe_allow_html=True)


# ==========================================================
# ✨ TYPEWRITER EFFECT
# ==========================================================
def typewriter_effect(text):
    placeholder = st.empty()
    words = text.split(" ")
    typed = ""

    for word in words:
        typed += word + " "
        placeholder.markdown(
            typed + '<span class="typing-cursor">▍</span>',
            unsafe_allow_html=True
        )
        time.sleep(0.03)

    placeholder.markdown(typed)
    return typed.strip()


# ==========================================================
# 💡 SUGGESTIONS (MULTILINGUAL)
# ==========================================================
def get_suggestions(user_text, language):
    text = user_text.lower()

    if "tomato" in text:
        return [
            t(language, "suggest_tomato_fertilizer"),
            t(language, "suggest_tomato_season"),
            t(language, "suggest_tomato_prevention")
        ]

    if "rice" in text:
        return [
            t(language, "suggest_rice_fertilizer"),
            t(language, "suggest_rice_season"),
            t(language, "suggest_rice_prevention")
        ]

    if "wheat" in text:
        return [
            t(language, "suggest_wheat_fertilizer"),
            t(language, "suggest_wheat_season")
        ]

    if "scheme" in text or "pm kisan" in text:
        return [
            t(language, "suggest_insurance"),
            t(language, "suggest_soil_card")
        ]

    return [
        t(language, "suggest_general_prevention"),
        t(language, "suggest_maize_fertilizer"),
        t(language, "suggest_weather_cotton")
    ]


# ==========================================================
# 🚀 MAIN UI
# ==========================================================
def render_chatbot_ui(language, disease=None, confidence=None):

    if "status" not in st.session_state:
        st.session_state.status = t(language, "status_online")

    # HEADER
    st.markdown(f"### 🌿 {t(language, 'chatbot_title')}")

    if st.button(t(language, "back_button")):
        st.session_state.clear()
        st.session_state.show_chatbot = False
        st.rerun()

    # STATUS
    st.markdown(
        f"""
        <div class="status-container">
            <div class="status-dot"></div>
            <div><b>{st.session_state.status}</b></div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.caption(t(language, "chatbot_caption"))

    # INIT CHAT
    if "chat_messages" not in st.session_state:
        st.session_state.chat_messages = [
            {
                "role": "assistant",
                "content": t(language, "chatbot_welcome")
            }
        ]

    # DETECTION INFO
    if disease and confidence:
        st.info(f"{t(language,'detected_disease')}: {disease} ({int(confidence * 100)}%)")

    # CHAT HISTORY
    for msg in st.session_state.chat_messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # INPUT
    prompt = st.chat_input(t(language, "chat_input_placeholder"))

    if prompt:
        st.session_state.chat_messages.append({"role": "user", "content": prompt})

        with st.chat_message("user"):
            st.markdown(prompt)

        st.session_state.status = t(language, "status_thinking")
        st.rerun()

    # RESPONSE
    if st.session_state.status == t(language, "status_thinking"):

        last_user_message = st.session_state.chat_messages[-1]["content"]

        with st.chat_message("assistant"):

            typing_placeholder = st.empty()
            typing_placeholder.markdown(
                t(language, "typing_message") + ' <span class="typing-cursor">▍</span>',
                unsafe_allow_html=True
            )

            time.sleep(0.8)

            response = get_response(last_user_message)
            typing_placeholder.empty()
            
            if not response:
                response = t(language, "no_response_fallback")
                
            final_response = typewriter_effect(response)
                
        st.session_state.chat_messages.append({
            "role": "assistant",
            "content": final_response
        })

        st.session_state.status = t(language, "status_online")
        st.rerun()

    # SUGGESTIONS
    if st.session_state.chat_messages:
        last_user_text = st.session_state.chat_messages[-1]["content"]
        suggestions = get_suggestions(last_user_text, language)

        st.markdown(f"##### 💡 {t(language, 'suggested_questions')}")

        cols = st.columns(len(suggestions))

        for i, suggestion in enumerate(suggestions):
            if cols[i].button(suggestion):
                st.session_state.chat_messages.append({
                    "role": "user",
                    "content": suggestion
                })
                st.session_state.status = t(language, "status_thinking")
                st.rerun()