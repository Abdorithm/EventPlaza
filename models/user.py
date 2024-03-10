#!/usr/bin/env python3
"""This module defines the User model for EventPlaza"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String


class User(BaseModel, Base):
    """This class defines the User model for EventPlaza"""
    __tablename__ = 'organizers'
    username = Column(String(128), nullable=False, unique=True)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    email = Column(String(128), nullable=False, unique=True)
    phone = Column(String(128), nullable=True)

    def __init__(self, **kwargs):
        """Initializes the User"""
        super().__init__(**kwargs)
