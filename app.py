from flask import Flask, render_template, request
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Initialize OpenAI client
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def call_openai(prompt):
    system_content = (
        "You are a helpful chatbot for the Ivy Tech School of IT. "
        "You ONLY answer questions specifically about Ivy Tech or its School of IT. "
        "If the question is outside that scope, you must reply exactly with: "
        "'Sorry, that is out of my scope.'"
    )
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_content},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()

@app.route("/", methods=["GET", "POST"])
def index():
    answer = None
    if request.method == "POST":
        question = request.form.get("question")
        answer = call_openai(question)
    return render_template("index.html", answer=answer)

if __name__ == "__main__":
    app.run(debug=True)