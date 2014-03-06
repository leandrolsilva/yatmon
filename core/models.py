# -*- coding: utf-8 *-*
from core import db


class User(db.Document):

    '''model for users...'''
    # editable fields
    id = db.StringField()
    nickname = db.StringField(max_length=30, required=True)
    email = db.StringField(max_length=50, required=True)
    password = db.StringField(max_length=128, required=True)
    active = db.BooleanField(required=True, default=True)
    role = db.StringField(default="role_user")
