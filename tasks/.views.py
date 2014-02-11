from app import app
from flask import render_template

@app.route('/')
@app.route('/index/')
def index():
    return render_template("index.html")

@app.route('/signup/')
def signup():
	return render_template("signup.html")

@app.route('/login/')
def login():
	pass
