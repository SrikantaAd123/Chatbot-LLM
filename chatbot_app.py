
### ✅ `chatbot_app.py`
```python
import streamlit as st
from transformers import pipeline

st.title("🤖 Chat with AI - LLM")
chatbot = pipeline("text-generation", model="EleutherAI/gpt-neo-1.3B")

user_input = st.text_input("You:", placeholder="Ask me anything!")

if st.button("Send"):
    with st.spinner("Thinking..."):
        response = chatbot(user_input, max_length=50, do_sample=True)[0]['generated_text']
        st.text_area("Bot:", response)
