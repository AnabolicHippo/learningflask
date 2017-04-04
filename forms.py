from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
class SignupForm(Form): 
	first_name = StringField("First Name", validators=[DataRequired("You must enter your first name")])
	last_name = StringField("Last Name", validators=[DataRequired("You must enter your last name")])
	email = StringField('Email', validators=[DataRequired("You need to enter a valid email"), Email("Please enter your email address.")])
	password = PasswordField('Password', validators=[DataRequired("You must enter a password"), Length(min=6, message="Passwords must be at least 6 characters long")])
	submit = SubmitField('Sign up')


