#!/usr/bin/env python3
"""Define the Base Module"""
from uuid import uuid4
from event_plaza import db
from datetime import datetime

time = "%Y-%m-%dT%H:%M:%S"


class BaseModel():
    """The base model class for all coming classes"""
    id = db.Column(db.String(60), primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, default=datetime.now())

    def __init__(self, **kwargs):
        """Initialization of the base model"""

        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)

            if 'id' in kwargs:
                self.id = kwargs['id']
            else:
                self.id = str(uuid4())
            if 'created_at' in kwargs:
                self.created_at = datetime.strptime(kwargs['created_at'], time)
            else:
                self.created_at = datetime.now()
            if 'updated_at' in kwargs:
                self.updated_at = datetime.strptime(kwargs['updated_at'], time)
            else:
                self.updated_at = datetime.now()
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """Return the string representation of the object"""
        new_dict = self.to_dict().copy()
        new_dict.pop('__class__', None)
        
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, new_dict)

    def to_dict(self):
        """Return a dictionary containing all keys/values of __dict__"""
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = type(self).__name__
        new_dict['created_at'] = self.created_at.strftime(time)
        new_dict['updated_at'] = self.updated_at.strftime(time)
        new_dict.pop('_sa_instance_state', None)
        return new_dict
