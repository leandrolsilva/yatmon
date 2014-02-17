from flask import render_template
from flask.ext.security import login_required, \
                               Security, MongoEngineUserDatastore
from core import app, db
from core.models import Role, User


# Setup Flask-Security
user_datastore = MongoEngineUserDatastore(db, User, Role)
security = Security(app, user_datastore)


@app.route('/')
@app.route('/index/')
def index():
    '''this function call the index with options to sign up and sign in.'''
    return render_template("index.html")


@app.route('/signup/')
def signup():
    '''this function just call a simple form'''
    return render_template("security/register_user.html")

@app.route('/sigin/')
def signin():
    '''this function call the login form'''
    return render_template("security/login_user.html")


@app.route('/logout/')
@login_required
def logout():
    '''this function finish the current session'''
    pass


@app.route('/user_auth/')
@login_required
def user_auth(nickname, password):
    '''This class make the user validation and create a session'''
    pass
