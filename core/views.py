from flask import render_template
from core import app
#from core.models import Role, User


@app.route('/')
@app.route('/index/')
def index():
    '''this function call the index with options to sign up and sign in.'''
    return render_template("index.html")


@app.route('/signup/', methods=['GET', 'POST'])
def signup():
    '''this function just call a simple form'''
    return render_template("security/register_user.html")


@app.route('/sigin/')
def signin():
    '''this function call the login form'''
    return render_template("security/login_user.html")


@app.route('/logout/')
def logout():
    '''this function finish the current session'''
    pass
