from flask import render_template
from core import app


@app.route('/')
@app.route('/index/')
def index():
	'''
	this function call the index with options to sign up and sign in.
	'''
	return render_template("index.html")

@app.route('/signup/', methods=['GET', '[POST]'])
def signup():
	'''
	this function is to register new users... call a simple form and make a save in database.
	'''
	return render_template("signup.html")

@app.route('/sigin/')
def signin():
	'''
	this function call the page to login and process the user authentication;
	'''
	pass

