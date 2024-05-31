from models import text_generate,setup_openai
import streamlit as st
from apikey import apikey

client = setup_openai(apikey)
st.title("Text Generating using openai")
prompt = st.text_input("Enter your prompt")
