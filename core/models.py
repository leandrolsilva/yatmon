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
    id = db.StringField()
    nickname = db.StringField(max_length=30, required=True)
    email = db.StringField(max_length=50, required=True)
    password = db.StringField(max_length=128, required=True)
    active = db.BooleanField(required=True, default=True)
    role = db.StringField(default="role_user")

