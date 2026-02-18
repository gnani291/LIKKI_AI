import streamlit as st
import os
from ai_brain import get_ai_response
from web_search import search_web
from tts_output import speak
import speech_recognition as sr
import requests
from PIL import Image
from io import BytesIO
from youtubesearchpython import VideosSearch
from dotenv import load_dotenv
import pytesseract

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")       
MODEL_NAME = os.getenv("MODEL_NAME")           
PIXABAY_API_KEY = os.getenv("PIXABAY_API_KEY") 

st.set_page_config(page_title="LIKKI AI Assistant", page_icon="🤖", layout="wide")
st.title("🤖 LIKKI AI Assistant")

enable_voice = st.sidebar.checkbox("Enable Voice Input", value=True)
enable_tts = st.sidebar.checkbox("Enable Voice Output", value=True)

#SESSION STATE
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "query" not in st.session_state:
    st.session_state.query = ""

# VOICE INPUT
def listen_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("🎤 Listening...")
        r.adjust_for_ambient_noise(source, duration=0.6)
        audio = r.listen(source)
    try:
        return r.recognize_google(audio)
    except:
        st.warning("❌ Could not understand audio")
        return ""

# OCR FUNCTION
def extract_text_from_image(image):
    try:
        text = pytesseract.image_to_string(image)
        return text
    except:
        return ""

# PIXABAY IMAGE SEARCH
def search_images_pixabay(query, count=9):
    url = "https://pixabay.com/api/"
    params = {
        "key": PIXABAY_API_KEY,
        "q": query,
        "image_type": "photo",
        "per_page": count
    }
    response = requests.get(url, params=params).json()
    return [img["largeImageURL"] for img in response.get("hits", [])]

# QUERY INPUT
col1, col2 = st.columns([1, 2])

with col1:
    if enable_voice and st.button("🎤 Speak"):
        query = listen_command()
        if query:
            st.session_state.query = query
            st.session_state.chat_history.append({"role": "user", "content": query})

with col2:
    with st.form(key="text_query_form"):
        text_input = st.text_input("Or type your query", value="")
        submit_button = st.form_submit_button("Send")
        if submit_button and text_input.strip():
            st.session_state.query = text_input.strip()
            st.session_state.chat_history.append({"role": "user", "content": text_input.strip()})

# PROCESS QUERY
if st.session_state.query:
    query = st.session_state.query

    # AI RESPONSE
    st.subheader("🤖 LIKKI Response")
    ai_reply = get_ai_response(query)
    st.session_state.chat_history.append({"role": "ai", "content": ai_reply})
    st.write(ai_reply)
    if enable_tts:
        speak(ai_reply)

    # WEB SERACH
    st.subheader("🔎 Web Results")
    try:
        results = search_web(query)
        if results:
            for res in results:
                st.markdown(f"**[{res['title']}]({res['link']})**")
                st.write(res["snippet"])
        else:
            st.info("No web results found")
    except Exception as e:
        st.error(f"Web Search Error: {e}")

    # PIXABAY IMAGE SEARCH
    st.subheader("🖼 Pixabay Image Results")
    try:
        images = search_images_pixabay(query)
        if images:
            cols = st.columns(3)
            for i, img_url in enumerate(images):
                cols[i % 3].image(img_url, use_column_width=True)
        else:
            st.info("No images found")
    except Exception as e:
        st.error(f"Image Search Error: {e}")

    # YOUTUBE VIDEO SEARCH
    st.subheader("🎥 Video Results")
    try:
        videos_search = VideosSearch(query, limit=5)
        videos = videos_search.result().get("result", [])
        if videos:
            for v in videos:
                st.markdown(f"[{v['title']}]({v['link']})")
        else:
            st.info("No videos found")
    except Exception as e:
        st.error(f"Video Search Error: {e}")

    # Clear query after processing
    st.session_state.query = ""

# OCR UPLOAD SECTION
st.subheader("📄 Extract Text from Your Image")
uploaded_file = st.file_uploader("Upload an image for text extraction", type=["png", "jpg", "jpeg"])
if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    extracted_text = extract_text_from_image(image)
    if extracted_text.strip():
        st.text_area("📝 Extracted Text", value=extracted_text, height=150)
    else:
        st.info("No text found in this image.")

