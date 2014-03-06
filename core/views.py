from flask import render_template
from core import app


@app.route('/')
@app.route('/index/')
def index():
    return render_template("index.html")


@app.route('/signin/')
def signin():
    pass


@app.route('/signup/')
def signup():
	pass
