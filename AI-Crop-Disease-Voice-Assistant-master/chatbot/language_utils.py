from langdetect import detect


def detect_language(text: str) -> str:
    try:
        lang = detect(text)

        if lang.startswith("hi"):
            return "hi"
        elif lang.startswith("te"):
            return "te"
        else:
            return "en"

    except Exception:
        return "en"


def translate_to_english(text: str) -> str:
    # No external translation needed anymore
    return text


def translate_from_english(text: str, target_lang: str) -> str:
    # No reverse translation needed
    return text
