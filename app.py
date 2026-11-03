import os
import secrets
import string
from flask import Flask, render_template
import redis

app = Flask(__name__)


r = redis.Redis(
    host=os.environ.get("REDIS_HOST", "localhost"),
    port=6379,
    decode_responses=True,)

def generate_secure_password(length=16):
    characters = string.ascii_letters + string.digits + "!@#$%^&*()-_=+"
    return "".join(secrets.choice(characters) for _ in range(length))

def count_generated(amount):
    try:
        return r.incrby("passwords_generated", amount)
    except redis.exceptions.ConnectionError:
        return None

@app.route("/")

def index():
    passwords = [generate_secure_password() for _ in range(3)]
    count = count_generated(len(passwords))
    return render_template("index.html", passwords=passwords, count=count)

if __name__ == "__main__":
   
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)