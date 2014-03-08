from flask import render_template, redirect
from app import app


@app.route('/project/')
def project():
    '''Just a redirect, but I will improve it in the future... :]'''
    return redirect("https://github.com/alesouza/yatmon.git")


@app.route('/')
@app.route('/index/')
def index():
    return render_template('test.jade')
