# -*- coding: utf-8 *-*
from core import db

class Task(db.Document):
    name        = db.StringField(required=True, max_length=50)
    exec_date   = db.DateTimeField(required=True)
    email_alert = db.StringField(required=True, max_length=50)
    description = db.StringField(required=True, max_length=255)

    def __unicode__(self):
        return self.name

