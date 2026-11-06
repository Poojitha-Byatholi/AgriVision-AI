from gtts import gTTS
import tempfile


def text_to_speech(text, language="en"):

    # ✅ Safety check
    if not text:
        return None

    try:
        # ✅ Map your system language → gTTS codes
        lang_map = {
            "English": "en",
            "Hindi": "hi",
            "Telugu": "te"
        }

        lang_code = lang_map.get(language, "en")

        tts = gTTS(text=text, lang=lang_code)

        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
        tts.save(temp_file.name)

        return temp_file.name

    except Exception as e:
        print("TTS Error:", e)
        return None