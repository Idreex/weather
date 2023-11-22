from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from market.model import  User

class Registration(FlaskForm):
    
    def validate_username(self, username_to_check):
        User.query.filter_by(username = username_to_check.data).first()
        if User:
            raise ValidationError('Username already exists!, try different username')
        
    def validate_email_address(self, email_address_to_check):
        User.query.filter_by(email_address = email_address_to_check.data).first()
        if User:
            raise ValidationError('Email Address already exists!')


    username = StringField(label="Username", validators = [Length(min = 2, max = 30), DataRequired()])
    email_address = StringField(label='Email', validators = [Email(), DataRequired()])
    password1 = PasswordField(label='Password1', validators = [Length(min=3), DataRequired()])
    password2 = PasswordField(label='Password2', validators = [EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Create Account')




    
