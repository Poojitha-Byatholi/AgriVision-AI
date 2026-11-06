import os
import re
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# --------------------------------------------------
# SANITIZER
# --------------------------------------------------

def sanitize_response(text, output_language):
    if not text:
        return None

    dosage_pattern = r"\b\d+\s?(ml|l|litre|liter|kg|g|grams|%)\b"

    if re.search(dosage_pattern, text.lower()):
        if output_language == "Hindi":
            warning = "\n\n⚠ कृपया रासायनिक उपचार से पहले कृषि विशेषज्ञ से सलाह लें।"
        elif output_language == "Telugu":
            warning = "\n\n⚠ రసాయన చికిత్సకు ముందు స్థానిక వ్యవసాయ నిపుణుడిని సంప్రదించండి."
        else:
            warning = "\n\n⚠ Consult expert before chemical use."

        text += warning

    return text


# --------------------------------------------------
# LLM CALL
# --------------------------------------------------

def call_llm(messages, max_tokens, temperature=0.3):
    return client.chat.completions.create(
        model="llama-3.1-8b-instant",
        temperature=temperature,
        max_tokens=max_tokens,
        messages=messages
    )


# --------------------------------------------------
# BULLET VALIDATOR
# --------------------------------------------------

def validate_bullets(text):
    bullets = [l for l in text.split("\n") if l.strip().startswith("-")]
    return len(bullets) >= 2


# --------------------------------------------------
# MAIN LLM RESPONSE
# --------------------------------------------------

def generate_llm_response(
    disease,
    confidence,
    user_query,
    response_mode="short",
    output_language="English"
):

    # ✅ FIX: Normalize language here (CORRECT PLACE)
    output_language = output_language.capitalize()

    # ⭐ TOKEN ALLOCATION
    if output_language == "Telugu":
        max_tokens = 1000
    elif output_language == "Hindi":
        max_tokens = 900
    else:
        max_tokens = 450

    system_prompt = f"""
You are a professional agricultural advisory assistant.

RULES:
- Only agriculture queries allowed.
- Do NOT invent pesticide brand names.
- Do NOT provide chemical dosage.
- Respond ONLY in {output_language}.
- Do NOT mix languages.

STRUCTURE:
- Provide EXACTLY 2 bullet recommendations.
- Each bullet must start with '-' on new line.
- Maximum 12 words per bullet.
- Never merge bullets.
- No headings or sections.
- Keep advice practical and concise.
"""

    if disease and confidence:
        user_prompt = f"""
Predicted Disease: {disease}
Prediction Confidence: {int(confidence * 100)}%

Farmer Question: {user_query}
"""
    else:
        user_prompt = f"Farmer Question: {user_query}"

    try:
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]

        response = call_llm(messages, max_tokens)

        finish_reason = response.choices[0].finish_reason
        raw_text = response.choices[0].message.content.strip()

        print("Finish reason:", finish_reason)

        if finish_reason == "length":
            continuation = call_llm(
                messages + [
                    {"role": "assistant", "content": raw_text},
                    {"role": "user", "content": "Continue and complete remaining bullet."}
                ],
                200
            )

            raw_text += "\n" + continuation.choices[0].message.content.strip()

        if not validate_bullets(raw_text):
            repair_prompt = system_prompt + "\nRewrite ensuring EXACTLY 2 bullets."

            repair = call_llm(
                [
                    {"role": "system", "content": repair_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                250
            )

            raw_text = repair.choices[0].message.content.strip()

        return sanitize_response(raw_text, output_language)

    except Exception as e:
        print("Groq API Error:", e)
        return None


# --------------------------------------------------
# DISEASE ENRICHMENT
# --------------------------------------------------

def generate_disease_enrichment(disease, crop_name, output_language="English"):

    # ✅ FIX: Normalize language here (CORRECT PLACE)
    output_language = output_language.capitalize()

    if output_language == "Telugu":
        max_tokens = 1000
    elif output_language == "Hindi":
        max_tokens = 900
    else:
        max_tokens = 450

    system_prompt = f"""
You are a senior agricultural advisory expert.

RULES:
- Supplementary insight only.
- Do NOT repeat remedies.
- Do NOT provide dosage.
- Respond ONLY in {output_language}.
- EXACTLY 2 bullets per section.
- Maximum 12 words per bullet.
"""

    user_prompt = f"Crop: {crop_name}\nDisease: {disease}"

    try:
        response = call_llm(
            [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            max_tokens,
            temperature=0.2
        )

        raw_text = response.choices[0].message.content.strip()
        return sanitize_response(raw_text, output_language)

    except Exception as e:
        print("Groq Enrichment Error:", e)
        return None