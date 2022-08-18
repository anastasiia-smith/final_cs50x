
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

# Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template("error.html", error=404, msg="Page not found"), 404

# Internal Server Error
@app.errorhandler(500)
def page_not_found(e):
    return render_template("error.html", error=500, msg="Try again..."), 500