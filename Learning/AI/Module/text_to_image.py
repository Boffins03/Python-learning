from models import image_generate,setup_openai
import streamlit as st
from apikey import apikey

client = setup_openai(apikey)
st.title("Image Generating using openai")
prompt = st.text_input("Enter your prompt")

if st.button("Image Generate"):
    with st.spinner("Image generating"):
        image=image_generate(client,prompt)
        image.show()
        