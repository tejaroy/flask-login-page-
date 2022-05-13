from wtforms import (
StringField,
PasswordField,
)
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length, EqualTo, Email, Regexp ,Optional
import email_validator
from wtforms import ValidationError,validators
from flask_login import current_user
from models import User


#login forms
class Login_Form(FlaskForm):
    email=StringField(validators=[
        DataRequired(),
        Length(3,25),
        Email(),
    ])
    pwd=PasswordField(validators=[
        DataRequired(),
        Length(8,25),
    ])
    username=StringField(validators=[
        Optional()
    ])

#register form
class Register_Form(FlaskForm):
    first_name=StringField(validators=[
        DataRequired(),
        Length(3,10)
    ])
    username=StringField(validators=[
        DataRequired(),
        Length(5,30,message='please provied a valid name'),
        Regexp("^[A-Za-z][A-Za-z0-9_.]*$",0,"Username must have only letters," "numbers,dots or underscores", ),
    ])
    email=StringField(validators=[
        DataRequired(),
        Length(3,25),
        Email(),
    ])
    pwd=PasswordField(validators=[
        Length(8,25),
        DataRequired(),
    ])
    cpwd=PasswordField(validators=[
        Length(8,25),
        DataRequired(),
        EqualTo("pwd",message="password should match"),
    ])

    def validator_email(self,email):
        if User.query.filter_by(email=email.data).first():
            raise ValidationError("Email is alraedy taken")

    def validator_uname(self,uname):
        if User.query.filter_by(username=username.data).first():
            raise ValidationError("Username alraedy taken")
