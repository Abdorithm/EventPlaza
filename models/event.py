#!/usr/bin/env python3
"""This module defines the Event model for EventPlaza"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String


class Event(BaseModel, Base):
    """This class defines the Event model for EventPlaza"""
    __tablename__ = 'events'
    name = Column(String(128), nullable=False, unique=True)
    description = Column(String(1024), nullable=False)
    location = Column(String(128), nullable=False)
    start_time = Column(String(128), nullable=False)
    end_time = Column(String(128), nullable=False)
    manager_id = Column(String(60), nullable=False)
    attendees = Column(String(128), nullable=False)

    def __init__(self, *args, **kwargs):
        """Initializes the Event"""
        super().__init__(*args, **kwargs)
