from flask import render_template, request
from core import app


@app.route('/')
@app.route('/index/')
def index():
	'''
	this function call the index with options to sign up and sign in.
	'''
	return render_template("index.html")

@app.route('/signup/')
def signup():
	'''
	this function just call a simple form
	'''
	return render_template("signup.html")
@app.route('/_reg/<nome>',methods=['POST'])
def register_user(nome):
	'''
	this function confirm the user register.
	'''
	return "<html>oi, %s</html>"%(nome)

@app.route('/sigin/')
def signin():
	'''
	this function call the page to login and process the user authentication;
	'''
	pass
@app.route('/logout/')
def logout():
	'''
	this function just finish the user session... the security is managed with flask-security
	'''
	pass
