from flask.ext.wtf import Form
from wtforms import TextField
from wtforms.validators import Required

class TaskForm(Form):
	label = TextField('label', validators = [Required()])
