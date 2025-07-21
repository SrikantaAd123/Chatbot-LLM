import streamlit as st
import openai
import os

# Set your OpenAI API key here or use secrets/environment variables
openai.api_key = os.getenv("OPENAI_API_KEY") or "your-api-key-here"

# Initialize OpenAI client (for v1.x)
client = openai.OpenAI()

st.set_page_config(page_title="AI Chatbot", layout="centered")
st.title("🤖 AI Chatbot with OpenAI & Streamlit")

# Initialize session
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]

# User input
user_input = st.text_input("You:", key="input")

if st.button("Send") and user_input:
    # Add user input to chat history
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Call OpenAI API (v1.x syntax)
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=st.session_state.messages
        )
        reply = response.choices[0].message.content

        # Add bot reply to history
        st.session_state.messages.append({"role": "assistant", "content": reply})
    except Exception as e:
        st.error(f"⚠️ Error: {e}")

# Display conversation
for msg in st.session_state.messages[1:]:
    if msg["role"] == "user":
        st.markdown(f"**You:** {msg['content']}")
    else:
        st.markdown(f"**Bot:** {msg['content']}")
