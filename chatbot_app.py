import streamlit as st
import openai
import os

# Set your OpenAI API Key securely
openai.api_key = st.secrets["OPENAI_API_KEY"] if "OPENAI_API_KEY" in st.secrets else os.getenv("OPENAI_API_KEY")

# App title
st.set_page_config(page_title="AI Chatbot", page_icon="🤖")
st.title("🤖 Intelligent AI Chatbot")
st.markdown("Ask anything and get smart AI-powered answers using GPT!")

# Session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Input area
user_input = st.text_input("You:", placeholder="Ask me anything...", key="input")

# Function to get OpenAI response
def get_gpt_response(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",  # or "gpt-3.5-turbo"
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                *st.session_state.messages,
                {"role": "user", "content": prompt}
            ],
            max_tokens=500,
            temperature=0.7
        )
        return response.choices[0].message["content"].strip()
    except Exception as e:
        return f"⚠️ Error: {e}"

# Process user input
if user_input:
    # Save user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Get response
    bot_response = get_gpt_response(user_input)
    st.session_state.messages.append({"role": "assistant", "content": bot_response})

# Show conversation
st.markdown("### 💬 Conversation:")
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"**You:** {msg['content']}")
    elif msg["role"] == "assistant":
        st.markdown(f"**Bot:** {msg['content']}")
