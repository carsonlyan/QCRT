from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from flask import render_template, redirect, url_for
from . import author


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Submit')


@author.route('/login', methods=('GET', 'POST'))
def login():
    loginForm = LoginForm(csrf_enabled=False)
    return render_template('login.html', loginForm=loginForm)