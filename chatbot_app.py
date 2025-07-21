# chatbot_app.py

import os
import openai
import streamlit as st
from transformers import AutoModelForCausalLM, AutoTokenizer
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set OpenAI API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

# Title
st.set_page_config(page_title="LLM Chatbot App")
st.title("🤖 AI Chatbot using GPT-Neo and OpenAI")

# Sidebar toggle
model_choice = st.sidebar.selectbox("Choose a model", ("GPT-Neo", "OpenAI GPT-3.5"))

# Input box
prompt = st.text_area("📝 Enter your question:", height=150)

if st.button("💬 Generate Response"):
    if not prompt.strip():
        st.warning("Please enter a prompt/question.")
    else:
        with st.spinner("Generating response..."):
            if model_choice == "GPT-Neo":
                # Load GPT-Neo
                tokenizer = AutoTokenizer.from_pretrained("EleutherAI/gpt-neo-1.3B")
                model = AutoModelForCausalLM.from_pretrained("EleutherAI/gpt-neo-1.3B")
                inputs = tokenizer(prompt, return_tensors="pt")
                outputs = model.generate(**inputs, max_length=150, do_sample=True)
                response = tokenizer.decode(outputs[0], skip_special_tokens=True)
                st.success("✅ Response Generated")
                st.markdown(f"**Response:**\n
{response}")

            elif model_choice == "OpenAI GPT-3.5":
                try:
                    response = openai.ChatCompletion.create(
                        model="gpt-3.5-turbo",
                        messages=[
                            {"role": "system", "content": "You are a helpful assistant."},
                            {"role": "user", "content": prompt},
                        ]
                    )
                    reply = response['choices'][0]['message']['content']
                    st.success("✅ Response Generated")
                    st.markdown(f"**Response:**\n
{reply}")
                except Exception as e:
                    st.error(f"❌ Error: {e}")
