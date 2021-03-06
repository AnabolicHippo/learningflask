from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
class SignupForm(Form): 
	first_name = StringField("First Name", validators=[DataRequired("You must enter your first name")])
	last_name = StringField("Last Name", validators=[DataRequired("You must enter your last name")])
	email = StringField('Email', validators=[DataRequired("You need to enter a valid email"), Email("Please enter your email address.")])
	password = PasswordField('Password', validators=[DataRequired("You must enter a password"), Length(min=6, message="Passwords must be at least 6 characters long")])
	submit = SubmitField('Sign up')

class LoginForm(Form):
	email = StringField('Email', validators=[DataRequired("please enter your email address"), Email("Please Enter your email")])
	password = PasswordField('Password', validators=[DataRequired("please enter your passowrd")])
	submit = SubmitField('Sign in')

class AddressForm(Form):
  address = StringField('Address', validators=[DataRequired("Please enter an address.")])
  submit = SubmitField("Search")