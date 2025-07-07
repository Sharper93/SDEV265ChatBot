from flask import Flask, render_template, request
import os
from openai import OpenAI

app = Flask(__name__)

# Initialize OpenAI client
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def call_openai(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful School of IT chatbot. Answer questions about the School of IT clearly and helpfully."},
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