import streamlit as st
import openai
from transformers import pipeline
import os
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Hugging Face Pipeline
hf_generator = pipeline("text-generation", model="EleutherAI/gpt-neo-1.3B")

def generate_hf_response(prompt):
    result = hf_generator(prompt, max_length=100, do_sample=True, temperature=0.7)
    return result[0]['generated_text']

def generate_openai_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # You must have access to this model in your OpenAI account
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']

# Streamlit UI
st.set_page_config(page_title="LLM Chatbot", layout="centered")
st.title("🤖 LLM Chatbot")
st.markdown("Chat with Hugging Face GPT-Neo or OpenAI GPT-3.5 Turbo")

# User input
user_input = st.text_area("Enter your message:")

# Model selection
model_choice = st.selectbox("Select Model:", ["GPT-Neo (Hugging Face)", "GPT-3.5 Turbo"])

if st.button("Get Response"):
    if model_choice == "GPT-3.5 Turbo":
        try:
            response = generate_openai_response(user_input)
            st.markdown(f"""**Response:**  
{response}""")
        except Exception as e:
            st.error(f"⚠️ Error: {str(e)}")
    else:
        response = generate_hf_response(user_input)
        st.markdown(f"""**Response:**  
{response}""")
