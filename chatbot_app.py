import streamlit as st
import openai
import os
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Streamlit UI
st.set_page_config(page_title="🧠 Chatbot App")
st.title("🧠 Chatbot App")

# Input from user
user_input = st.text_input("Ask me anything")

if user_input:
    with st.spinner("Generating response..."):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful chatbot."},
                {"role": "user", "content": user_input}
            ]
        )
        reply = response['choices'][0]['message']['content']
        st.success(reply)
