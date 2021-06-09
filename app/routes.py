from flask import Flask, render_template, redirect, url_for
from app.db import db
from app import app
from app.forms import LoginForm


@app.route('/',  methods=['GET','POST'])
def login():
    form = LoginForm(csrf_enabled=False)
    if form.validate_on_submit():
        print(f'Username: {form.username.data}\
                Password: {form.password.data}\
                Remember_me: {form.remember_me.data}')
        return redirect(url_for('dbViewer'))
    return render_template('login.html', form=form)

@app.route('/dbViewer')
def dbViewer():
    return render_template('dbViewer.html', listColumns=db.select_names_tables(),  listInfo=db.select_all())

app.run(port=6500)
