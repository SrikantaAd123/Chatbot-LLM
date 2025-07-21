import os
import openai
import streamlit as st
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Set OpenAI API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

# Set up Streamlit page
st.set_page_config(page_title="LLM Chatbot App")
st.title("🤖 AI Chatbot using OpenAI GPT-3.5")

# User input
prompt = st.text_area("📝 Enter your question:", height=150)

if st.button("💬 Generate Response"):
    if not prompt.strip():
        st.warning("⚠️ Please enter a prompt/question.")
    else:
        with st.spinner("🧠 Generating response..."):
            try:
                # Call OpenAI API
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
