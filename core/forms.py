from flask_wtf import Form
from wtforms import TextField, DateTimeField, BooleanField
from wtforms.validators import DataRequired

class taskForm(Form):
    done			= BooleanField('Task done')
    name      		= TextField('Task Name', validators=[DataRequired()])
    date_due 		= DateTimeField('Date due', validators=[DataRequired()])
    description 	= TextField('Description', validators=[DataRequired()])
    email_alert 	= BooleanField('Send e-mail alerts', validators=[DataRequired()])
