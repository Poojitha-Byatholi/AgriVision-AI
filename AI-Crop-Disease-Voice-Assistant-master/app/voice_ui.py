import streamlit as st
import tempfile
import time
from streamlit_mic_recorder import mic_recorder
from voice.stt import speech_to_text
from voice.tts import text_to_speech
from chatbot.chatbot import get_response
from utils.language import t   # ✅ ADD THIS


def render_voice_ui(language, disease=None, confidence=None):

    # -----------------------------
    # Styling
    # -----------------------------
    st.markdown("""
    <style>
    .status-text {
        margin-top: 15px;
        font-size: 15px;
        font-weight: 500;
        color: #2563eb;
    }

    .fade-message {
        margin-top: 15px;
        padding: 12px 16px;
        border-radius: 8px;
        background-color: #fef2f2;
        color: #b91c1c;
        font-size: 14px;
        font-weight: 500;
        animation: fadeOut 3s forwards;
    }

    @keyframes fadeOut {
        0% { opacity: 1; }
        80% { opacity: 1; }
        100% { opacity: 0; }
    }
    </style>
    """, unsafe_allow_html=True)

    # =========================
    # HEADER
    # =========================
    st.title(f"🎙 {t(language, 'voice_title')}")

    if st.button(t(language, "back_button")):
        st.session_state.show_voice = False
        st.rerun()

    st.markdown(f"### {t(language, 'voice_instruction')}")

    # -----------------------------
    # Mic Recorder
    # -----------------------------
    audio = mic_recorder(
        start_prompt=t(language, "mic_start"),
        stop_prompt=t(language, "mic_stop"),
        key="mic_recorder"
    )

    if audio is None:
        return

    # -----------------------------
    # Processing Indicator
    # -----------------------------
    status_placeholder = st.empty()
    status_placeholder.markdown(
        f'<div class="status-text">{t(language, "processing_message")}</div>',
        unsafe_allow_html=True
    )

    audio_bytes = audio["bytes"]

    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
        tmp.write(audio_bytes)
        temp_path = tmp.name

    spoken_text = speech_to_text(temp_path)

    # ❌ STT FAIL
    if not spoken_text:
        status_placeholder.empty()
        st.markdown(
            f'<div class="fade-message">⚠ {t(language, "voice_not_understood")}</div>',
            unsafe_allow_html=True
        )
        time.sleep(3)
        st.session_state["mic_recorder"] = None
        st.rerun()

    # -----------------------------
    # CHATBOT RESPONSE
    # -----------------------------
    response_text = get_response(spoken_text)

    # ✅ SAFE FIX
    if not response_text:
        response_text = t(language, "no_response_fallback")

    audio_file = text_to_speech(response_text)

    status_placeholder.empty()

    st.audio(audio_file, autoplay=True)

    st.markdown("---")
    st.markdown(f"🗣 **{t(language,'you_label')}:** {spoken_text}")
    st.markdown(f"🤖 **{t(language,'assistant_label')}:** {response_text}")