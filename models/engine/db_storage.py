#!/usr/bin/python3
"""
Contains the class DBStorage
"""

import models
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from os import environ


class DBStorage:
    """Interacts with the MySQL database"""
    __engine = None
    __session = None

    def __init__(self):
        """Creates the engine"""
        PLAZA_MYSQL_USER = environ.get('PLAZA_MYSQL_USER')
        PLAZA_MYSQL_PWD = environ.get('PLAZA_MYSQL_PWD')
        PLAZA_MYSQL_HOST = environ.get('PLAZA_MYSQL_HOST')
        PLAZA_MYSQL_DB = environ.get('PLAZA_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(PLAZA_MYSQL_USER,
                                              PLAZA_MYSQL_PWD,
                                              PLAZA_MYSQL_HOST,
                                              PLAZA_MYSQL_DB),
                                      pool_pre_ping=True)
