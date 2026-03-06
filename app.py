from flask import Flask

app = Flask(__name__)

API_KEY = "sk_test_123456789SECRET"

@app.route("/")
def home():
    return "DevSecOps Pipeline Running!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
