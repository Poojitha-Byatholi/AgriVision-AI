def analyze_weather_risk(weather: dict, crop: str | None = None) -> list[str]:
    """
    Analyze weather conditions and return advisory KEYS (not raw text).
    """

    advisories = []

    temperature = weather.get("temperature")
    humidity = weather.get("humidity")
    rainfall = weather.get("rainfall")

    # ---- General disease risk ----
    if humidity is not None and humidity >= 80:
        advisories.append("humidity_risk")

    if rainfall == "high":
        advisories.append("heavy_rainfall")

    # ---- Heat stress ----
    if temperature is not None and temperature >= 35:
        advisories.append("heat_stress")

    # ---- Crop-specific rules ----
    if crop == "wheat" and humidity and humidity > 75:
        advisories.append("wheat_rust_risk")

    if crop == "rice" and rainfall == "high":
        advisories.append("rice_lodging_risk")

    # ---- Default condition ----
    if not advisories:
        advisories.append("favorable_weather")

    return advisories


# --------------------------------------------------
# UPDATED: Multilingual-friendly severity
# --------------------------------------------------

def calculate_weather_severity(weather: dict) -> str:
    temperature = weather.get("temperature")
    humidity = weather.get("humidity")
    rainfall = weather.get("rainfall")

    severity_score = 0

    if temperature is not None:
        if temperature >= 38:
            severity_score += 2
        elif temperature >= 34:
            severity_score += 1

    if humidity is not None:
        if humidity >= 85:
            severity_score += 2
        elif humidity >= 75:
            severity_score += 1

    if rainfall == "high":
        severity_score += 2

    if severity_score >= 4:
        return "high_risk"
    elif severity_score >= 2:
        return "moderate_risk"
    else:
        return "low_risk"