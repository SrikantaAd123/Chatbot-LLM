import streamlit as st
import torch  # Required for Hugging Face pipelines
from transformers import pipeline

st.title("🧠 Mini AI Chatbot")

# Use a lightweight and supported model
chatbot = pipeline("text-generation", model="distilgpt2")

# Input field for user query
user_input = st.text_input("Ask something:")

# Generate and show response
if user_input:
    response = chatbot(user_input, max_length=50, do_sample=True)[0]['generated_text']
    st.text_area("Bot says:", response)
