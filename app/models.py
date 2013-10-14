from app import db

class Task(db.Document):
	label = db.StringField(required = True)
	
