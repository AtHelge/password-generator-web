import os
import secrets
import string
from flask import Flask, render_template

app = Flask(__name__)

def generate_secure_password(length=16):
    characters = string.ascii_letters + string.digits + "!@#$%^&*()-_=+"
    return "".join(secrets.choice(characters) for _ in range(length))

@app.route("/")

def index():
    passwords = [generate_secure_password() for _ in range(3)]
    return render_template("index.html", passwords=passwords)

if __name__ == "__main__":
   
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)