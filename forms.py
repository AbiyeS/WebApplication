from flask_wtf import Form
from wtforms import StringField, PasswordField, TextAreaField
from wtforms.validators import (DataRequired, Regexp, ValidationError, Email,
							   Length, EqualTo)

from models import User

def name_exists(form, field):
	if User.select().where(User.username == field.data).exists():
		raise ValidationError('User already exists.')

def email_exists(form,field):
	if User.select().where(User.email == field.data).exists():
		raise ValidationError('User already exists.')

class RegisterForm(Form):
	username = StringField(
		'Username',
		validators=[
			DataRequired(),
			Regexp(
				r'^[a-zA-Z0-9_]+$',
				message = ("Letters_Numbers and Underscore only")
				),
			name_exists
		])

	email = StringField(
		'Email',
		validators=[
			DataRequired(),
			Email(),
			email_exists
		])

	password = PasswordField(
		'Password',
		validators=[
			DataRequired(),
			Length(min=2),
			EqualTo('password2', message = 'Passwords must be the same')
		])
	password2 = PasswordField(
		'Confirm Password',
		validators=[DataRequired()
		])


class LoginForm(Form):
	email = StringField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired()])

class PostForm(Form):
	content = TextAreaField("Post", validators = [DataRequired()])
