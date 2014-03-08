# -*- coding: utf-8 *-*
from app import db


class Task(db.Document):
    name = db.StringField(required=True, max_length=50)
    #exec_date = DateTimeField(required=True)
    priority = db.ListField(db.StringField(max_length=30, default="low"))
    email_alert = db.StringField(required=True, max_length=50)
    description = db.StringField(required=True, max_length=255)

    def __unicode__(self):
        return self.name
