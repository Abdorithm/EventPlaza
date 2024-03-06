#!/usr/bin/python3
"""
Contains the class DBStorage
"""

from models.base_model import Base
from models.event import Event
from models.organizer import Organizer
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from os import getenv


class DBStorage:
    """Interacts with the MySQL database"""

    def __init__(self):
        """Creates the engine"""
        PLAZA_MYSQL_USER = getenv('PLAZA_MYSQL_USER')
        PLAZA_MYSQL_PWD = getenv('PLAZA_MYSQL_PWD')
        PLAZA_MYSQL_HOST = getenv('PLAZA_MYSQL_HOST')
        PLAZA_MYSQL_DB = getenv('PLAZA_MYSQL_DB')
        PLAZA_ENV = getenv('PLAZA_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(PLAZA_MYSQL_USER,
                                              PLAZA_MYSQL_PWD,
                                              PLAZA_MYSQL_HOST,
                                              PLAZA_MYSQL_DB),
                                      pool_pre_ping=True)
        if PLAZA_ENV == "test":
            Base.metadata.drop_all(self.__engine)

    def reload(self):
        """Creates all tables in the database"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def save(self):
        """Commits all changes of the current database session"""
        self.__session.commit()

    def new(self, obj):
        """Adds the instance to the current database session"""
        self.__session.add(obj)

    def close(self):
        """Closes the current session"""
        self.__session.close()
