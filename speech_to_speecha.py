import streamlit as st
from deep_translator import GoogleTranslator
import edge_tts
import asyncio
import tempfile
import base64
import streamlit as st

with open("Rlogo.png", "rb") as f:
    data = base64.b64encode(f.read()).decode()

st.markdown(
    f"""
    <div style="display:flex; align-items:center;">
        <img src="data:image/png;base64,{data}" width="100">
        <h1 style="margin-left:25px;">
            Rvoice - GulfTalk Translator
        </h1>
    </div>
    """,
    unsafe_allow_html=True
)

st.write("Founder & CEO - Raj Gupta")

# Language Selection
input_lang = st.selectbox(
    "Select Input Language",
    ["Hindi", "Arabic"]
)

# Voice Selection
voice_type = st.selectbox(
    "Select Voice",
    ["Male", "Female"]
)

# Text Input
user_text = st.text_area(
    "Enter Text",
    height=150
)

# Voice Mapping
voices = {
    "English": {
        "Male": "en-US-GuyNeural",
        "Female": "en-US-JennyNeural"
    },
    "Arabic": {
        "Male": "ar-SA-HamedNeural",
        "Female": "ar-SA-ZariyahNeural"
    },
    "Hindi": {
        "Male": "hi-IN-MadhurNeural",
        "Female": "hi-IN-SwaraNeural"
    }
}

async def create_audio(text, voice):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
        path = fp.name

    communicate = edge_tts.Communicate(text=text, voice=voice)
    await communicate.save(path)

    with open(path, "rb") as f:
        audio_data = f.read()

    return audio_data

if st.button(" Convert & Translate"):

    if not user_text.strip():
        st.warning("Please enter text")
        st.stop()

    try:

        if input_lang == "Hindi":

            english_text = GoogleTranslator(
                source="hi",
                target="en"
            ).translate(user_text)

            arabic_text = GoogleTranslator(
                source="en",
                target="ar"
            ).translate(english_text)

            st.subheader("🇬🇧 English Translation")
            st.success(english_text)

            en_audio = asyncio.run(
                create_audio(
                    english_text,
                    voices["English"][voice_type]
                )
            )

            st.audio(en_audio)
            st.download_button(
                "⬇ Download English MP3",
                en_audio,
                "english.mp3",
                "audio/mp3"
            )

            st.subheader("🇸🇦 Arabic Translation")
            st.success(arabic_text)

            ar_audio = asyncio.run(
                create_audio(
                    arabic_text,
                    voices["Arabic"][voice_type]
                )
            )

            st.audio(ar_audio)
            st.download_button(
                "⬇ Download Arabic MP3",
                ar_audio,
                "arabic.mp3",
                "audio/mp3"
            )

        else:

            english_text = GoogleTranslator(
                source="ar",
                target="en"
            ).translate(user_text)

            hindi_text = GoogleTranslator(
                source="en",
                target="hi"
            ).translate(english_text)

            st.subheader("🇬🇧 English Translation")
            st.success(english_text)

            en_audio = asyncio.run(
                create_audio(
                    english_text,
                    voices["English"][voice_type]
                )
            )

            st.audio(en_audio)
            st.download_button(
                "⬇ Download English MP3",
                en_audio,
                "english.mp3",
                "audio/mp3"
            )

            st.subheader("🇮🇳 Hindi Translation")
            st.success(hindi_text)

            hi_audio = asyncio.run(
                create_audio(
                    hindi_text,
                    voices["Hindi"][voice_type]
                )
            )

            st.audio(hi_audio)
            st.download_button(
                "⬇ Download Hindi MP3",
                hi_audio,
                "hindi.mp3",
                "audio/mp3"
            )

    except Exception as e:
        st.error(f"Error: {e}")
