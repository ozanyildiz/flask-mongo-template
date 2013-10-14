from flask import render_template, url_for, redirect
from app import app
from forms import TaskForm
from models import Task

@app.route('/', methods = ['GET', 'POST'])
def index():
	form = TaskForm()
	if form.validate_on_submit(): # if it is a POST request
		task = Task(label = form.label.data)
		task.save()
		return redirect(url_for('index'))
	
	tasks = Task.objects.all()
	return render_template('index.html', form = form, tasks = tasks)
