from models import audio_to_text,setup_openai
import streamlit as st
from apikey import apikey

client = setup_openai(apikey)
st.title("Audio to text transcribe")
audio_file = st.file_uploader("Choose the audio file",type=['mp3','mav'])

if audio_file:
    if st.button("Transcribe"):
        st.audio(audio_file,format='audio/mov')
        with st.spinner("Transcribing audio..."):
            result = audio_to_text(client,audio_file)
            st.write(result)