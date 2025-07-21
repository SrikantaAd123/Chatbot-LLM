import streamlit as st
import openai

# ✅ Use OpenAI client (v1+)
client = openai.OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# UI
st.title("🧠 Chatbot App")
user_input = st.text_input("Enter your question:")

if user_input:
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_input}
            ]
        )
        st.write("🤖", response.choices[0].message.content)
    except Exception as e:
        st.error(f"❌ Error: {str(e)}")
