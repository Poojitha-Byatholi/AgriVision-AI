def detect_intent(text: str) -> str:
    """
    Detect intent using strict priority-based keyword matching.
    Text is expected to be in English.
    """
    text = text.lower()

    # ---------- PREVENTION (HIGHEST PRIORITY) ----------
    prevention_keywords = [
        "prevent", "prevention", "avoid",
        "control", "management", "protect",
        "protection", "safety"
    ]

    # ---------- SCHEME ----------
    scheme_keywords = [
        "scheme", "yojana", "government", "subsidy",
        "pm kisan", "kisan", "insurance", "bima",
        "soil health card", "soil card", "card"
    ]

    # ---------- SEASONAL ----------
    seasonal_keywords = [
        "season", "sow", "sowing", "plant", "planting",
        "harvest", "harvesting", "month", "time",
        "kharif", "rabi", "zaid", "best time"
    ]

    # ---------- DISEASE ----------
    disease_keywords = [
        "disease", "spot", "spots", "blight",
        "rust", "wilt", "virus", "patches",
        "leaf problem"
    ]

    # ---------- FERTILIZER ----------
    fertilizer_keywords = [
        "fertilizer", "urea", "dap", "npk",
        "nutrient", "manure"
    ]

    # ---------- SOIL ----------
    soil_keywords = [
        "soil", "ph", "deficiency",
        "nutrient deficiency", "black soil", "red soil"
    ]

    # ---------- WEATHER ----------
    weather_keywords = [
        "weather", "rain", "rainfall", "temperature",
        "humidity", "heat", "cold", "climate",
        "forecast", "frost"
    ]

    # ---------- PRIORITY ORDER ----------
    if any(word in text for word in prevention_keywords):
        return "PREVENTION"

    if any(word in text for word in scheme_keywords):
        return "SCHEME"

    if any(word in text for word in seasonal_keywords):
        return "SEASONAL"

    if any(word in text for word in disease_keywords):
        return "DISEASE"

    if any(word in text for word in fertilizer_keywords):
        return "FERTILIZER"

    if any(word in text for word in soil_keywords):
        return "SOIL"

    if any(word in text for word in weather_keywords):
        return "WEATHER"

    return "UNKNOWN"
