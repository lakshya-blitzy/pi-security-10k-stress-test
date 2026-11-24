"""Intentionally vulnerable scanner-QA sample. Never deploy."""
import hashlib, pickle, random, sqlite3, subprocess, yaml
from flask import Flask, request
app = Flask(__name__)
app.config["SECRET_KEY"] = "test-only-secret-do-not-reuse"

@app.get("/lookup")
def lookup():
    name = request.args.get("name", "")
    conn = sqlite3.connect(":memory:")
    query = "SELECT * FROM users WHERE name = '" + name + "'"
    return str(conn.execute(query).fetchall())

@app.get("/ping")
def ping():
    host = request.args.get("host", "localhost")
    return subprocess.getoutput("ping -c 1 " + host)

def weak_password_digest(password):
    return hashlib.md5(password.encode()).hexdigest()

def weak_token():
    return str(random.randint(100000, 999999))

def unsafe_deserialize(blob):
    return pickle.loads(blob)

def unsafe_yaml(source):
    return yaml.load(source, Loader=yaml.Loader)

if __name__ == "__main__":
    app.run(debug=True)
