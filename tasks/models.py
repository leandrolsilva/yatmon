import datetime
from flask import url_for
from app import db

class User(db.Document):
    '''
    docstring
    '''
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)

    #nickname used in login and other things...
    nickname = db.StringField(max_length=30, required=True)

    #email used in notification tool
    email = db.StringField(max_length=50, required=True)

    #the password... I'll use sha256, sha512 for hash authentication... ;]
    password = db.StringField(max_length=128, required=True)


class Task(db.Document):
    '''
    This is a model new task form.
    '''
    #internal use
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)

    #name of task...
    name = db.StringField(max_length=50, required=True)

    #something like a id or primary key...
    slug = db.StringField(max_length=255, required=True)

    #owner of task have to be a user.
    owner = db.StringField(max_length=50, required=True)

    #date of finish/execution
    exec_date = db.DateTimeField(default=datetime.datetime.now, required=True)

    #the priority of task['urgent', 'medium', 'just_a_alert']
    priority = db.StringField(max_length=10, required=True)

    #some description about the task...
    desc = db.StringField(max_length=255, required=True)

    def get_absolute_url(self):
        return url_for('post', kwargs={"slug": self.slug})

    def __unicode__(self):
        return self.title

    meta = {
        'allow_inheritance': True,
        'indexes': ['-created_at', 'slug'],
        'ordering': ['-created_at']
    }
