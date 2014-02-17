# -*- coding: utf-8 *-*
from core import db
import datetime


class Role(db.Document):
    '''this a simple control for the roles...'''
    name = db.StringField(max_length=80, unique=True)
    description = db.StringField(max_length=255)


class User(db.Document):
    '''model for users...'''
    #editable fields
    nickname = db.StringField(max_length=30, required=True)
    id = db.StringField(required=True)
    email = db.StringField(max_length=50, required=True)
    password = db.StringField(max_length=128, required=True)
    #status = [True, False]
    active = db.BooleanField(required=True, default=True)

    #log fields...
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    #I can't show a error if the app not save it or something wrong happen
    last_login_at = db.DateTimeField(default=datetime.datetime, required=False)
    current_login_at = db.DateTimeField(default=datetime.datetime,
                                        required=False)

    #information 4 sell to NS...lol
    last_login_ip = db.StringField(max_length=20, required=True)
    current_login_ip = db.StringField(max_length=20, required=True)
    login_count = db.StringField(max_length=20, required=True)
