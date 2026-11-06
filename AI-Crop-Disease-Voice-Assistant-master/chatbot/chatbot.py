import os
import json

from chatbot.tfidf_engine import CropTFIDFEngine
from .language_utils import detect_language, translate_to_english
from .llm_engine import generate_llm_response


# --------------------------------------------------
# PATH CONFIGURATION
# --------------------------------------------------

BASE_DIR = os.path.dirname(__file__)
KNOWLEDGE_DIR = os.path.join(BASE_DIR, "knowledge")

tfidf_engine = CropTFIDFEngine(knowledge_dir="knowledge")


# --------------------------------------------------
# JSON LOADER
# --------------------------------------------------

def load_json(filename):
    filepath = os.path.join(KNOWLEDGE_DIR, filename)
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)


# --------------------------------------------------
# LANGUAGE HELPER
# --------------------------------------------------

def get_language_key(lang_code):
    if lang_code == "te":
        return "Telugu"
    elif lang_code == "hi":
        return "Hindi"
    return "English"


# --------------------------------------------------
# DISCLAIMER APPENDER
# --------------------------------------------------

def append_disclaimer(response, disclaimer_data, lang_key):
    try:
        disclaimer_text = disclaimer_data.get("general_disclaimer", {}).get(lang_key, "")
        if disclaimer_text:
            return response + "\n\n⚠ Disclaimer:\n" + disclaimer_text
        return response
    except Exception:
        return response


# --------------------------------------------------
# MAIN CHATBOT LOGIC
# --------------------------------------------------

def get_response(user_text: str, disease_context=None, confidence=None):

    # -------------------------
    # Detect Language
    # -------------------------
    user_lang = detect_language(user_text)
    lang_key = get_language_key(user_lang)

    if user_lang != "en":
        processed_text = translate_to_english(user_text).lower().strip()
    else:
        processed_text = user_text.lower().strip()

    # -------------------------
    # Load Knowledge Files
    # -------------------------
    diseases_data = load_json("diseases.json")
    fertilizers_data = load_json("fertilizers.json")
    preventions_data = load_json("prevention.json")
    schemes_data = load_json("schemes.json")
    seasonal_data = load_json("seasonal.json")
    soil_data = load_json("soil.json")
    weather_data = load_json("weather.json")
    disclaimer_data = load_json("disclaimer.json")

    # ==========================================================
    # 1️⃣ DISEASE HANDLING
    # ==========================================================
    for key, info in diseases_data.items():

        if key == "__FALLBACK__":
            continue

        parts = key.split("___")
        if len(parts) != 2:
            continue

        crop_key = parts[0].lower()
        disease_key = parts[1].replace("_", " ").lower()
        crop_name = info["crop"]["English"].lower()

        if (
            disease_key in processed_text
            and (crop_name in processed_text or crop_key in processed_text)
        ) or disease_key in processed_text:

            symptoms = info["symptoms"][lang_key]
            advice = info["general_advice"][lang_key]
            note = info["note"][lang_key]

            response = f"🌿 Disease: {disease_key.title()}\n\n"

            response += "🩺 Symptoms:\n"
            for s in symptoms:
                response += f"- {s}\n"

            response += "\n📋 General Advice:\n"
            for a in advice:
                response += f"- {a}\n"

            response += f"\nℹ Note:\n{note}"

            return append_disclaimer("SOURCE: JSON\n\n" + response, disclaimer_data, lang_key)

    # ==========================================================
    # 2️⃣ FERTILIZER HANDLING
    # ==========================================================
    for crop, crop_data in fertilizers_data.items():

        if crop.lower() in processed_text and any(
            word in processed_text for word in ["fertilizer", "manure", "nutrient", "npk"]
        ):

            response = f"🌱 Fertilizer Advisory for {crop}\n\n"

            for stage, details in crop_data.items():

                response += f"{stage.replace('_',' ').title()}:\n"

                fertilizers = details["recommended_fertilizers"][lang_key]
                purpose = details["purpose"][lang_key]
                advice = details["advice"][lang_key]

                response += "Recommended:\n"
                for f in fertilizers:
                    response += f"- {f}\n"

                response += f"\nPurpose:\n{purpose}\n"
                response += f"\nAdvice:\n{advice}\n\n"

            return append_disclaimer(response, disclaimer_data, lang_key)

    # ==========================================================
    # 3️⃣ SOIL HANDLING
    # ==========================================================
    for soil_type, soil_info in soil_data.items():

        soil_match = soil_type.lower().replace("_", " ")

        if soil_match in processed_text:

            response = f"🌍 Soil Type: {soil_type.replace('_',' ')}\n\n"

            if "characteristics" in soil_info:
                for c in soil_info["characteristics"][lang_key]:
                    response += f"- {c}\n"

            if "general_advice" in soil_info:
                response += "\nAdvice:\n"
                for a in soil_info["general_advice"][lang_key]:
                    response += f"- {a}\n"

            if "note" in soil_info:
                response += f"\nℹ Note:\n{soil_info['note'][lang_key]}"

            return append_disclaimer(response, disclaimer_data, lang_key)

    # ==========================================================
    # 4️⃣ PREVENTION HANDLING
    # ==========================================================
    if "prevent" in processed_text:

        practices = preventions_data["general_prevention"]["preventive_practices"][lang_key]
        note = preventions_data["general_prevention"]["note"][lang_key]

        response = "🛡 General Prevention Practices\n\n"

        for p in practices:
            response += f"- {p}\n"

        response += f"\nℹ Note:\n{note}"

        return append_disclaimer(response, disclaimer_data, lang_key)

    # ==========================================================
    # 5️⃣ SCHEMES HANDLING
    # ==========================================================
    for scheme_key, scheme_info in schemes_data.items():

        if scheme_key == "__FALLBACK__":
            continue

        if scheme_key.lower().replace("_", " ") in processed_text:

            name = scheme_info["scheme_name"][lang_key]
            desc = scheme_info["description"][lang_key]
            benefits = scheme_info["benefits"][lang_key]
            note = scheme_info["note"][lang_key]

            response = f"🏛 {name}\n\n{desc}\n\nBenefits:\n"

            for b in benefits:
                response += f"- {b}\n"

            response += f"\nℹ Note:\n{note}"

            return append_disclaimer(response, disclaimer_data, lang_key)

    # ==========================================================
    # 6️⃣ SEASONAL HANDLING
    # ==========================================================
    for crop, crop_data in seasonal_data.items():

        if crop.lower() in processed_text:

            response = f"🌾 Seasonal Advisory for {crop}\n\n"

            for key, value in crop_data.items():

                if isinstance(value, dict) and "sowing_period" in value:

                    response += f"Sowing: {value['sowing_period'][lang_key]}\n"
                    response += f"Harvest: {value['harvest_period'][lang_key]}\n\n"

                    for a in value["general_advice"][lang_key]:
                        response += f"- {a}\n"

            return append_disclaimer(response, disclaimer_data, lang_key)

    # ==========================================================
    # 7️⃣ WEATHER HANDLING
    # ==========================================================
    for crop, crop_data in weather_data.items():

        if crop in processed_text:

            for condition, details in crop_data.items():

                condition_name = condition.replace("_", " ")

                if condition_name in processed_text:

                    impacts = details["possible_impacts"][lang_key]
                    advice = details["general_advice"][lang_key]

                    response = f"🌦 Weather Advisory for {crop.title()}\n\nPossible Impacts:\n"

                    for i in impacts:
                        response += f"- {i}\n"

                    response += "\nAdvice:\n"
                    for a in advice:
                        response += f"- {a}\n"

                    return append_disclaimer(response, disclaimer_data, lang_key)

    # ==========================================================
    # 8️⃣ TF-IDF FALLBACK (FIXED)
    # ==========================================================
    result = tfidf_engine.get_answer(processed_text)

    answer, score = result

    if answer and score > 0.30:
        return append_disclaimer("SOURCE: TFIDF\n\n" + answer, disclaimer_data, lang_key)

    # ==========================================================
    # 9️⃣ GROQ LLM FALLBACK (FIXED)
    # ==========================================================
    low_confidence = confidence is not None and confidence < 0.75

    if low_confidence or not answer:

        llm_answer = generate_llm_response(
            disease_context,
            confidence,
            user_text,
            response_mode="short",
            output_language=lang_key
        )

        if llm_answer:
            return append_disclaimer("SOURCE: LLM\n\n" + llm_answer, disclaimer_data, lang_key)

    # ==========================================================
    # FINAL SAFE FALLBACK
    # ==========================================================
    fallback_message = diseases_data["__FALLBACK__"]["message"][lang_key]
    return append_disclaimer(fallback_message, disclaimer_data, lang_key)