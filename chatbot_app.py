# chatbot_app.py

import os
import openai
import streamlit as st
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Streamlit page settings
st.set_page_config(page_title="LLM Chatbot App")
st.title("🤖 AI Chatbot using OpenAI GPT-3.5")

# Prompt input
prompt = st.text_area("📝 Enter your question:", height=150)

# Generate response
if st.button("💬 Generate Response"):
    if not prompt.strip():
        st.warning("Please enter a prompt/question.")
    else:
        with st.spinner("Generating response..."):
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant."},
                        {"role": "user", "content": prompt}
                    ]
                )
                reply = response['choices'][0]['message']['content']
                st.success("✅ Response Generated")
                st.markdown(f"**Response:**\n\n{reply}")
            except Exception as e:
                st.error(f"❌ Error: {e}")
