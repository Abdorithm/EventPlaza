#!/usr/bin/env python3
"""This module defines the Organizer model for EventPlaza"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Organizer(BaseModel, Base):
    """This class defines the Organizer model for EventPlaza"""
    __tablename__ = 'organizers'

    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    email = Column(String(128), nullable=True)
    phone = Column(String(128), nullable=True)
    events = relationship("Event", backref="organizer")

    def __init__(self, **kwargs):
        """Initializes the Organizer"""
        super().__init__(**kwargs)
