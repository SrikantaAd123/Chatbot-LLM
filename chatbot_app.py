import streamlit as st
from transformers import pipeline
import torch  # ✅ Import torch to fix error

st.title("🤖 Chat with AI - LLM")
chatbot = pipeline("text-generation", model="sshleifer/tiny-gpt2")


user_input = st.text_input("You:", placeholder="Ask me anything!")

if st.button("Send"):
    with st.spinner("Thinking..."):
        response = chatbot(user_input, max_length=50, do_sample=True)[0]['generated_text']
        st.text_area("Bot:", response)
