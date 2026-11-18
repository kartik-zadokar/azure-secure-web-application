
from flask import Flask, jsonify
import socket

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "Azure Backend API is running!",
        "server": socket.gethostname(),
        "status": "healthy"
    })

@app.route("/health")
def health():
    return jsonify({
        "status": "UP",
	"server": socket.gethostname()
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
