from flask import Flask
from flask import redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///ekluntom"
db = SQLAlchemy(app)

@app.route("/")
def index():
    result = db.session.execute(text("SELECT content FROM messages"))
    messages = result.fetchall()
    return render_template("index.html", count=len(messages), messages=messages)

@app.route("/sign_in")
def sign_in():
    return render_template("sign_in.html")

@app.route("/new_post")
def new_post():
    return render_template("new_post.html")

@app.route("/new_user")
def new_user():
    return render_template("new_user.html")

@app.route("/send", methods=["POST"])
def send():
    content = request.form["content"]
    sql = text("INSERT INTO messages (content) VALUES (:content)")
    db.session.execute(sql, {"content":content})
    db.session.commit()
    return redirect("/")