#!/usr/bin/python3
""" Starts a Flask Web Application """
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


class Base(DeclarativeBase):
    pass
db = SQLAlchemy(model_class=Base)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'd685ddbe85e8fa0e7fb24d5aeb994e8f'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://plaza_dev:plaza_dev_pwd@localhost/plaza_dev_db'
db.init_app(app)
bcrypt =  Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'error'

from event_plaza import routes
