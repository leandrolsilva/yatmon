from flask import render_template, redirect
from core import app
from core.models import Task
from core.forms import taskForm
import urllib.request

@app.route('/project/')
def project():
    try:
        github = "https://github.com/alexandre/yatmon.git"
        bitbucket = "https://bitbucket.org/alesouza/yatmon"
        if urllib.request.urlopen(github).getcode() != 200:
            return redirect(bitbucket)
        return redirect(github)
    except Exception as error:         
        return 'erro'
                   
@app.route('/')
@app.route('/index/')
def index():
    return render_template('index.jade')

@app.route('/newTask/')
def newTask():
    task = Task()
    taskform = taskForm()
    return render_template('newtask.jade',taskform=taskform)
