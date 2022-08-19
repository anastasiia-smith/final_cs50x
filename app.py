
from flask import Flask, render_template, redirect, session\

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    return render_template("login.html", title="Log in")

@app.route("/register", methods=["GET", "POST"])
def register():
    return render_template("register.html", title="Register")

@app.route("/tasks", methods=["GET", "POST"])
def tasks():
    return render_template("tables.html", title="Tasks", header="task", name="Name of task")

@app.route("/rewards", methods=["GET", "POST"])
def rewards():
    return render_template("tables.html", title="Rewards", header="reward", name="Name of reward")

# Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template("error.html", error=404, msg="Page not found"), 404

# Internal Server Error
@app.errorhandler(500)
def page_not_found(e):
    return render_template("error.html", error=500, msg="Try again..."), 500