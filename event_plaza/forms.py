#!/usr/bin/python3
""" Flask forms """
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from event_plaza import app
from event_plaza.models import User


class RegistrationForm(FlaskForm):
    """ Class for the Sign Up form"""
    first_name = StringField('First Name',
                             validators=[DataRequired(), Length(min=2, max=20)])
    last_name = StringField('Last Name',
                            validators=[DataRequired(), Length(min=2, max=20)])                      
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_email(self, email):
        """ validate that the email is unique """
        with app.app_context():
            user = User.query.filter_by(email=email.data).first()

        if user:
            raise ValidationError('That email is already Registered.')

        


class LoginForm(FlaskForm):
    """ Class for the log in form """                 
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Log In')
