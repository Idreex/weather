from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from market.model import  User

class Registrationform(FlaskForm):
    
    def validate_username(self, username_to_check):
        user = User.query.filter_by(username = username_to_check.data).first()
        if user:
            raise ValidationError('Username already exists!, try different username')
        
    def validate_email_address(self, email_address_to_check):
        user = User.query.filter_by(email_address = email_address_to_check.data).first()
        if user:
            raise ValidationError('Email Address already exists!')


    username = StringField(label="Username", validators = [Length(min = 2, max = 30), DataRequired()])
    email_address = StringField(label='Email', validators = [Email(), DataRequired()])
    password1 = PasswordField(label='Password1', validators = [Length(min=3), DataRequired()])
    password2 = PasswordField(label='Password2', validators = [EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Create Account')



class Loginform(FlaskForm):

    username = StringField(label="Username", validators=[DataRequired()])
    password = PasswordField(label='Password', validators = [DataRequired()])
    submit = SubmitField(label="Submit")

    
class PurchaseForm(FlaskForm):
    submit = SubmitField(label='Buy')







    
