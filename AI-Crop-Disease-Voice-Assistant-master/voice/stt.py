import whisper
import streamlit as st


# --------------------------------------------------
# Load Whisper Model (Cached Properly)
# --------------------------------------------------

@st.cache_resource
def load_whisper_model():
    return whisper.load_model("tiny")


model = load_whisper_model()


# --------------------------------------------------
# Speech To Text (Optimized)
# --------------------------------------------------

def speech_to_text(audio_path: str) -> str:
    try:
        result = model.transcribe(
            audio_path,
            fp16=False,        # CPU safe
            temperature=0,     # Deterministic
            best_of=1,
            beam_size=1,
            language=None      # Auto detect
        )

        return result.get("text", "").strip()

    except Exception as e:
        print("STT Error:", e)
        return ""
