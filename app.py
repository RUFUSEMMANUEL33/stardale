from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>🚀 Welcome To FERRARI</h1>
    <p>Successfully deployed using Docker & Jenkins CI/CD Pipeline!</p>
    """

@app.route("/health")
def health():
    return {"status": "running"}, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
