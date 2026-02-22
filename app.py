from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def hello():
    r = requests.get("https://example.com")
    return f"Status: {r.status_code}"

if __name__ == "__main__":
    app.run()
