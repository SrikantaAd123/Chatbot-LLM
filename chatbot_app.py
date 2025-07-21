import streamlit as st
from transformers import pipeline

st.title("🧠 Mini AI Chatbot")

# Use a lightweight, compatible model
chatbot = pipeline("text-generation", model="distilgpt2")

user_input = st.text_input("Ask something:")
if user_input:
    response = chatbot(user_input, max_length=50, do_sample=True)[0]['generated_text']
    st.text_area("Bot says:", response)
