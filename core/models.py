# -*- coding: utf-8 *-*
from core import db
import datetime

class User(db.Document):
	"""
	Preparing for User Access control (signup and signin)
	"""
	name 		= db.StringField(required=True, max_length=255, min_length=2)
	email 		= db.EmailField(required=True, verbose_name='e-mail')
	last_seen	= db.DateTimeField(default=datetime.datetime.now)
	date_modified = DateTimeField(default=datetime.datetime.now)
	password	= db.StringField(required=True, max_length=255)

    def __str__(self):
        return self.name

class Task(db.DynamicDocument):
	"""
	Used DynamicDocument in order to allow grouping TODO's by PROJECT or TAG/Contexts
	that can be created on the fly by the user
	"""
    name        = db.StringField(required=True, max_length=255)
    date_due   	= db.DateTimeField(required=True)
    email_alert = db.EmailField(required=True, verbose_name='e-mail alert')
    description = db.StringField(required=True, max_length=255)
    done 		= db.BooleanField()
    user 		= db.GenericReferenceField(choices=[User],required=False) #required=False used while User Access isn't finished. Design time only.

    def __str__(self):
        return self.name

