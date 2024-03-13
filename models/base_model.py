#!/usr/bin/env python3
"""Define the Base Module"""
from uuid import uuid4
from sqlalchemy import Column, String, DateTime
from sqlalchemy.orm import declarative_base
from datetime import datetime, timezone

time = "%Y-%m-%dT%H:%M:%S.%f"
Base = declarative_base()


class BaseModel():
    """The base model class for all coming classes"""
    id = Column(String(60), primary_key=True)
    created_at = Column(DateTime, default=datetime.now(timezone.utc))
    updated_at = Column(DateTime, default=datetime.now(timezone.utc))

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
                self.created_at = datetime.now(timezone.utc)
            if 'updated_at' in kwargs:
                self.updated_at = datetime.strptime(kwargs['updated_at'], time)
            else:
                self.updated_at = datetime.now(timezone.utc)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now(timezone.utc)
            self.updated_at = datetime.now(timezone.utc)

    def __str__(self):
        """Return the string representation of the object"""
        new_dict = self.to_dict().copy()
        new_dict.pop('__class__', None)
        
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, new_dict)

    def save(self):
        """Update the updated_at attribute and save the instance"""
        self.updated_at = datetime.now(timezone.utc)
        from models import storage
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Return a dictionary containing all keys/values of __dict__"""
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = type(self).__name__
        new_dict['created_at'] = self.created_at.strftime(time)
        new_dict['updated_at'] = self.updated_at.strftime(time)
        new_dict.pop('_sa_instance_state', None)
        return new_dict
