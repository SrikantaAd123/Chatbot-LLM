# 🤖 Chatbot-LLM

A simple chatbot built using Hugging Face LLMs and deployed via Streamlit. This project demonstrates how to integrate a Large Language Model (LLM) with an interactive web interface using Python. It supports conversation through GPT-Neo or OpenAI API (based on configuration).

---

## 👨‍💻 Created By

**Srikanta Vai Sravan**  
AI Developer – Launched Global AI Internship

---

## 🧠 Model Used

- `EleutherAI/gpt-neo-1.3B` (via Hugging Face Transformers)
- Optional: OpenAI GPT models (if configured using OpenAI API)

---

## 📦 Setup Instructions

Make sure you have Python ≥ 3.8 installed.

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/chatbot-llm.git
cd chatbot-llm
pip install -r requirements.txt
pip install streamlit transformers torch
pip install openai
export OPENAI_API_KEY=" sk-https://platform.openai.com/account/api-keys"

openai migrate
pip install openai==0.28
