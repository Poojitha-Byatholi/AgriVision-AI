
LANG = {

    # ==================================================
    # ENGLISH
    # ==================================================
    "English": {

        # -------- Sidebar / App --------
        "app_name": "AgriVision AI",
        "tagline": "AI-powered crop health assistant",
        "language": "Language",
        "help_faq": "Help (FAQ)",

        # -------- FAQ --------
        "faq_image_q": "How do I take a clear leaf image?",
        "faq_image_a": (
            "- Capture the image in good natural light.\n"
            "- Focus on a single leaf.\n"
            "- Avoid blur."
        ),

        "faq_crops_q": "Which crops are supported?",
        "faq_crops_a": (
            "The following crops are currently supported by this system:\n"
            "- Rice\n- Wheat\n- Cotton\n- Pepper\n- Tomato\n- Potato\n- Maize"
        ),

        "faq_confidence_q": "What if the prediction confidence is low?",
        "faq_confidence_a": (
            "Try capturing a clearer image with proper lighting and focus.\n"
            "If the confidence remains low, consult a local agricultural expert.\n"
            "or extension officer for professional guidance."
        ),

        "faq_offline_q": "Can this system work offline?",
        "faq_offline_a": (
            "Image analysis works locally once the application is running.\n"
            "However, live weather advisory requires an active internet connection."
        ),

        "faq_accuracy_q": "Is this system 100% accurate?",
        "faq_accuracy_a": (
            "No AI-based system can guarantee 100% accuracy.\n"
            "This tool is intended to provide advisory support and decision assistance."
        ),

        "faq_after_detect_q": "What should I do after detecting a disease?",
        "faq_after_detect_a": (
            "- Follow the suggested remedies provided by the system\n"
            "- Monitor the crop condition regularly\n"
            "- Avoid excessive irrigation or fertilizer use\n"
            "- Contact local agricultural officers or experts if the issue persists"
        ),
        
        # -------- Help Center Extra --------
        "help_center_title": "Help Center",
        "general_help": "General Help",
        "chatbot_help": "AgriAssist (Chatbot)",
        "voice_help": "Voice Assistant",

        "chatbot_use_q": "How do I use the chatbot?",
        "chatbot_use_a": "Click AgriAssist and type your question. It provides multilingual crop guidance and remedies.",

        "chatbot_type_q": "What type of questions can I ask?",
        "chatbot_type_a": "You can ask about disease symptoms, treatments, prevention, weather advisory, and farming guidance.",

        "chatbot_lang_q": "Does chatbot support multiple languages?",
        "chatbot_lang_a": "Yes. Select your preferred language from the sidebar dropdown.",

        "voice_work_q": "How does the voice assistant work?",
        "voice_work_a": "Click Voice Assist, press Speak, and ask your question naturally. The system converts speech to text and responds with voice output.",

        "voice_delay_q": "Why does voice processing take a few seconds?",
        "voice_delay_a": "Speech recognition and AI response generation require computation time depending on system performance.",

        "voice_switch_q": "Can I switch between Chatbot and Voice?",
        "voice_switch_a": "Yes. You can switch anytime using the buttons at the bottom of the page.",

        "contact_support": "Contact Support",
        "contact_expand": "Need Help? Reach Out to Us",
        "contact_text": (
            "If you experience any of the following:\n"
            "- Incorrect disease prediction\n"
            "- Voice assistant not responding\n"
            "- Weather advisory not loading\n"
            "- Technical errors or unexpected behavior\n\n"
            "Please contact the support team.\n\n"
            "Email: agrivision.support@example.com\n"
            "Response Time: Within 24–48 hours\n\n"
            "This application is developed for academic and demonstration purposes.\n"
            "Your feedback helps improve the system's accuracy and performance."
        ),

        "feedback_title": "Feedback",
        "feedback_expand": "Share Your Feedback",
        "rate_experience": "Rate your experience",
        "your_comments": "Your suggestions or comments",
        "submit_feedback": "Submit Feedback",
        "thank_feedback": "Thank you for your feedback!",

        # -------- Important Notice --------
        "important_notice": "Important Notice",
        "disclaimer_text": (
            "This system provides AI-based advisory assistance only.\n"
            "Predictions may vary depending on image quality, lighting conditions,\n"
            "and environmental factors.\n\n"
            "Farmers are strongly encouraged to consult local agricultural experts,\n"
            "extension officers, or plant pathologists for confirmed diagnosis\n"
            "and treatment decisions."
        ),

        # -------- Footer --------
        "footer_line1": "AgriVision AI – Final Year Academic Project",
        "footer_line2": "AI-Based Crop Disease Detection & Multilingual Farming Assistant",
        "footer_line3": "Developed for educational and advisory demonstration purposes only.",

        # -------- Results / Prediction --------
        "result_disease_detected": "Disease Detected",
        "result_prediction_confidence": "Prediction Confidence",
        "result_disease_info": "Disease Information",
        "result_crop": "Crop",
        "result_symptoms": "Symptoms",
        "result_general_advice": "General Advisory",
        "result_weather_advisory": "Weather Advisory",
        "result_recommended_advisory": "Recommended Advisory",
        "result_remedy_unavailable": "Remedy information not available in the selected language.",
        "humidity_high": (
            "High humidity detected. Increased risk of fungal diseases. "
            "Avoid overhead irrigation and monitor crop closely."
        ),
        "humidity_low": (
            "Low humidity detected. Ensure adequate irrigation and "
            "monitor for moisture stress."
        ),  
        # -------- New UI Keys --------
        "main_title": "Crop Disease Detection & Advisory",
        "main_subtitle": "Capture a leaf image to receive AI-based diagnosis and guidance.",
        
        "use_camera": "Use Camera",
        "upload_image": "Upload Image",
        "capture_leaf": "Capture Leaf Image",
        "upload_leaf": "Upload Leaf Image",
        
        "retake_camera": "Retake Image (Camera)",
        "reupload_image": "Re-upload Image",
        "analyze_crop": "Analyze Crop",
        
        "camera_error": "⚠️ Camera not accessible. Please allow camera permission.",
        
        # -------- Ratings --------
        "rating_excellent": "Excellent",
        "rating_good": "Good",
        "rating_average": "Average",
        "rating_improve": "Needs Improvement",
        "optional_placeholder": "Optional suggestions...",
        
        # -------- Errors --------
        "invalid_leaf": "⚠ The uploaded image is not a clear supported crop leaf. Please upload a high-quality image.",
        "unsupported_crop": "⚠ The image may not belong to supported crop categories.",
        # -------- Prediction --------
        "diagnosis_summary": "AI Diagnosis Summary",
        "predicted_condition": "Predicted Condition",
        "model_confidence": "Model Confidence",
        "model": "Model",
        "input_size": "Input Size",
        "inference_time": "Inference Time",
        "generated": "Generated",
        
        # -------- Disease --------
        "crop_health": "Crop Health Status",
        "healthy_msg": "Leaf appears healthy. No disease detected.",
        "disease_analysis": "Disease Analysis",
        "crop_label": "Crop",
        "symptoms_label": "Symptoms Observed",
        "actions_label": "Recommended Actions",
        "no_info": "No detailed information available for this disease.",
        
        # -------- Remedies --------
        "treatment": "Treatment & Remedies",
        "no_remedy": "Remedy information not available.",
        
        # -------- AI --------
        "ai_insight": "AI Extended Insight",
        "get_insight": "Get Extended AI Insight",
        "generating": "Generating AI insight...",
        "analyzing": "Analyzing image...",
        
        # -------- Weather --------
        "weather_title": "Weather Details",
        "weather_not_configured": "Weather service not configured.",
        "location": "Location",
        "temperature": "Temperature",
        "humidity": "Humidity",
        "condition": "Condition",
        "weather_fetch_error": "Unable to fetch live weather data.",
        
        # -------- Buttons --------
        "agri_assist": "AgriAssist",
        "voice_assist": "Voice Assist", 
        
        "app_name": "AgriVision AI",
        "app_description": "AI-Driven Crop Disease Research & Advisory System",
        
        "capture_image": "Capture Image",
        "image_captured_success": "Image captured successfully ✓",
        "processing_stopped": "Process stopped",
        
        "humidity_risk": "High humidity increases the risk of fungal diseases. Regular field inspection is advised.",
        "heavy_rainfall": "Heavy rainfall detected. Avoid excess irrigation and ensure proper drainage.",
        "heat_stress": "High temperature may cause crop stress. Ensure adequate irrigation.",
        "wheat_rust_risk": "Wheat is susceptible to rust diseases under high humidity. Consider preventive fungicide application.",
        "rice_lodging_risk": "Excess rainfall in rice fields may cause lodging. Monitor water levels carefully.",
        "favorable_weather": "Weather conditions are currently favorable for crop growth.",
        
        "high_risk": "HIGH RISK",
        "moderate_risk": "MODERATE RISK",
        "low_risk": "LOW RISK",
        
        "weather_api_missing": "Weather service is not configured. Please try again later.",
        
        "no_response_fallback": "Sorry, I couldn’t find relevant information. Please try rephrasing.",
        
        "chatbot_title": "AgriAssist",
        "chatbot_caption": "AI-powered Crop Disease Knowledge Assistant",
        "chatbot_welcome": "Hello! I am AgriAssist 🌿\n\nAsk me about crops, diseases, fertilizers, soil, weather, or schemes.",
        "chat_input_placeholder": "Ask about crops, diseases, fertilizers...",
        "back_button": "⬅ Back to Detection",
        "status_online": "Online",
        "status_thinking": "Thinking...",
        "typing_message": "AgriAssist is typing",
        "suggested_questions": "Suggested Questions",
        "detected_disease": "Detected disease",
        "suggest_tomato_fertilizer": "Tomato fertilizer advice",
        "suggest_tomato_season": "Tomato seasonal information",
        "suggest_tomato_prevention": "Tomato prevention methods",
        "suggest_rice_fertilizer": "Rice fertilizer advice",
        "suggest_rice_season": "Rice seasonal information",
        "suggest_rice_prevention": "Rice prevention methods",
        "suggest_wheat_fertilizer": "Wheat fertilizer recommendation",
        "suggest_wheat_season": "Wheat seasonal advisory",
        "suggest_insurance": "Crop insurance details",
        "suggest_soil_card": "Soil health card scheme",
        "suggest_general_prevention": "General prevention practices",
        "suggest_maize_fertilizer": "Fertilizer advice for maize",
        "suggest_weather_cotton": "Weather advisory for cotton",
        
        "voice_title": "AgriVision AI Voice Assistant",
        "voice_instruction": "Tap mic and speak naturally",
        "mic_start": "🎤 Speak",
        "mic_stop": "⏹ Done",
        "processing_message": "Processing your request...",
        "voice_not_understood": "I could not understand. Please try again.",
        "you_label": "You",
        "assistant_label": "Assistant",
        "risk_level": "Risk Level",
        
        "broken clouds": "Broken Clouds",
        "clear sky": "Clear Sky",
        "few clouds": "Few Clouds",
        "scattered clouds": "Scattered Clouds",
        "overcast clouds": "Overcast Clouds",
        
        "low": "Low Risk",
        "medium": "Moderate Risk",
        "high": "High Risk",
    },

    # ==================================================
    # TELUGU
    # ==================================================
    "Telugu": {

        "app_name": "అగ్రివిజన్ AI",
        "tagline": "ఏఐ ఆధారిత పంట ఆరోగ్య సహాయకుడు",
        "language": "భాష",
        "help_faq": "సహాయం (FAQ)",

        "faq_image_q": "స్పష్టమైన ఆకు చిత్రం ఎలా తీసుకోవాలి?",
        "faq_image_a": (
            "- మంచి సహజ వెలుతురులో చిత్రం తీయండి.\n"
            "- ఒకే ఆకు పై దృష్టి పెట్టండి.\n"
            "- మసకబారకుండా చూసుకోండి."
        ),

        "faq_crops_q": "ఏ పంటలకు మద్దతు ఉంది?",
        "faq_crops_a": (
            "ఈ వ్యవస్థ ప్రస్తుతం క్రింది పంటలను మద్దతు ఇస్తుంది:\n"
            "- వరి\n- గోధుమ\n- పత్తి\n- మిరప\n- టమోటా\n- బంగాళాదుంప\n- మక్క"
        ),

        "faq_confidence_q": "అంచనా నమ్మక స్థాయి తక్కువగా ఉంటే ఏమి చేయాలి?",
        "faq_confidence_a": (
            "సరైన వెలుతురు మరియు ఫోకస్‌తో స్పష్టమైన చిత్రం తీసుకోండి.\n"
            "నమ్మక స్థాయి ఇంకా తక్కువగా ఉంటే స్థానిక వ్యవసాయ నిపుణులను\n"
            "లేదా విస్తరణ అధికారులను సంప్రదించండి."
        ),

        "faq_offline_q": "ఈ వ్యవస్థ ఆఫ్‌లైన్‌లో పనిచేస్తుందా?",
        "faq_offline_a": (
            "అనువర్తనం నడుస్తున్నప్పుడు చిత్రం విశ్లేషణ స్థానికంగా జరుగుతుంది.\n"
            "కానీ ప్రత్యక్ష వాతావరణ సలహాకు ఇంటర్నెట్ అవసరం."
        ),

        "faq_accuracy_q": "ఈ వ్యవస్థ 100% ఖచ్చితమా?",
        "faq_accuracy_a": (
            "ఏఐ ఆధారిత వ్యవస్థలు 100% ఖచ్చితత్వాన్ని హామీ ఇవ్వలేవు.\n"
            "ఈ సాధనం మార్గదర్శక సహాయం మాత్రమే అందిస్తుంది."
        ),

        "faq_after_detect_q": "వ్యాధి గుర్తించిన తర్వాత ఏమి చేయాలి?",
        "faq_after_detect_a": (
            "- వ్యవస్థ సూచించిన చికిత్సలను అనుసరించండి\n"
            "- పంట పరిస్థితిని క్రమం తప్పకుండా పరిశీలించండి\n"
            "- అధిక నీటిపారుదల లేదా ఎరువుల వాడకాన్ని నివారించండి\n"
            "- సమస్య కొనసాగితే స్థానిక వ్యవసాయ నిపుణులను సంప్రదించండి"
        ),
        
         # -------- Help Center Extra --------
        "help_center_title": "సహాయ కేంద్రం",
        "general_help": "సాధారణ సహాయం",
        "chatbot_help": "AgriAssist (చాట్‌బాట్)",
        "voice_help": "వాయిస్ అసిస్టెంట్",

        "chatbot_use_q": "నేను చాట్‌బాట్‌ను ఎలా ఉపయోగించాలి?",
        "chatbot_use_a": "AgriAssist పై క్లిక్ చేసి మీ ప్రశ్నను టైప్ చేయండి. ఇది బహుభాషా పంట మార్గదర్శకాలు మరియు పరిష్కారాలను అందిస్తుంది.",

        "chatbot_type_q": "నేను ఎలాంటి ప్రశ్నలు అడగగలను?",
        "chatbot_type_a": "మీరు వ్యాధి లక్షణాలు, చికిత్సలు, నివారణ, వాతావరణ సలహాలు మరియు వ్యవసాయ మార్గదర్శకత గురించి అడగవచ్చు.",

        "chatbot_lang_q": "చాట్‌బాట్ బహుభాషా మద్దతు ఇస్తుందా?",
        "chatbot_lang_a": "అవును. సైడ్‌బార్ డ్రాప్‌డౌన్ నుండి మీకు ఇష్టమైన భాషను ఎంచుకోండి.",

        "voice_work_q": "వాయిస్ అసిస్టెంట్ ఎలా పనిచేస్తుంది?",
        "voice_work_a": "Voice Assist పై క్లిక్ చేసి Speak నొక్కి సహజంగా మీ ప్రశ్న అడగండి. సిస్టమ్ మీ వాయిస్‌ను టెక్స్ట్‌గా మార్చి వాయిస్ అవుట్‌పుట్‌తో సమాధానం ఇస్తుంది.",

        "voice_delay_q": "వాయిస్ ప్రాసెసింగ్‌కు కొన్ని సెకన్లు ఎందుకు పడుతుంది?",
        "voice_delay_a": "స్పీచ్ గుర్తింపు మరియు AI ప్రతిస్పందన తయారీకి సిస్టమ్ పనితీరుపై ఆధారపడి సమయం పడుతుంది.",

        "voice_switch_q": "నేను చాట్‌బాట్ మరియు వాయిస్ మధ్య మారగలనా?",
        "voice_switch_a": "అవును. పేజీ దిగువన ఉన్న బటన్లను ఉపయోగించి ఎప్పుడైనా మారవచ్చు.",

        "contact_support": "సహాయానికి సంప్రదించండి",
        "contact_expand": "సహాయం కావాలా? మమ్మల్ని సంప్రదించండి",
        "contact_text": (
            "మీకు క్రింది సమస్యల్లో ఏదైనా ఎదురైతే:\n"
            "- తప్పు వ్యాధి అంచనా\n"
            "- వాయిస్ అసిస్టెంట్ స్పందించకపోవడం\n"
            "- వాతావరణ సలహా లోడ్ కాకపోవడం\n"
            "- సాంకేతిక లోపాలు లేదా అనుకోని ప్రవర్తన\n\n"
            "దయచేసి సహాయ బృందాన్ని సంప్రదించండి.\n\n"
            "ఇమెయిల్: agrivision.support@example.com\n"
            "ప్రతిస్పందన సమయం: 24–48 గంటలలోపు\n\n"
            "ఈ అప్లికేషన్ విద్యా మరియు ప్రదర్శన ప్రయోజనాల కోసం అభివృద్ధి చేయబడింది.\n"
            "మీ అభిప్రాయం వ్యవస్థ ఖచ్చితత్వం మరియు పనితీరును మెరుగుపరచడంలో సహాయపడుతుంది."
        ),

        "feedback_title": "అభిప్రాయం",
        "feedback_expand": "మీ అభిప్రాయాన్ని పంచుకోండి",
        "rate_experience": "మీ అనుభవాన్ని రేట్ చేయండి",
        "your_comments": "మీ సూచనలు లేదా వ్యాఖ్యలు",
        "submit_feedback": "అభిప్రాయం సమర్పించండి",
        "thank_feedback": "మీ అభిప్రాయం కోసం ధన్యవాదాలు!",

        # -------- Important Notice --------
        "important_notice": "ముఖ్య గమనిక",
        "disclaimer_text": (
            "ఈ వ్యవస్థ ఏఐ ఆధారిత మార్గదర్శక సహాయం మాత్రమే అందిస్తుంది.\n"
            "చిత్ర నాణ్యత, వెలుతురు పరిస్థితులు మరియు పర్యావరణ కారకాలపై\n"
            "అంచనాలు మారవచ్చు.\n\n"
            "ఖచ్చితమైన నిర్ధారణ మరియు చికిత్స కోసం రైతులు స్థానిక వ్యవసాయ నిపుణులను,\n"
            "విస్తరణ అధికారులను లేదా మొక్కల రోగ నిపుణులను సంప్రదించాలి."
        ),

        "footer_line1": "అగ్రివిజన్ AI – తుది సంవత్సరం అకాడెమిక్ ప్రాజెక్ట్",
        "footer_line2": "ఏఐ ఆధారిత పంట వ్యాధి గుర్తింపు & బహుభాషా వ్యవసాయ సహాయకుడు",
        "footer_line3": "విద్యా మరియు మార్గదర్శక ప్రదర్శన ప్రయోజనాల కోసం మాత్రమే",

        # -------- Results / Prediction --------
        "result_disease_detected": "వ్యాధి గుర్తించబడింది",
        "result_prediction_confidence": "అంచనా నమ్మక స్థాయి",
        "result_disease_info": "వ్యాధి సమాచారం",
        "result_crop": "పంట",
        "result_symptoms": "లక్షణాలు",
        "result_general_advice": "సాధారణ సలహా",
        "result_weather_advisory": "వాతావరణ సలహా",
        "result_recommended_advisory": "సూచించిన చికిత్స",
        "result_remedy_unavailable": "ఎంచుకున్న భాషలో చికిత్స సమాచారం అందుబాటులో లేదు.",
        "humidity_high": (
            "అధిక తేమ గుర్తించబడింది. శిలీంద్ర వ్యాధుల ప్రమాదం ఎక్కువగా ఉంటుంది. "
            "పై నుండి నీరు పోయడం నివారించండి మరియు పంటను జాగ్రత్తగా పరిశీలించండి."
        ),
        "humidity_low": (
            "తక్కువ తేమ గుర్తించబడింది. సరైన నీటిపారుదలని నిర్ధారించండి మరియు "
            "తేమ లోపం వల్ల వచ్చే ఒత్తిడిని గమనించండి."
        ),
        
        "main_title": "పంట వ్యాధి గుర్తింపు & సలహా",
        "main_subtitle": "ఆకు చిత్రాన్ని తీసి AI ఆధారిత నిర్ధారణ మరియు మార్గదర్శకాన్ని పొందండి.",
        
        "use_camera": "కెమెరా ఉపయోగించండి",
        "upload_image": "చిత్రాన్ని అప్లోడ్ చేయండి",
        "capture_leaf": "ఆకు చిత్రాన్ని తీసుకోండి",
        "upload_leaf": "ఆకు చిత్రాన్ని అప్లోడ్ చేయండి",
        
        "retake_camera": "మళ్లీ ఫోటో తీసుకోండి",
        "reupload_image": "మళ్లీ అప్లోడ్ చేయండి",
        "analyze_crop": "పంటను విశ్లేషించండి",
        
        "camera_error": "⚠️ కెమెరా అందుబాటులో లేదు. అనుమతి ఇవ్వండి.",
        
        "rating_excellent": "అత్యుత్తమం",
        "rating_good": "మంచిది",
        "rating_average": "సగటు",
        "rating_improve": "మెరుగుదల అవసరం",
        "optional_placeholder": "ఐచ్చిక సూచనలు...",
        
        "invalid_leaf": "⚠ ఈ చిత్రం సరైన పంట ఆకుగా లేదు. స్పష్టమైన చిత్రం అప్లోడ్ చేయండి.",
        "unsupported_crop": "⚠ ఈ చిత్రం మద్దతు ఉన్న పంటలకు చెందినది కాదు.",
        
        "diagnosis_summary": "AI నిర్ధారణ సారాంశం",
        
        "predicted_condition": "అంచనా పరిస్థితి",
        "model_confidence": "మోడల్ నమ్మక స్థాయి",
        "model": "మోడల్",
        "input_size": "ఇన్‌పుట్ పరిమాణం",
        "inference_time": "ప్రాసెసింగ్ సమయం",
        "generated": "సృష్టించిన సమయం",
        
        "crop_health": "పంట ఆరోగ్య స్థితి",
        "healthy_msg": "ఆకు ఆరోగ్యంగా ఉంది. వ్యాధి లేదు.",
        "disease_analysis": "వ్యాధి విశ్లేషణ",
        "crop_label": "పంట",
        "symptoms_label": "లక్షణాలు",
        "actions_label": "సూచించిన చర్యలు",
        "no_info": "ఈ వ్యాధికి సమాచారం అందుబాటులో లేదు.",
        
        "treatment": "చికిత్స & పరిష్కారాలు",
        "no_remedy": "చికిత్స సమాచారం అందుబాటులో లేదు.",
        
        "ai_insight": "AI విస్తృత విశ్లేషణ",
        "get_insight": "AI విశ్లేషణ పొందండి",
        "generating": "AI విశ్లేషణ తయారవుతోంది...",
        "analyzing": "చిత్రం విశ్లేషణ జరుగుతోంది...",
        
        "weather_title": "వాతావరణ వివరాలు",
        "weather_not_configured": "వాతావరణ సేవ అందుబాటులో లేదు.",
        "location": "ప్రాంతం",
        "temperature": "ఉష్ణోగ్రత",
        "humidity": "తేమ",
        "condition": "స్థితి",
        "weather_fetch_error": "వాతావరణ డేటా పొందలేకపోయాము.",
        
        "agri_assist": "AgriAssist",
        "voice_assist": "వాయిస్ సహాయకుడు",
        
        "app_name": "అగ్రివిజన్ AI",
        "app_description": "AI ఆధారిత పంట వ్యాధి పరిశోధన & సలహా వ్యవస్థ",
        
        "capture_image": "చిత్రాన్ని తీసుకోండి",
        "image_captured_success": "చిత్రం విజయవంతంగా తీసుకోబడింది ✓",
        "processing_stopped": "ప్రక్రియ నిలిపివేయబడింది",
        
        "high_risk": "అధిక ప్రమాదం",
        "moderate_risk": "మధ్యస్థ ప్రమాదం",
        "low_risk": "తక్కువ ప్రమాదం",
        
        "humidity_risk": "అధిక ఆర్ద్రత ఫంగస్ వ్యాధుల ప్రమాదాన్ని పెంచుతుంది. క్రమం తప్పకుండా పంటను పరిశీలించండి.",
        "heavy_rainfall": "భారీ వర్షపాతం గుర్తించబడింది. అధిక నీరుపారుదల నివారించి సరైన డ్రైనేజ్ ఉండేలా చూడండి.",
        "heat_stress": "అధిక ఉష్ణోగ్రత పంటపై ఒత్తిడిని కలిగించవచ్చు. తగినంత నీరుపారుదల ఇవ్వండి.",
        "wheat_rust_risk": "అధిక ఆర్ద్రతలో గోధుమలో రస్ట్ వ్యాధులు వచ్చే అవకాశం ఉంది. ముందస్తుగా ఫంగిసైడ్ ఉపయోగించండి.",
        "rice_lodging_risk": "వరిలో అధిక వర్షపాతం వల్ల మొక్కలు వంగిపోవచ్చు. నీటి మట్టాన్ని పర్యవేక్షించండి.",
        "favorable_weather": "ప్రస్తుతం వాతావరణ పరిస్థితులు పంట పెరుగుదలకు అనుకూలంగా ఉన్నాయి.",  
        
         "weather_api_missing": "వాతావరణ సేవ అమర్చబడలేదు. దయచేసి తరువాత ప్రయత్నించండి.",
         
         "no_response_fallback": "క్షమించండి, సరైన సమాచారం కనుగొనలేకపోయాను. దయచేసి మరో విధంగా అడగండి.",
         
         "chatbot_title": "అగ్రి అసిస్ట్",
         "chatbot_caption": "AI ఆధారిత పంట వ్యాధి సలహా సహాయకుడు",
         "chatbot_welcome": "హలో! నేను అగ్రి అసిస్ట్ 🌿\n\nపంటలు, వ్యాధులు, ఎరువులు, నేల, వాతావరణం లేదా పథకాల గురించి అడగండి.",
         "chat_input_placeholder": "పంటలు, వ్యాధులు, ఎరువుల గురించి అడగండి...",
         "back_button": "⬅ గుర్తింపు వద్దకు తిరిగి వెళ్ళండి",
         
         "status_online": "ఆన్‌లైన్",
         "status_thinking": "ఆలోచిస్తోంది...",
         "typing_message": "అగ్రి అసిస్ట్ టైప్ చేస్తోంది",
         "suggested_questions": "సూచించిన ప్రశ్నలు",
         "detected_disease": "గుర్తించిన వ్యాధి",
         "suggest_tomato_fertilizer": "టమాటాకు ఎరువు సలహా",
         "suggest_tomato_season": "టమాటా సీజనల్ సమాచారం",
         "suggest_tomato_prevention": "టమాటా నివారణ పద్ధతులు",
         "suggest_rice_fertilizer": "వరి కోసం ఎరువు సలహా",
         "suggest_rice_season": "వరి సీజనల్ సమాచారం",
         "suggest_rice_prevention": "వరి నివారణ పద్ధతులు",
         "suggest_wheat_fertilizer": "గోధుమకు ఎరువు సిఫార్సు",
         "suggest_wheat_season": "గోధుమ సీజనల్ సలహా",
         "suggest_insurance": "పంట బీమా వివరాలు",
         "suggest_soil_card": "మట్టి ఆరోగ్య కార్డు పథకం",
         "suggest_general_prevention": "సాధారణ నివారణ పద్ధతులు",
         "suggest_maize_fertilizer": "మొక్కజొన్నకు ఎరువు సలహా",
         "suggest_weather_cotton": "పత్తి కోసం వాతావరణ సలహా",
         "no_response_fallback": "క్షమించండి, సరైన సమాచారం కనుగొనలేకపోయాను. దయచేసి మరో విధంగా అడగండి.",
         "voice_title": "అగ్రివిజన్ AI వాయిస్ అసిస్టెంట్",
         "voice_instruction": "మైక్‌ను నొక్కి సహజంగా మాట్లాడండి",
         "mic_start": "🎤 మాట్లాడండి",
         "mic_stop": "⏹ పూర్తైంది",
         "processing_message": "మీ అభ్యర్థనను ప్రాసెస్ చేస్తున్నాము...",
         "voice_not_understood": "క్షమించండి, నేను అర్థం చేసుకోలేకపోయాను. మళ్లీ ప్రయత్నించండి.",
         "you_label": "మీరు",
         "assistant_label": "సహాయకుడు",
         "risk_level": "ప్రమాద స్థాయి",
         "broken clouds": "చిన్న మేఘాలు",
         "clear sky": "స్పష్టమైన ఆకాశం",
         "few clouds": "కొన్ని మేఘాలు",
         "scattered clouds": "చెల్లాచెదురైన మేఘాలు",
         "overcast clouds": "మేఘావృతం",
         
         "low": "తక్కువ ప్రమాదం",
         "medium": "మధ్యస్థ ప్రమాదం",
         "high": "అధిక ప్రమాదం",
    },

    # ==================================================
    # HINDI
    # ==================================================
    "Hindi": {

        "app_name": "एग्रीविज़न AI",
        "tagline": "एआई आधारित फसल स्वास्थ्य सहायक",
        "language": "भाषा",
        "help_faq": "सहायता (FAQ)",

        "faq_image_q": "स्पष्ट पत्ते की तस्वीर कैसे लें?",
        "faq_image_a": (
            "- अच्छी प्राकृतिक रोशनी में तस्वीर लें।\n"
            "- केवल एक पत्ते पर ध्यान दें।\n"
            "- धुंधलापन न हो।"
        ),

        "faq_crops_q": "कौन सी फसलें समर्थित हैं?",
        "faq_crops_a": (
            "यह प्रणाली वर्तमान में निम्नलिखित फसलों का समर्थन करती है:\n"
            "- धान\n- गेहूं\n- कपास\n- मिर्च\n- टमाटर\n- आलू\n- मक्का"
        ),

        "faq_confidence_q": "यदि पूर्वानुमान विश्वास स्तर कम हो तो क्या करें?",
        "faq_confidence_a": (
            "उचित रोशनी और फोकस के साथ स्पष्ट तस्वीर लें।\n"
            "यदि विश्वास स्तर फिर भी कम रहे तो स्थानीय कृषि विशेषज्ञों\n"
            "या विस्तार अधिकारियों से परामर्श लें।"
        ),

        "faq_offline_q": "क्या यह प्रणाली ऑफ़लाइन काम करती है?",
        "faq_offline_a": (
            "एप्लिकेशन चलने पर छवि विश्लेषण स्थानीय रूप से होता है।\n"
            "हालाँकि, लाइव मौसम परामर्श के लिए इंटरनेट आवश्यक है।"
        ),

        "faq_accuracy_q": "क्या यह प्रणाली 100% सटीक है?",
        "faq_accuracy_a": (
            "कोई भी एआई आधारित प्रणाली 100% सटीकता की गारंटी नहीं देती।\n"
            "यह उपकरण केवल मार्गदर्शन हेतु है।"
        ),

        "faq_after_detect_q": "रोग पहचान के बाद क्या करना चाहिए?",
        "faq_after_detect_a": (
            "- प्रणाली द्वारा सुझाए गए उपचार अपनाएँ\n"
            "- फसल की स्थिति की नियमित निगरानी करें\n"
            "- अत्यधिक सिंचाई या उर्वरक उपयोग से बचें\n"
            "- समस्या बनी रहने पर कृषि विशेषज्ञों से संपर्क करें"
        ),
        
        # -------- Help Center Extra --------
        "help_center_title": "सहायता केंद्र",
        "general_help": "सामान्य सहायता",
        "chatbot_help": "AgriAssist (चैटबॉट)",
        "voice_help": "वॉइस असिस्टेंट",

        "chatbot_use_q": "मैं चैटबॉट का उपयोग कैसे करूं?",
        "chatbot_use_a": "AgriAssist पर क्लिक करें और अपना प्रश्न टाइप करें। यह बहुभाषी फसल मार्गदर्शन और उपचार प्रदान करता है।",

        "chatbot_type_q": "मैं किस प्रकार के प्रश्न पूछ सकता/सकती हूँ?",
        "chatbot_type_a": "आप रोग के लक्षण, उपचार, रोकथाम, मौसम परामर्श और खेती संबंधी मार्गदर्शन के बारे में पूछ सकते हैं।",

        "chatbot_lang_q": "क्या चैटबॉट कई भाषाओं का समर्थन करता है?",
        "chatbot_lang_a": "हाँ। साइडबार ड्रॉपडाउन से अपनी पसंदीदा भाषा चुनें।",

        "voice_work_q": "वॉइस असिस्टेंट कैसे काम करता है?",
        "voice_work_a": "Voice Assist पर क्लिक करें, Speak दबाएं और स्वाभाविक रूप से अपना प्रश्न पूछें। सिस्टम आपकी आवाज़ को टेक्स्ट में बदलकर वॉइस आउटपुट के साथ उत्तर देता है।",

        "voice_delay_q": "वॉइस प्रोसेसिंग में कुछ सेकंड क्यों लगते हैं?",
        "voice_delay_a": "स्पीच पहचान और एआई प्रतिक्रिया निर्माण में सिस्टम प्रदर्शन के अनुसार समय लगता है।",

        "voice_switch_q": "क्या मैं चैटबॉट और वॉइस के बीच बदल सकता/सकती हूँ?",
        "voice_switch_a": "हाँ। आप पेज के नीचे दिए गए बटनों का उपयोग करके कभी भी बदल सकते हैं।",

        "contact_support": "सहायता से संपर्क करें",
        "contact_expand": "सहायता चाहिए? हमसे संपर्क करें",
        "contact_text": (
            "यदि आपको निम्न में से कोई समस्या होती है:\n"
            "- गलत रोग पूर्वानुमान\n"
            "- वॉइस असिस्टेंट प्रतिक्रिया नहीं दे रहा\n"
            "- मौसम परामर्श लोड नहीं हो रहा\n"
            "- तकनीकी त्रुटियाँ या अप्रत्याशित व्यवहार\n\n"
            "कृपया सहायता टीम से संपर्क करें।\n\n"
            "ईमेल: agrivision.support@example.com\n"
            "प्रतिक्रिया समय: 24–48 घंटों के भीतर\n\n"
            "यह एप्लिकेशन शैक्षणिक और प्रदर्शन उद्देश्यों के लिए विकसित किया गया है।\n"
            "आपकी प्रतिक्रिया प्रणाली की सटीकता और प्रदर्शन को बेहतर बनाने में मदद करती है।"
        ),

        "feedback_title": "प्रतिक्रिया",
        "feedback_expand": "अपनी प्रतिक्रिया साझा करें",
        "rate_experience": "अपने अनुभव को रेट करें",
        "your_comments": "आपके सुझाव या टिप्पणियाँ",
        "submit_feedback": "प्रतिक्रिया जमा करें",
        "thank_feedback": "आपकी प्रतिक्रिया के लिए धन्यवाद!",

        # -------- Important Notice --------
        "important_notice": "महत्वपूर्ण सूचना",
        "disclaimer_text": (
            "यह प्रणाली केवल एआई आधारित मार्गदर्शन प्रदान करती है।\n"
            "छवि गुणवत्ता, प्रकाश व्यवस्था और पर्यावरणीय कारकों के कारण\n"
            "पूर्वानुमान में अंतर हो सकता है।\n\n"
            "सटीक निदान और उपचार के लिए किसानों को स्थानीय कृषि विशेषज्ञों,\n"
            "विस्तार अधिकारियों या पौध रोग विशेषज्ञों से परामर्श करना चाहिए।"
        ),

        "footer_line1": "एग्रीविज़न AI – अंतिम वर्ष शैक्षणिक परियोजना",
        "footer_line2": "एआई आधारित फसल रोग पहचान एवं बहुभाषी कृषि सहायक",
        "footer_line3": "केवल शैक्षणिक और मार्गदर्शन प्रदर्शन उद्देश्यों हेतु",

        # -------- Results / Prediction --------
        "result_disease_detected": "रोग पहचाना गया",
        "result_prediction_confidence": "पूर्वानुमान विश्वास स्तर",
        "result_disease_info": "रोग जानकारी",
        "result_crop": "फसल",
        "result_symptoms": "लक्षण",
        "result_general_advice": "सामान्य सलाह",
        "result_weather_advisory": "मौसम परामर्श",
        "result_recommended_advisory": "अनुशंसित उपचार",
        "result_remedy_unavailable": "चयनित भाषा में उपचार जानकारी उपलब्ध नहीं है।",
        "humidity_high": (
            "उच्च आर्द्रता पाई गई है। फफूंद रोगों का खतरा बढ़ जाता है। "
            "ऊपर से सिंचाई से बचें और फसल की नियमित निगरानी करें।"
        ),
        "humidity_low": (
            "कम आर्द्रता पाई गई है। पर्याप्त सिंचाई सुनिश्चित करें और "
            "नमी की कमी के लक्षणों पर ध्यान दें।"
        ),
        
        "main_title": "फसल रोग पहचान एवं सलाह",
        "main_subtitle": "पत्ते की तस्वीर लेकर AI आधारित निदान और मार्गदर्शन प्राप्त करें।",
        
        "use_camera": "कैमरा उपयोग करें",
        "upload_image": "छवि अपलोड करें",
        "capture_leaf": "पत्ते की तस्वीर लें",
        "upload_leaf": "पत्ते की तस्वीर अपलोड करें",
        
        "retake_camera": "फिर से फोटो लें",
        "reupload_image": "फिर से अपलोड करें",
        "analyze_crop": "फसल का विश्लेषण करें",
        
        "camera_error": "⚠️ कैमरा उपलब्ध नहीं है। अनुमति दें।",
        
        "rating_excellent": "उत्कृष्ट",
        "rating_good": "अच्छा",
        "rating_average": "सामान्य",
        "rating_improve": "सुधार आवश्यक",
        "optional_placeholder": "वैकल्पिक सुझाव...",
        
        "invalid_leaf": "⚠ यह छवि सही फसल पत्ती नहीं है। कृपया स्पष्ट छवि अपलोड करें।",
        "unsupported_crop": "⚠ यह छवि समर्थित फसल की नहीं हो सकती है।",
        
        "diagnosis_summary": "AI निदान सारांश",
        "predicted_condition": "अनुमानित स्थिति",
        "model_confidence": "मॉडल विश्वास स्तर",
        "model": "मॉडल",
        "input_size": "इनपुट आकार",
        "inference_time": "प्रसंस्करण समय",
        "generated": "उत्पन्न समय",
        
        "crop_health": "फसल स्वास्थ्य स्थिति",
        "healthy_msg": "पत्ता स्वस्थ है। कोई रोग नहीं पाया गया।",
        "disease_analysis": "रोग विश्लेषण",
        "crop_label": "फसल",
        "symptoms_label": "लक्षण",
        "actions_label": "अनुशंसित कार्य",
        "no_info": "इस रोग के लिए जानकारी उपलब्ध नहीं है।",
        
        "treatment": "उपचार और समाधान",
        "no_remedy": "उपचार जानकारी उपलब्ध नहीं है।",
        
        "ai_insight": "AI विस्तृत विश्लेषण",
        "get_insight": "AI विश्लेषण प्राप्त करें",
        "generating": "AI विश्लेषण तैयार हो रहा है...",
        "analyzing": "छवि का विश्लेषण हो रहा है...",
        
        "weather_title": "मौसम विवरण",
        "weather_not_configured": "मौसम सेवा कॉन्फ़िगर नहीं है।",
        "location": "स्थान",
        "temperature": "तापमान",
        "humidity": "आर्द्रता",
        "condition": "स्थिति",
        "weather_fetch_error": "मौसम डेटा प्राप्त नहीं हो सका।",
        
        "agri_assist": "AgriAssist",
        "voice_assist": "वॉइस असिस्टेंट",
        
        "app_name": "एग्रीविजन AI",
        "app_description": "AI आधारित फसल रोग अनुसंधान और सलाह प्रणाली",
        
        "capture_image": "छवि कैप्चर करें",
        "image_captured_success": "छवि सफलतापूर्वक कैप्चर हुई ✓",
        "processing_stopped": "प्रक्रिया रोक दी गई",
        
        "humidity_risk": "उच्च आर्द्रता फंगल रोगों के जोखिम को बढ़ाती है। नियमित खेत निरीक्षण करें।",
        "heavy_rainfall": "भारी वर्षा का पता चला है। अधिक सिंचाई से बचें और उचित जल निकासी सुनिश्चित करें।",
        "heat_stress": "उच्च तापमान से फसल पर तनाव हो सकता है। पर्याप्त सिंचाई सुनिश्चित करें।",
        "wheat_rust_risk": "उच्च आर्द्रता में गेहूं में रस्ट रोग का खतरा बढ़ता है। निवारक फफूंदनाशक का उपयोग करें।",
        "rice_lodging_risk": "धान में अधिक वर्षा से पौधे गिर सकते हैं। जल स्तर पर नजर रखें।",
        "favorable_weather": "वर्तमान मौसम फसल वृद्धि के लिए अनुकूल है।",
        
        "high_risk": "उच्च जोखिम",
        "moderate_risk": "मध्यम जोखिम",
        "low_risk": "कम जोखिम",
        
        "weather_api_missing": "मौसम सेवा कॉन्फ़िगर नहीं है। कृपया बाद में प्रयास करें।",
        
        "no_response_fallback": "माफ़ कीजिए, मुझे उपयुक्त जानकारी नहीं मिली। कृपया प्रश्न बदलकर पूछें।",
        
        "chatbot_title": "एग्री असिस्ट",
        "chatbot_caption": "AI आधारित फसल रोग सलाह सहायक",
        "chatbot_welcome": "नमस्ते! मैं एग्री असिस्ट हूँ 🌿\n\nफसलों, रोगों, उर्वरकों, मिट्टी, मौसम या योजनाओं के बारे में पूछें।",
        "chat_input_placeholder": "फसल, रोग या उर्वरक के बारे में पूछें...",
        "back_button": "⬅ पहचान पर वापस जाएँ",
        "status_online": "ऑनलाइन",
        "status_thinking": "सोच रहा है...",
        "typing_message": "एग्री असिस्ट टाइप कर रहा है",
        "suggested_questions": "सुझाए गए प्रश्न",
        "detected_disease": "पहचानी गई बीमारी",
        "suggest_tomato_fertilizer": "टमाटर के लिए उर्वरक सलाह",
        "suggest_tomato_season": "टमाटर की मौसमी जानकारी",
        "suggest_tomato_prevention": "टमाटर की रोकथाम के तरीके",
        "suggest_rice_fertilizer": "चावल के लिए उर्वरक सलाह",
        "suggest_rice_season": "चावल की मौसमी जानकारी",
        "suggest_rice_prevention": "चावल की रोकथाम के तरीके",
        "suggest_wheat_fertilizer": "गेहूं के लिए उर्वरक सिफारिश",
        "suggest_wheat_season": "गेहूं की मौसमी सलाह",
        "suggest_insurance": "फसल बीमा विवरण",
        "suggest_soil_card": "मिट्टी स्वास्थ्य कार्ड योजना",
        "suggest_general_prevention": "सामान्य रोकथाम उपाय",
        "suggest_maize_fertilizer": "मक्का के लिए उर्वरक सलाह",
        "suggest_weather_cotton": "कपास के लिए मौसम सलाह",
        "no_response_fallback": "क्षमा करें, मुझे उपयुक्त जानकारी नहीं मिली। कृपया प्रश्न को दोबारा पूछें।",
        "voice_title": "एग्रीविजन AI वॉयस असिस्टेंट",
        "voice_instruction": "माइक दबाएँ और सामान्य रूप से बोलें",
        "mic_start": "🎤 बोलें",
        "mic_stop": "⏹ समाप्त",
        "processing_message": "आपका अनुरोध प्रोसेस किया जा रहा है...",
        "voice_not_understood": "माफ़ कीजिए, मैं समझ नहीं पाया। कृपया फिर से कोशिश करें।",
        "you_label": "आप",
        "assistant_label": "सहायक",
        "risk_level": "जोखिम स्तर",
        "broken clouds": "टूटे हुए बादल",
        "clear sky": "साफ आसमान",
        "few clouds": "कुछ बादल",
        "scattered clouds": "बिखरे बादल",
        "overcast clouds": "घने बादल",
        
        "low": "कम जोखिम",
        "medium": "मध्यम जोखिम",
        "high": "उच्च जोखिम",
     }
}

def t(lang: str, key: str) -> str:
    """
    Translation helper with safe fallback.
    """
    if lang not in LANG:
        lang = "English"
    return LANG.get(lang, {}).get(key, LANG["English"].get(key, key))
