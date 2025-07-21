import streamlit as st
from transformers import pipeline, set_seed
from collections import deque
from datetime import datetime
import time

# —————————————————————————————————————————
# 🚀 Streamlit App Setup
# —————————————————————————————————————————
st.set_page_config(page_title="🌐 Smart Chatbot", layout="wide")
st.title("🌍 Intelligent Chatbot with Memory & Context")
st.markdown("""
A conversational AI inspired by your Colab chatbot.
Features context memory, creativity controls, simulated web responses.
""")

# —————————————————————————————————————————
# ⚙️ Sidebar Configuration
# —————————————————————————————————————————
with st.sidebar:
    st.header("⚙️ Settings")
    model_name = st.selectbox("Model:", ["distilgpt2", "gpt2"])
    seed = st.slider("Random seed", 0, 9999, 1234)
    max_len = st.slider("Max response length", 50, 300, 150)
    temp = st.slider("Temperature (creativity)", 0.1, 1.0, 0.7, step=0.05)
    top_p = st.slider("Top-p (nucleus sampling)", 0.1, 1.0, 0.9, step=0.05)

# —————————————————————————————————————————
# 🔐 Model Initialization (lazy-load)
# —————————————————————————————————————————
@st.cache_resource(show_spinner=False)
def load_model():
    set_seed(seed)
    return pipeline("text-generation", model=model_name)

gen = load_model()

# —————————————————————————————————————————
# 🧠 Conversation Memory (deque)
# —————————————————————————————————————————
if "memory" not in st.session_state:
    st.session_state.memory = deque(maxlen=6)

def memorize(user, bot):
    st.session_state.memory.append({"user": user, "bot": bot})

# —————————————————————————————————————————
# 📝 Input & Web Lookup Simulation
# —————————————————————————————————————————
def web_lookup(prompt):
    t = datetime.now().strftime("%H:%M:%S")
    return f"🌐 [Simulated lookup at {t}]: Sorry, I can't browse the web yet!"

user_input = st.text_input("You:", placeholder="Ask anything...")

if st.button("Send") and user_input.strip():
    # Add memory and generate response
    context = "\n".join(
        f"User: {m['user']}\nBot: {m['bot']}" for m in st.session_state.memory
    )
    prompt = f"{context}\nUser: {user_input}\nBot:"
    raw = gen(prompt, max_length=len(prompt.split()) + max_len,
              temperature=temp, top_p=top_p)[0]["generated_text"]
    reply = raw.split("Bot:")[-1].strip().split("\n")[0]  # clean

    # Optionally simulate web lookup for "when", "who", "what is" questions
    if any(token in user_input.lower() for token in ["who", "what", "when", "where", "why"]):
        reply += "\n\n" + web_lookup(user_input)

    memorize(user_input, reply)

# —————————————————————————————————————————
# 💬 Display Conversation
# —————————————————————————————————————————
st.subheader("💬 Conversation:")
for entry in st.session_state.memory:
    st.markdown(f"**You:** {entry['user']}")
    st.markdown(f"**Bot:** {entry['bot']}")

# —————————————————————————————————————————
# ℹ️ Usage Instructions & Notes
# —————————————————————————————————————————
st.markdown("""
---
### ℹ️ Notes

- The bot uses Hugging Face GPT models — adjust creativity in sidebar.
- Conversation memory retains last 6 exchanges.
- Web-lookup responses are **simulated** — real browsing would need external API.
""")
