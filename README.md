# 📚 SDEV265 School of IT Chatbot

Collaborative assignment for Systems Software Analysis (SDEV 265) at Ivy Tech.  
Team Members: Walter Hodgson, Grant Perry, and Ren Davis.

This project is a simple Flask web app that connects to OpenAI's GPT model to answer questions about the Ivy Tech School of IT.  

---

## 🚀 Project Goal

✅ User-friendly chatbot interface  
✅ Uses OpenAI's GPT to generate answers  
✅ Secure handling of API keys via `.env`  
✅ Clean, documented, collaborative code

---

## 🛠️ Prerequisites

- Python 3.10 or higher
- A free or paid OpenAI account with an API key

---

## 💻 Getting Started

1️⃣ Set up your virtual environment

```bash
git clone https://github.com/your-org/your-repo.git
cd your-repo

2️⃣ Set up your virtual environment

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3️⃣ Install requirements

pip install -r requirements.txt

🔑 Setting up your OpenAI API Key

1️⃣ Create a .env file in the project root (same level as app.py):

touch .env

2️⃣ Add this line to it (with your actual key):

OPENAI_API_KEY=sk-your-own-key-here

3️⃣ That’s it! When you run flask run, the app will read your API key automatically.

✅ Important: .env is in .gitignore, so you will never accidentally commit your secret key to GitHub.

⚡️ Running the App Locally

flask run

✅ Open your browser at: http://127.0.0.1:5000
✅ Enter a question to test the chatbot.

🧭 Project Structure

.
├── app.py
├── requirements.txt
├── .gitignore
├── templates/
│   └── index.html
└── venv/