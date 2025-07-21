import streamlit as st
import os
from dotenv import load_dotenv
from openai import OpenAI

# Load your .env secrets
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

# Streamlit UI
st.set_page_config(page_title="🧠 Chatbot App")
st.title("🧠 Chatbot App")

# Input from user
user_input = st.text_input("Ask me anything")

if user_input:
    with st.spinner("Generating response..."):
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful chatbot."},
                {"role": "user", "content": user_input}
            ]
        )
        reply = response.choices[0].message.content
        st.success(reply)
