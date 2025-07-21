import openai
import os
from dotenv import load_dotenv

load_dotenv()  # load variables from .env

openai.api_key = os.getenv("OPENAI_API_KEY")

# Function to get GPT response
def ask_gpt(prompt, chat_history):
    messages = chat_history + [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # or gpt-4
        messages=messages,
        temperature=0.7,
        max_tokens=300,
    )
    answer = response.choices[0].message["content"]
    chat_history.append({"role": "assistant", "content": answer})
    return answer, chat_history

# Streamlit UI
st.title("🧠 Chatbot App")
if "history" not in st.session_state:
    st.session_state.history = [{"role": "system", "content": "You are a helpful assistant."}]

user_input = st.text_input("You:", "")

if user_input:
    response, st.session_state.history = ask_gpt(user_input, st.session_state.history)
    st.markdown(f"**Bot:** {response}")
