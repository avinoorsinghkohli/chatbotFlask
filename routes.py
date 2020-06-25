from app import app,db
from flask import Flask, render_template
import forms
@app.route('/')
@app.route('/index')
def home():
    return render_template('index.html')
@app.route('/about', methods=['GET','POST'])
def about():
    form=forms.AddTaskForm()
    if form.validate_on_submit():
        print(form.title.data)
        return render_template('about.html',form=form,title=form.title.data)
    return render_template('about.html',form=form)
