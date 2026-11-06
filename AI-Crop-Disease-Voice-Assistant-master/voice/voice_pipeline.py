from chatbot.chatbot import get_response
from voice.stt import speech_to_text
from utils.language import t


def process_voice(audio_input, language):
    """
    Process voice input:
    STT → Chatbot → Safe multilingual response
    """

    # -----------------------------
    # Speech to Text
    # -----------------------------
    spoken_text = speech_to_text(audio_input)

    # ❌ If speech not understood
    if not spoken_text:
        return "", t(language, "voice_not_understood")

    # Clean text
    spoken_text = spoken_text.strip()

    # -----------------------------
    # Chatbot Response
    # -----------------------------
    response_text = get_response(spoken_text)

    # ❌ If chatbot fails / returns None
    if not response_text:
        response_text = t(language, "no_response_fallback")

    # -----------------------------
    # Return result
    # -----------------------------
    return spoken_text, response_text