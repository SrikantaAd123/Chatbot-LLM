import streamlit as st
from transformers import pipeline

# Title of the app
st.title("🤖 Chatbot with HuggingFace Transformers")

# Create chatbot pipeline using a pre-trained model
chatbot = pipeline("text-generation", model="microsoft/DialoGPT-medium")

# Input from user
user_input = st.text_input("You: ", "")

if user_input:
    # Generate response from chatbot
    response = chatbot(user_input, max_length=1000, pad_token_id=50256)[0]['generated_text']
    st.text_area("Bot:", value=response, height=200)
