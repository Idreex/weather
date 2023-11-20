from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField



class Registration(FlaskForm):
    username = StringField(label="Username")
    email = StringField(label='Email')
    password1 = PasswordField(label='Password1')
    password2 = PasswordField(label='Password2')
    submit = SubmitField(label='Create Account')
    
