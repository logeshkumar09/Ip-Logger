from flask import Flask, request, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    user_agent = request.headers.get('User-Agent')
    log_line = f"{datetime.now()} | IP: {ip} | User-Agent: {user_agent}\n"
    
    with open("log.txt", "a") as f:
        f.write(log_line)
    
    return render_template('index.html')
