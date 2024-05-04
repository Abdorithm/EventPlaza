#!/usr/bin/python3
""" Flask forms """
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, DateField, TimeField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from event_plaza import app
from event_plaza.models import User, Event


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
    remember = BooleanField('Remember me for 30 days')
    submit = SubmitField('Log In')

class UpdateProfileForm(FlaskForm):
    """ Class for the Sign Up form"""
    first_name = StringField('First Name',
                             validators=[DataRequired(), Length(min=2, max=20)])
    last_name = StringField('Last Name',
                            validators=[DataRequired(), Length(min=2, max=20)])                      
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    picture = FileField('Update your profile picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')

    def validate_email(self, email):
        """ validate that the email is unique """
        if email.data != current_user.email:
            with app.app_context():
                user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is already Registered.')

class CreateEventForm(FlaskForm):
    """" Class for creating an event form """
    import csv
    with open('cities.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        all_cities = [city[3] for city in spamreader]
        all_cities.pop(0)

    
    name = StringField('Name', validators=[DataRequired()])
    # Description limit is 1024 
    description = TextAreaField('Description', validators=[DataRequired(), Length(min=2, max=1024)])
    date = DateField('Date', format='%Y-%m-%d', validators=[DataRequired()])
    time = TimeField('Time', format='%H:%M', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    location = SelectField('Location', choices=all_cities)
    picture = FileField('Event thumbnail', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Create Event')

    def validate_name(self, name):
        """ validate that the event name is unique """
        with app.app_context():
            event = Event.query.filter_by(name=name.data).first()
        if event:
            raise ValidationError('That event name is already taken.')

class CreateTaskForm(FlaskForm):
    """ Class for creating a task form """
    name = StringField('Title', validators=[DataRequired(), Length(min=2, max=128)], render_kw={"placeholder": "Title", "spellcheck": "false"})
    description = TextAreaField('Description', validators=[DataRequired(), Length(min=2, max=1024)], render_kw={"placeholder": "Describe everything about this task here", "spellcheck": "false"})
    submit = SubmitField('Create')

class RequestResetForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')

    def validate_email(self, email):
        with app.app_context():
            user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError('There is no account with that email. You must register first.')


class ResetPasswordForm(FlaskForm):
    password = PasswordField('New Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Reset Password')
    

class VerifyEmailForm(FlaskForm):
    email = StringField('Email', validators=[Email()])
    submit = SubmitField('Send Email With Verification Link')
