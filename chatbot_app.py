import streamlit as st
from transformers import pipeline
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Load local model for Q&A
qa_pipeline = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")

# Streamlit UI
st.title("🧠 Local Chatbot App (No API)")

st.write("Ask a question related to the context provided below:")

context = st.text_area("Enter context (the text from which chatbot will answer):", height=200)
question = st.text_input("Enter your question:")

if context and question:
    try:
        result = qa_pipeline(question=question, context=context)
        st.success(f"🤖 Answer: {result['answer']}")
    except Exception as e:
        st.error(f"❌ Error: {str(e)}")
