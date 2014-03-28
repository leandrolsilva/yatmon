from flask import render_template, redirect
from app import app
import urllib.request

@app.route('/project/')
def project():
    '''
    if github down (yeap...), try redirect to bitbucket...
    '''
    try:
        github = "https://github.com/alexandre/yatmon.git"
        bitbucket = "https://bitbucket.org/alesouza/yatmon"
        if urllib.request.urlopen(github).getcode() != 200:
	        return redirect(bitbucket)
        return redirect(github)
    except Exception as error:         
        return "mayday...mayday....houston, we have a problem! WTH!, the source code is lost..."
                

@app.route('/')
@app.route('/index/')
def index():
    return render_template('index.jade')
