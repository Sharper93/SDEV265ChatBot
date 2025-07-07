from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    answer = None
    if request.method == "POST":
        question = request.form.get("question")
        answer = f"You asked: {question}"
    return render_template("index.html", answer=answer)

if __name__ == "__main__":
    app.run(debug=True)