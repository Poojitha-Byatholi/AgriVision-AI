import datetime
import streamlit as st
import time
import sys
import os
import json
import numpy as np
from PIL import Image
import tensorflow as tf

# --------------------------------------------------
# Path Fix  ← MUST COME BEFORE CUSTOM IMPORTS
# --------------------------------------------------
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(BASE_DIR)

# --------------------------------------------------
# Custom Imports
# --------------------------------------------------
from utils.image_utils import get_image_hash
from utils.language import t, LANG
from chatbot_ui import render_chatbot_ui
from utils.camera import capture_leaf_image
from utils.disease_translations import DISEASE_TRANSLATIONS
from datetime import datetime
from chatbot.llm_engine import generate_disease_enrichment
from weather.weather_rules import analyze_weather_risk, calculate_weather_severity
from weather.weather_service import get_weather_data

from dotenv import load_dotenv
load_dotenv()
WEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")

# --------------------------------------------------
# Page Configuration (UNCHANGED UI)
# --------------------------------------------------
st.set_page_config(
    page_title="AgriVision AI",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --------------------------------------------------
# Session State (UNCHANGED UI)
# --------------------------------------------------
st.session_state.setdefault("loaded", False)
st.session_state.setdefault("prediction_done", False)
st.session_state.setdefault("image", None)
st.session_state.setdefault("last_image_hash", None)
st.session_state.setdefault("input_mode", None)  
st.session_state.setdefault("image_source", None) 
st.session_state.setdefault("show_chatbot", False)
st.session_state.setdefault("show_voice", False)
st.session_state.setdefault("extended_insights", {})

# --------------------------------------------------
# Global Language Reference
# --------------------------------------------------
if "language" not in st.session_state:
    st.session_state.language = "English"

language = st.session_state.language

# --------------------------------------------------
# Load Model (REAL LOGIC)
# --------------------------------------------------
MODEL_PATH = os.path.join(BASE_DIR, "models", "mobilenet_crop_disease.h5")
CLASS_PATH = os.path.join(BASE_DIR, "results", "class_indices.json")

@st.cache_resource
def load_model_and_labels():
    model = tf.keras.models.load_model(MODEL_PATH)
    with open(CLASS_PATH, "r", encoding="utf-8") as f:
        class_indices = json.load(f)
    return model, {v: k for k, v in class_indices.items()}

model, idx_to_class = load_model_and_labels()

def predict_disease(image_array):
    preds = model.predict(image_array, verbose=0)[0]

    predicted_index = int(np.argmax(preds))
    predicted_label = idx_to_class[predicted_index]
    confidence = float(np.max(preds))

    # ---- Entropy Calculation ----
    epsilon = 1e-10
    entropy = -np.sum(preds * np.log(preds + epsilon))

    # ---- Top-2 Probability Gap ----
    sorted_probs = np.sort(preds)
    top1 = sorted_probs[-1]
    top2 = sorted_probs[-2]
    prob_gap = float(top1 - top2)

    return predicted_label, confidence, entropy, prob_gap

def get_live_weather(city, api_key):
    import requests

    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={api_key}&units=metric"
    )

    try:
        res = requests.get(url, timeout=5)
        data = res.json()
        return {
            "temp": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "condition": data["weather"][0]["description"]
        }
    except Exception:
        return None

def detect_city_from_ip(default_city="Kurnool"):
    try:
        import requests
        res = requests.get("https://ipapi.co/json/", timeout=3)
        data = res.json()
        return data.get("city", default_city)
    except Exception:
        return default_city

# --------------------------------------------------
# Weather Location Initialization (IP + Fallback)
# --------------------------------------------------
if "user_location" not in st.session_state:
    try:
        detected_city = detect_city_from_ip("Kurnool")
        if detected_city and isinstance(detected_city, str):
            st.session_state.user_location = detected_city
        else:
            st.session_state.user_location = "Kurnool"
    except Exception:
        st.session_state.user_location = "Kurnool"

# --------------------------------------------------
# Remedies (REAL LOGIC)
# --------------------------------------------------
REMEDIES_PATH = os.path.join(BASE_DIR, "remedies", "remedies.json")
with open(REMEDIES_PATH, "r", encoding="utf-8") as f:
    REMEDIES_DATA = json.load(f)

# --------------------------------------------------
# Disease Details (FROM CHATBOT KNOWLEDGE BASE)
# --------------------------------------------------
DISEASE_DETAILS_PATH = os.path.join(
    BASE_DIR, "chatbot", "knowledge", "diseases.json"
)

if os.path.exists(DISEASE_DETAILS_PATH):
    with open(DISEASE_DETAILS_PATH, "r", encoding="utf-8") as f:
        DISEASE_DETAILS = json.load(f)
else:
    DISEASE_DETAILS = {}

# --------------------------------------------------
# Weather Advisory Knowledge Base
# --------------------------------------------------
WEATHER_DATA_PATH = os.path.join(
    BASE_DIR, "chatbot", "knowledge", "weather.json"
)

if os.path.exists(WEATHER_DATA_PATH):
    with open(WEATHER_DATA_PATH, "r", encoding="utf-8") as f:
        WEATHER_ADVISORY_DATA = json.load(f)
else:
    WEATHER_ADVISORY_DATA = {}

st.markdown(
    """
    <style>
    
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+Telugu&display=swap');
    html, body, [class*="css"] {
    font-family: 'Noto Sans Telugu', sans-serif;
    }

    /*==================================================
       MAIN APP BACKGROUND
    ================================================== */
    .stApp {
        background: linear-gradient(to bottom, #f1f8f4, #ffffff);
    }

    .block-container {
        padding-top: 2.2rem !important;
        padding-left: 3rem !important;
        padding-right: 3rem !important;
    }

    .section {
        margin-top: 2.5rem;
    }

    /* ==================================================
       CAMERA / CONTENT STYLING
    ================================================== */
    .camera-box {
        border: 2px dashed #9ca3af;
        border-radius: 12px;
        padding: 30px;
        text-align: center;
        background-color: #f9fafb;
        font-size: 16px;
        color: #374151;
    }

    .info-box {
        background-color: #ffffff;
        border-left: 5px solid #22c55e;
        padding: 18px;
        border-radius: 8px;
        line-height: 1.7;
        font-size: 15px;
        color: #1f2937;
    }

    .advisory-box {
        background-color: #f0fdf4;
        border: 1px solid #bbf7d0;
        padding: 18px;
        border-radius: 8px;
        font-size: 15px;
        line-height: 1.65;
    }

    /* ==================================================
       CONFIDENCE BAR
    ================================================== */
    .confidence-bar {
        height: 14px;
        border-radius: 8px;
        background-color: #e5e7eb;
        overflow: hidden;
    }

    .conf-high { background-color: #22c55e; }
    .conf-medium { background-color: #facc15; }
    .conf-low { background-color: #ef4444; }

    .confidence-wrapper {
        margin-top: 12px;
    }

    .confidence-label {
        font-size: 14px;
        font-weight: 600;
        color: #1f2937;
        margin-bottom: 6px;
    }

    .confidence-percentage {
        font-size: 13px;
        color: #374151;
        margin-bottom: 6px;
    }

    .confidence-fill {
        height: 100%;
        transition: width 0.8s ease-in-out;
    }

    /* ==================================================
       WEATHER BOX
    ================================================== */
    .weather-box {
        background: #ecfeff;
        border-left: 5px solid #06b6d4;
        padding: 18px;
        border-radius: 10px;
        margin-top: 20px;
    }

    .weather-box h4 {
        margin-bottom: 10px;
        color: #0f172a;
    }

    /* ==================================================
       FLOATING BUTTONS
    ================================================== */
    .chat-launcher {
        position: fixed;
        bottom: 28px;
        right: 28px;
        background-color: #22c55e;
        color: #ffffff;
        padding: 14px 20px;
        border-radius: 30px;
        font-size: 15px;
        font-weight: 600;
        box-shadow: 0 6px 16px rgba(0,0,0,0.2);
        cursor: pointer;
        z-index: 1000;
    }

    .voice-launcher {
        position: fixed;
        bottom: 90px;
        right: 28px;
        background-color: #2563eb;
        color: #ffffff;
        padding: 14px 16px;
        border-radius: 50%;
        font-size: 18px;
        font-weight: 600;
        box-shadow: 0 6px 16px rgba(0,0,0,0.2);
        cursor: pointer;
        z-index: 1000;
    }

    /* ==================================================
       SIDEBAR – INSTITUTIONAL STYLE
    ================================================== */

    section[data-testid="stSidebar"] {
        background-color: #f8fafc;
    }

    section[data-testid="stSidebar"] h3 {
        font-size: 15px;
        font-weight: 600;
        color: #1e293b;
        margin-bottom: 6px;
    }

    section[data-testid="stSidebar"] hr {
        margin-top: 12px;
        margin-bottom: 12px;
        border: none;
        height: 1px;
        background-color: #cbd5e1;
    }

    section[data-testid="stSidebar"] .streamlit-expanderHeader {
        font-weight: 500;
        font-size: 14px;
        color: #334155;
    }

    section[data-testid="stSidebar"] .streamlit-expanderContent {
        padding-top: 5px;
    }

    /* Sidebar App Header Refinement */
    section[data-testid="stSidebar"] div[style*="font-size:30px"] {
        margin-bottom: 4px;
    }

    section[data-testid="stSidebar"] div[style*="font-size:20px"] {
        letter-spacing: 0.4px;
        color: #0f172a;
    }

    /* Institutional Notice Box */
    .notice-box {
        font-size: 13px;
        line-height: 1.6;
        color: #334155;
        background: #f1f5f9;
        border-left: 4px solid #64748b;
        padding: 12px;
        border-radius: 6px;
    }

    /* ==================================================
       FOOTER
    ================================================== */
    .footer {
        text-align: center;
        font-size: 13px;
        color: #6b7280;
        line-height: 1.6;
        padding: 24px 0;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# --------------------------------------------------
# Splash Screen (UNCHANGED UI)
# --------------------------------------------------
def show_splash():
    placeholder = st.empty()
    with placeholder:
        st.markdown(
            """
            <div style="text-align:center; padding-top:120px;">
                <h1 style="color:#2e7d32;">AgriVision AI</h1>
                <p style="color:#4b5563;">
                    Smart Diagnosis · Simple Guidance · Local Language
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )
        progress = st.progress(0)
        for i in range(100):
            progress.progress(i + 1)
            time.sleep(0.02)
    placeholder.empty()
    st.session_state.loaded = True

if not st.session_state.loaded:
    show_splash()

# --------------------------------------------------
# Sidebar (Institutional Structure – Notice Moved)
# --------------------------------------------------
with st.sidebar:

    # ---- Language Selector ----
    st.selectbox(
        label="🌐 " + t(st.session_state.get('language', 'English'), 'language'),
        options=list(LANG.keys()),
        key="language"
    )

    language = st.session_state.language

    # --------------------------------------------------
    # 🌾 APP IDENTITY
    # --------------------------------------------------
    st.markdown(
    """
    <div style="margin-top:10px; margin-bottom:8px;">
        <div style="display:flex; align-items:center; gap:8px;">
            <div style="font-size:28px;">🌾</div>
            <div style="font-size:20px; font-weight:700;">
                """ + t(language, "app_name") + """
            </div>
        </div>
        <div style="font-size:13px; color:#64748b; margin-top:6px;">
            """ + t(language, "app_description") + """
        </div>
    </div>
    """,
    unsafe_allow_html=True)

    # ==================================================
    # 📚 HELP CENTER
    # ==================================================
    st.markdown("### 📚 " + t(language, 'help_center_title'))

    with st.expander("🧾 " + t(language, 'general_help'), expanded=False):
        faq_items_general = [
            (t(language, "faq_image_q"), t(language, "faq_image_a")),
            (t(language, "faq_crops_q"), t(language, "faq_crops_a")),
            (t(language, "faq_confidence_q"), t(language, "faq_confidence_a")),
            (t(language, "faq_offline_q"), t(language, "faq_offline_a")),
            (t(language, "faq_accuracy_q"), t(language, "faq_accuracy_a")),
            (t(language, "faq_after_detect_q"), t(language, "faq_after_detect_a")),
        ]
        for q, a in faq_items_general:
            with st.expander(q, expanded=False):
                st.markdown(a)

    with st.expander("🤖 " + t(language, 'chatbot_help'), expanded=False):
        chatbot_faq = [
            (t(language, "chatbot_use_q"), t(language, "chatbot_use_a")),
            (t(language, "chatbot_type_q"), t(language, "chatbot_type_a")),
            (t(language, "chatbot_lang_q"), t(language, "chatbot_lang_a")),
        ]
        for q, a in chatbot_faq:
            with st.expander(q, expanded=False):
                st.markdown(a)

    with st.expander("🎙 " + t(language, 'voice_help'), expanded=False):
        voice_faq = [
            (t(language, "voice_work_q"), t(language, "voice_work_a")),
            (t(language, "voice_delay_q"), t(language, "voice_delay_a")),
            (t(language, "voice_switch_q"), t(language, "voice_switch_a")),
        ]
        for q, a in voice_faq:
            with st.expander(q, expanded=False):
                st.markdown(a)

    # ==================================================
    # ⚖ NOTICE
    # ==================================================
    st.markdown("---")
    st.markdown("### ⚖ " + t(language, "important_notice"))

    disclaimer_text = t(language, "disclaimer_text").replace("\n", "<br>")
    st.markdown(f"""
        <div style="font-size:13px; line-height:1.6; color:#334155;
        background:#f8fafc; border-left:4px solid #94a3b8;
        padding:10px; border-radius:6px;">
            {disclaimer_text}
        </div>
    """, unsafe_allow_html=True)

    # ==================================================
    # 📬 CONTACT
    # ==================================================
    st.markdown("---")
    st.markdown("### 📬 " + t(language, 'contact_support'))

    with st.expander(t(language, "contact_expand"), expanded=False):
        st.markdown(t(language, "contact_text"))

    # ==================================================
    # 📝 FEEDBACK
    # ==================================================
    st.markdown("---")
    st.markdown("### 📝 " + t(language, 'feedback_title'))

    with st.expander(t(language, "feedback_expand"), expanded=False):

        rating = st.radio(
            t(language, "rate_experience"),
            [
                t(language, "rating_excellent"),
                t(language, "rating_good"),
                t(language, "rating_average"),
                t(language, "rating_improve")
            ],
            index=1
        )

        feedback_text = st.text_area(
            t(language, "your_comments"),
            height=80,
            placeholder=t(language, "optional_placeholder")
        )

        if st.button(t(language, "submit_feedback"), use_container_width=True):
            st.success(t(language, "thank_feedback"))
      
    # --------------------------------------------------
    # PAGE ROUTING
    # --------------------------------------------------

if st.session_state.get("show_chatbot", False):
    render_chatbot_ui(
        language,  
        disease=st.session_state.get("predicted_disease"),
        confidence=st.session_state.get("prediction_confidence")
    )
    st.stop()

elif st.session_state.get("show_voice", False):
    from voice_ui import render_voice_ui
    render_voice_ui(
        language,  
        disease=st.session_state.get("predicted_disease"),
        confidence=st.session_state.get("prediction_confidence")
    )
    st.stop()
    

# --------------------------------------------------
# MAIN PAGE UI 
# --------------------------------------------------

title = t(language, "main_title")
subtitle = t(language, "main_subtitle")

st.markdown(
    f"""
    <h2 style="color:#1f2937;">{title}</h2>
    <p style="color:#4b5563;">
        {subtitle}
    </p>
    """,
    unsafe_allow_html=True
)

# --------------------------------------------------
# BUTTON-BASED INPUT UI (CAMERA / UPLOAD)
# --------------------------------------------------
st.markdown("<div class='section'>", unsafe_allow_html=True)

# Show buttons only if no image selected
if st.session_state.image is None:

    col1, col2 = st.columns(2)

    with col1:
        if st.button("📷 " + t(language, "use_camera"), use_container_width=True):
            st.session_state.input_mode = "camera"

    with col2:
        if st.button("📁 " + t(language, "upload_image"), use_container_width=True):
            st.session_state.input_mode = "upload"

# ---------------- CAMERA MODE ----------------
if (
    st.session_state.input_mode == "camera"
    and st.session_state.image is None
):

    st.markdown(
        "<h3 class='heading-main'>📷 " + t(language, "capture_leaf") + "</h3>",
        unsafe_allow_html=True
    )

    try:
        cam_img = capture_leaf_image(language)

        if cam_img:
            image = cam_img.convert("RGB")
            current_hash = get_image_hash(image)

            if st.session_state.last_image_hash != current_hash:

                st.session_state.last_image_hash = current_hash
                st.session_state.image = image
                st.session_state.image_source = "camera"
                st.session_state.input_mode = None

                st.session_state.prediction_done = False
                st.session_state.predicted_disease = None
                st.session_state.prediction_confidence = None

    except Exception:
        st.warning(t(language, "camera_error"))

# ---------------- UPLOAD MODE ----------------
if (
    st.session_state.input_mode == "upload"
    and st.session_state.image is None
):

    st.markdown(
        "<h3 class='heading-main'>📁 " + t(language, "upload_leaf") + "</h3>",
        unsafe_allow_html=True
    )

    uploaded_file = st.file_uploader("", type=["jpg", "jpeg", "png"])

    if uploaded_file:

        image = Image.open(uploaded_file).convert("RGB")
        current_hash = get_image_hash(image)

        if st.session_state.last_image_hash != current_hash:

            st.session_state.last_image_hash = current_hash
            st.session_state.image = image
            st.session_state.image_source = "upload"
            st.session_state.input_mode = None

            st.session_state.prediction_done = False
            st.session_state.predicted_disease = None
            st.session_state.prediction_confidence = None

# ---------------- IMAGE PREVIEW ----------------
if st.session_state.image:

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        st.image(st.session_state.image, use_container_width=True)

    if st.session_state.image_source == "camera":
        label = "🔄 " + t(language, "retake_camera")
    else:
        label = "🔄 " + t(language, "reupload_image")

    if st.button(label, use_container_width=True):

        st.session_state.image = None
        st.session_state.image_source = None
        st.session_state.input_mode = None
        st.session_state.prediction_done = False
        st.session_state.predicted_disease = None
        st.session_state.prediction_confidence = None
        st.session_state.last_image_hash = None

        st.rerun()

st.markdown("</div>", unsafe_allow_html=True)

# --------------------------------------------------
# Analyze Action
# --------------------------------------------------
if st.session_state.image:

    st.markdown("<div style='margin-top:25px;'></div>", unsafe_allow_html=True)

    if st.button("🔬 " + t(language, "analyze_crop"), use_container_width=True):
        st.session_state.prediction_done = True

    st.markdown("<div style='margin-bottom:15px;'></div>", unsafe_allow_html=True)

# --------------------------------------------------
# Prediction Result (Structured AI Report)
# --------------------------------------------------
if st.session_state.prediction_done and st.session_state.image is not None:

    # -------------------------------
    # Model Prediction
    # -------------------------------
    with st.spinner(t(language, "analyzing")):
        start_time = time.time()

        img = st.session_state.image.resize((224, 224))
        img_arr = np.expand_dims(np.array(img) / 255.0, axis=0)

        disease, confidence, entropy, prob_gap = predict_disease(img_arr)

        end_time = time.time()

    inference_time = round(end_time - start_time, 3)
    timestamp = datetime.now().strftime("%d %b %Y | %H:%M IST")

    # Save results
    st.session_state["predicted_disease"] = disease
    st.session_state["prediction_confidence"] = confidence
    st.session_state["inference_time"] = inference_time
    st.session_state["timestamp"] = timestamp

    confidence_pct = int(confidence * 100)

    # ==================================================
    # 🛑 OPEN-SET REJECTION
    # ==================================================
    CONFIDENCE_THRESHOLD = 0.50
    ENTROPY_THRESHOLD = 1.6
    GAP_THRESHOLD = 0.15

    if confidence < CONFIDENCE_THRESHOLD:
        st.error(t(language, "invalid_leaf"))
        st.stop()

    if entropy > ENTROPY_THRESHOLD or prob_gap < GAP_THRESHOLD:
        st.error(t(language, "unsupported_crop"))
        st.stop()

    # ==================================================
    # 🧪 AI DIAGNOSIS SUMMARY
    # ==================================================
    display_name = DISEASE_TRANSLATIONS.get(disease, {}).get(language, disease)

    bar_class = (
        "conf-high" if confidence_pct >= 80
        else "conf-medium" if confidence_pct >= 50
        else "conf-low"
    )

    st.markdown("## 🧪 " + t(language, "diagnosis_summary"))

    predicted_label = t(language, "predicted_condition")
    confidence_label = t(language, "model_confidence")
    model_label = t(language, "model")
    input_label = t(language, "input_size")
    time_label = t(language, "inference_time")
    gen_label = t(language, "generated")

    st.markdown(
        f"""
        <div style="background:#ffffff;
        border:1px solid #e2e8f0;
        border-radius:12px;
        padding:24px;
        margin-top:10px;">

        <div style="font-size:13px; color:#64748b; font-weight:600;">
        {predicted_label}
        </div>

        <div style="font-size:22px; font-weight:700; margin-top:6px;">
        {display_name}
        </div>

        <div style="margin-top:20px;">
        <div style="font-size:13px; font-weight:600;">
        {confidence_label}
        </div>

        <div style="font-size:13px; color:#475569; margin-bottom:8px;">
        {confidence_pct}%
        </div>

        <div class="confidence-bar">
        <div class="confidence-fill {bar_class}"
        style="width:{confidence_pct}%"></div>
        </div>
        </div>

        <hr style="margin:20px 0;">

        <div style="font-size:13px; color:#334155;">
        🧠 <b>{model_label}:</b> MobileNet v2<br>
        📦 <b>{input_label}:</b> 224 × 224<br>
        ⏱ <b>{time_label}:</b> {inference_time} sec<br>
        🕒 <b>{gen_label}:</b> {timestamp}
        </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    # ==================================================
    # HEALTHY vs DISEASED LOGIC
    # ==================================================
    crop_name = None

    if "healthy" in disease.lower():

        st.markdown("## 🌿 " + t(language, "crop_health"))
        st.success(t(language, "healthy_msg"))

    else:

        # ==================================================
        # 🧬 Disease Analysis
        # ==================================================
        st.markdown("## 🧬 " + t(language, "disease_analysis"))

        details = DISEASE_DETAILS.get(disease)

        if details:
            crop_name = details.get("crop", {}).get(language)

            if crop_name:
                st.markdown("**🌾 " + t(language, "crop_label") + ":** " + crop_name)

            symptoms = details.get("symptoms", {}).get(language, [])
            if symptoms:
                st.markdown("**🩺 " + t(language, "symptoms_label") + ":**")
                for s in symptoms:
                    st.markdown("- " + s)

            advice = details.get("general_advice", {}).get(language, [])
            if advice:
                st.markdown("**📋 " + t(language, "actions_label") + ":**")
                for a in advice:
                    st.markdown("- " + a)

            note = details.get("note", {}).get(language)
            if note:
                st.info(note)

        else:
            st.warning(t(language, "no_info"))

        # ==================================================
        # 💊 Treatment & Remedies
        # ==================================================
        st.markdown("## 💊 " + t(language, "treatment"))

        remedy_info = REMEDIES_DATA.get(disease, {})

        if language in remedy_info:
            for r in remedy_info[language]["remedies"]:
                st.markdown("- " + r)
        else:
            st.warning(t(language, "no_remedy"))

        # ==================================================
        # 🔎 AI Extended Insight
        # ==================================================
        if confidence >= CONFIDENCE_THRESHOLD + 0.10:

            st.markdown("## 🔎 " + t(language, "ai_insight"))

            insight_key = f"{disease}_{language}"

            if st.button(t(language, "get_insight"), use_container_width=True):

                enrichment_text = None

                if insight_key in st.session_state.extended_insights:
                    enrichment_text = st.session_state.extended_insights[insight_key]
                else:
                    with st.spinner(t(language, "generating")):
                        enrichment_text = generate_disease_enrichment(
                            disease=disease,
                            crop_name=crop_name if crop_name else "",
                            output_language=language
                        )

                    if enrichment_text:
                        st.session_state.extended_insights[insight_key] = enrichment_text

                if enrichment_text:
                    formatted_text = enrichment_text.replace("\n", "<br>")
                    st.markdown(
                        f"""
                        <div style="
                        background:#f8fafc;
                        border:1px solid #cbd5e1;
                        border-radius:10px;
                        padding:18px;
                        margin-top:10px;">
                        {formatted_text}
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

    # ==================================================
    # 🌦 Weather Section
    # ==================================================
    if crop_name:

        st.markdown("## 🌦 " + t(language, "weather_title"))

        if not WEATHER_API_KEY:
            st.warning(t(language, "weather_not_configured"))
        else:

            USER_LOCATION = st.text_input(
                t(language, "location"),
                value=st.session_state.user_location
            )

            USER_LOCATION = USER_LOCATION.strip().title()
            if not USER_LOCATION:
                USER_LOCATION = "Kurnool"

            st.session_state.user_location = USER_LOCATION

            try:
                weather_data = get_weather_data(USER_LOCATION)
                
                live_weather = {
                    "temp": weather_data["temperature"],
                    "humidity": weather_data["humidity"],
                    "condition": weather_data["description"]
                    }
            except ValueError as e:
                st.error(t(language, str(e)))
                live_weather = None

            if live_weather:
                translated_condition = t(language, live_weather['condition'])
                st.markdown(
                    f"""
                    <div style="
                        background:#f8fafc;
                        border:1px solid #e2e8f0;
                        border-radius:10px;
                        padding:18px;
                        margin-top:8px;">
                        <b>📍 {USER_LOCATION}</b><br>
                        🌡 {t(language,'temperature')}: {live_weather['temp']}°C<br>
                        💧 {t(language,'humidity')}: {live_weather['humidity']}%<br>
                        ☁ {t(language,'condition')}: {translated_condition}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                humidity = live_weather.get("humidity", 0)

                if humidity >= 80:
                    st.warning(t(language, "humidity_high"))
                elif humidity <= 40:
                    st.warning(t(language, "humidity_low"))
                
                weather_input = {
                    "temperature": live_weather["temp"],
                    "humidity": live_weather["humidity"],
                    "rainfall": "high" if live_weather["humidity"] > 80 else "low"
                    }
                severity = calculate_weather_severity(weather_input)
                
                st.markdown(
                    "### ⚠ " + t(language, "risk_level") + ": " + t(language, severity)
                    )
                
                advisories = analyze_weather_risk(weather_input, crop_name)
                for adv in advisories:
                    st.warning(t(language, adv) if adv in LANG.get(language, {}) else adv)        
            else:
                st.warning(t(language, "weather_fetch_error"))
                
                

# --------------------------------------------------
# CUSTOM CARD STYLING
# --------------------------------------------------
st.markdown("""
<style>

/* Remove extra space between columns */
div[data-testid="column"] {
    padding: 0.3rem !important;
}

/* Remove vertical spacing between blocks */
div[data-testid="stVerticalBlock"] > div {
    gap: 0.5rem !important;
}

/* Style Streamlit Buttons Directly */
div.stButton > button {
    width: 100%;
    padding: 16px 20px;
    border-radius: 12px;
    border: 1px solid #d1d5db;
    background-color: #f9fafb;
    font-size: 16px;
    font-weight: 500;
    transition: all 0.25s ease;
}

/* BLUE Glow Hover */
div.stButton > button:hover {
    border: 1px solid #2563eb;
    box-shadow: 0 0 18px rgba(37, 99, 235, 0.45);
    transform: translateY(-2px);
}

/* Click Animation */
div.stButton > button:active {
    transform: scale(0.98);
}

</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# LAYOUT
# --------------------------------------------------
st.markdown("<div style='margin-top:30px;'></div>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    if st.button("🤖 " + t(language, "agri_assist"), key="chat_btn", use_container_width=True):
        st.session_state.show_chatbot = True
        st.rerun()

with col2:
    if st.button("🎙 " + t(language, "voice_assist"), key="voice_btn", use_container_width=True):
        st.session_state.show_voice = True
        st.empty()
        st.stop()

st.markdown("<div style='height:30px;'></div>", unsafe_allow_html=True)

st.markdown(
    f"""
    <hr>
    <div class="footer">
        {t(language,'footer_line1')}<br>
        {t(language,'footer_line2')}<br>
        {t(language,'footer_line3')}
    </div>
    """,
    unsafe_allow_html=True
)
