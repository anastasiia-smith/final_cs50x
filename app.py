
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/tasks")
def tasks():
    return render_template("tasks.html")

@app.route("/rewards")
def rewards():
    return render_template("rewards.html")

# Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template("error.html", error=404, msg="Page not found"), 404

# Internal Server Error
@app.errorhandler(500)
def page_not_found(e):
    return render_template("error.html", error=500, msg="Try again..."), 500