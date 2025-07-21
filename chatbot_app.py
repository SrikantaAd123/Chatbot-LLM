import streamlit as st
from transformers import pipeline

st.title("🧠 Mini AI Chatbot")

try:
    chatbot = pipeline("text-generation", model="distilgpt2")
except Exception as e:
    st.error(f"Error loading model: {e}")
    st.stop()

user_input = st.text_input("Ask something:")
if user_input:
    try:
        response = chatbot(user_input, max_length=50, do_sample=True)[0]['generated_text']
        st.text_area("Bot says:", response)
    except Exception as e:
        st.error(f"Error generating response: {e}")
