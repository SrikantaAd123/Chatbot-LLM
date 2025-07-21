# 🤖 Chatbot App using OpenAI and Streamlit

A simple conversational chatbot built using OpenAI's GPT model (`gpt-3.5-turbo` or `gpt-4`) and Streamlit for the UI.

## 🔧 Features
- Chat interface with memory (session history)
- Powered by GPT via OpenAI API
- Streamlit-based frontend
- Easily deployable on Heroku or Streamlit Cloud

## 🛠️ Setup Instructions

### 1. Clone the Repository

git clone https://github.com/yourusername/chatbot-llm.git
cd chatbot-llm

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

pip install -r requirements.txt
streamlit run chatbot_app.py

pip install python-dotenv


heroku login
heroku create chatbotapp.py
git push heroku main
