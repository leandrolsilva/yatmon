from flask import render_template, redirect
from app import app


@app.route('/project/')
def project():
    return redirect("https://github.com/alesouza/yatmon.git")


@app.route('/')
@app.route('/index/')
def index():
    return render_template('index.jade')
