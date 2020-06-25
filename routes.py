from app import app,db
from flask import Flask, render_template, url_for, redirect, flash, get_flashed_messages
import forms
from models import Task
from datetime import datetime
@app.route('/')
@app.route('/index')
def index():
    tasks=Task.query.all()
    return render_template('index.html',tasks=tasks)
@app.route('/add', methods=['GET','POST'])
def add():
    form=forms.AddTaskForm()
    if form.validate_on_submit():
        #print(form.title.data)
        t=Task(title=form.title.data, date=datetime.utcnow())
        db.session.add(t)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add.html',form=form)
