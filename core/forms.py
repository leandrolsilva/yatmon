from flask_wtf import Form
from wtforms import TextField, DateTimeField
from wtforms.validators import DataRequired

class taskForm(Form):
    name      = TextField('Task Name', validators=[DataRequired()])
    exec_date = DateTimeField('Date', validators=[DataRequired()])
    email     = TextField('Email to Alerts', validators=[DataRequired()])
    desc      = TextField('Description', validators=[DataRequired()])