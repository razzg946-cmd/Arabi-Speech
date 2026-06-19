import streamlit as st
from deep_translator import GoogleTranslator
from gtts import gTTS
import io

st.set_page_config(page_title="GulfTalk", page_icon="🌍", layout="centered")

st.title("Rvoice - GulfTalk Translator for Indians")
st.write("Founder - Raj Gupta")

input_lang = st.selectbox(
"Select Input Language",
["Hindi", "Arabic"]
)

user_text = st.text_area(
"Enter Text",
height=120
)

voice_type = st.selectbox(
"Voice Type (Demo Only)",
["Male", "Female"]
)

if st.button("Convert & Translate"):

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

        st.subheader("🇬🇧 English")
        st.success(english_text)

        en_audio = io.BytesIO()
        gTTS(
            text=english_text,
            lang="en"
        ).write_to_fp(en_audio)

        st.audio(en_audio.getvalue())

        st.download_button(
            "⬇ Download English MP3",
            data=en_audio.getvalue(),
            file_name="english.mp3",
            mime="audio/mp3"
        )

        st.subheader("🇸🇦 Arabic")
        st.success(arabic_text)

        ar_audio = io.BytesIO()
        gTTS(
            text=arabic_text,
            lang="ar"
        ).write_to_fp(ar_audio)

        st.audio(ar_audio.getvalue())

        st.download_button(
            "⬇ Download Arabic MP3",
            data=ar_audio.getvalue(),
            file_name="arabic.mp3",
            mime="audio/mp3"
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

        st.subheader("🇬🇧 English")
        st.success(english_text)

        en_audio = io.BytesIO()
        gTTS(
            text=english_text,
            lang="en"
        ).write_to_fp(en_audio)

        st.audio(en_audio.getvalue())

        st.download_button(
            "⬇ Download English MP3",
            data=en_audio.getvalue(),
            file_name="english.mp3",
            mime="audio/mp3"
        )

        st.subheader("🇮🇳 Hindi")
        st.success(hindi_text)

        hi_audio = io.BytesIO()
        gTTS(
            text=hindi_text,
            lang="hi"
        ).write_to_fp(hi_audio)

        st.audio(hi_audio.getvalue())

        st.download_button(
            "⬇ Download Hindi MP3",
            data=hi_audio.getvalue(),
            file_name="hindi.mp3",
            mime="audio/mp3"
        )

except Exception as e:
    st.error(f"Error: {e}")
