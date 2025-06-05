from flask import Flask, request, render_template
import os
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    ip = request.remote_addr
    user_agent = request.headers.get('User-Agent')
    log_data = f"{datetime.now()} | IP: {ip} | User-Agent: {user_agent}\n"
    with open("log.txt", "a") as f:
        f.write(log_data)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
