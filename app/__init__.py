from flask import Flask
from flask.ext.mongoengine import MongoEngine

app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {'DB': "todolist"}
app.config["SECRET_KEY"] = "top-secret"
db = MongoEngine(app)

from app import views
