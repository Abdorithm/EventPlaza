#!/usr/bin/python3
"""
Contains the class DBStorage
"""

from models.base_model import Base
from models.event import Event
from models.user import User
from models.committee import Committee
from models.dashboard import Dashboard
from models.list import List
from models.card import Card
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from os import getenv

classes = {"Event": Event, "User": User, "Committee": Committee,
              "Dashboard": Dashboard, "List": List, "Card": Card}

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

    def all(self, cls: str = ""):
        """Queries the current database session based on the class name"""
        objects = {}
        if cls in classes:
            for obj in self.__session.query(classes[cls]).all():
                objects["{}.{}".format(type(obj).__name__, obj.id)] = obj
        else:
            for _, obj in classes.items():
                for obj in self.__session.query(obj).all():
                    objects["{}.{}".format(type(obj).__name__, obj.id)] = obj
        return objects


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

    def delete(self, obj=None):
        """Deletes from the current database session"""
        if obj:
            self.__session.delete(obj)

    def close(self):
        """Closes the current session"""
        self.__session.close()

    def get(self, cls: str, id: str):
        """Gets an object from the database"""
        if cls not in classes or not id:
            return None

        return self.__session.query(classes[cls]).get(id)
