from flask import Flask, render_template, redirect, request, session
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasksapp.db'
db = SQLAlchemy(app)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    password = db.Column(db.String(200), nullable=False)
    tasks = db.relationship('Tasks', backref='person', lazy=True)
    rewards = db.relationship('Rewards', backref='person', lazy=True)

    def __repr__(self):
        return '<Name %r>' % self.name

class Tasks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(300), nullable=False)
    person_id = db.Column(db.Integer, db.ForeignKey('person.id'),
        nullable=False)

    def __repr__(self):
        return '<Task %r>' % self.task

class Rewards(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    reward = db.Column(db.String(300), nullable=False)
    person_id = db.Column(db.Integer, db.ForeignKey('person.id'),
        nullable=False)

    def __repr__(self):
        return '<Reward %r>' % self.reward

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
    return render_template("error.html", error=404, msg="Page not found", title="Something went wrong"), 404

# Internal Server Error
@app.errorhandler(500)
def page_not_found(e):
    return render_template("error.html", error=500, msg="Try again...", title="Something went wrong"), 500