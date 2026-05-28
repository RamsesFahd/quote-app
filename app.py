from flask import Flask

app = Flask(__name__)

QUOTE = "Push your limits, not your deadlines."

@app.route("/")
def home():
    return f"<h1>Quote of the Day</h1><p>{QUOTE}</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)