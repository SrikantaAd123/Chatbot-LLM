import streamlit as st
from transformers import pipeline

st.title("🤖 AI Chatbot")
chatbot = pipeline("text-generation", model="distilgpt2")


user_input = st.text_input("You:")
if user_input:
    result = chatbot(user_input, max_length=50, do_sample=True)
    st.text_area("Bot says:", result[0]['generated_text'])
