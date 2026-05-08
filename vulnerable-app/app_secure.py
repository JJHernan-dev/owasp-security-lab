from flask import Flask, request
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def home():
    return "OWASP Security Lab Running"

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    conn = get_db_connection()
    cursor = conn.cursor()

    # ✅ VULNERABILIDAD CORREGIDA (SQL Injection)
    query = "SELECT * FROM users WHERE username = ? AND password = ?"
    cursor.execute(query, (username, password))
    #---------------------------------------------------------------------   
    user = cursor.fetchone()

    conn.close()

    if user:
        return f"Welcome {user['username']}"
    else:
        return "Invalid credentials", 401

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)