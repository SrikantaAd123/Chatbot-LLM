import streamlit as st
from transformers import pipeline
import torch

# Initialize chatbot pipeline
chatbot = pipeline("text-generation", model="distilgpt2")

st.set_page_config(page_title="🤖 Chatbot with HuggingFace Transformers")
st.title("🤖 Chatbot with HuggingFace Transformers")

# User input
user_input = st.text_input("You:", placeholder="Ask me anything...")

# Generate response
if user_input:
    with st.spinner("Bot is typing..."):
        response = chatbot(user_input, max_length=100, do_sample=True, top_k=50, top_p=0.95, temperature=0.9)
        generated_text = response[0]['generated_text']

        # Clean the response
        cleaned_response = generated_text[len(user_input):].strip().split(".")[0] + "."
        
        st.text_area("Bot:", value=cleaned_response, height=200)

# Add instructions/info
st.markdown("""
---
**Instructions:** Type your query above and press Enter. The bot will respond using a small, efficient transformer model.

Model: `distilgpt2` | Max tokens: 100 | Top-p sampling for creative output
""")
