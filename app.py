from flask import Flask, request, render_template
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    ip = request.remote_addr
    user_agent = request.headers.get("User-Agent")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("log.txt", "a") as file:
        file.write(f"{timestamp} | IP: {ip} | User-Agent: {user_agent}\n")

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
