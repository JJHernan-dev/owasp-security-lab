from flask import Flask, request, render_template
import sqlite3
import os

app = Flask(__name__)

MODE = os.getenv("APP_MODE", "vulnerable")
comments = []

def get_db_connection():
    conn = sqlite3.connect("database.db")
    return conn

@app.route("/")
def home():
    return render_template("login.html", mode=MODE)

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    conn = get_db_connection()
    cursor = conn.cursor()

    if MODE == "vulnerable":
        # ❌ SQL Injection vulnerable
        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        cursor.execute(query)

    else:
        # ✅ Secure version
        query = "SELECT * FROM users WHERE username = ? AND password = ?"
        cursor.execute(query, (username, password))

    user = cursor.fetchone()
    conn.close()

    if user:
        return render_template(
            "login.html",
            mode=MODE,
            message=f"Bienvenido {user[1]}",
            success=True
    )

    else:
        return render_template(
            "login.html",
            mode=MODE,
            message="Credenciales inválidas",
            success=False
    )

@app.route("/comments", methods=["GET", "POST"])
def comments_page():

    if request.method == "POST":
        comment = request.form.get("comment")
        comments.append(comment)

    return render_template(
        "comments.html",
        comments=comments
    )
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)