import streamlit as st
from transformers import pipeline

st.title("🤖 AI Chatbot (Tiny GPT)")

try:
    chatbot = pipeline("text-generation", model="sshleifer/tiny-gpt2")  # Tiny model for demo
except Exception as e:
    st.error(f"❌ Failed to load model: {e}")
    st.stop()

user_input = st.text_input("You:", placeholder="Type your message...")

if user_input:
    try:
        response = chatbot(user_input, max_length=50, do_sample=True)[0]["generated_text"]
        st.write("**Bot:**", response)
    except Exception as e:
        st.error(f"❌ Error generating response: {e}")
