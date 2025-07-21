import streamlit as st
import openai
from dotenv import load_dotenv
import os


load_dotenv()  # ✅ Load environment variables from .env
openai.api_key = os.getenv("OPENAI_API_KEY")



st.set_page_config(page_title="AI Chatbot", layout="centered")
st.title("🤖 AI Chatbot with OpenAI & Streamlit")

# Session message history
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]

# Text input
user_input = st.text_input("You:", key="input")

if st.button("Send") and user_input:
    # Add user message
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Call OpenAI API
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=st.session_state.messages
        )
        reply = response.choices[0].message.content.strip()

        # Add assistant reply
        st.session_state.messages.append({"role": "assistant", "content": reply})

    except Exception as e:
        st.error(f"⚠️ Error: {e}")

# Display full conversation
for msg in st.session_state.messages[1:]:
    if msg["role"] == "user":
        st.markdown(f"**You:** {msg['content']}")
    else:
        st.markdown(f"**Bot:** {msg['content']}")
