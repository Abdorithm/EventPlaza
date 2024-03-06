#!/usr/bin/env python3
"""This module defines the Event model for EventPlaza"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey


class Event(BaseModel, Base):
    """This class defines the Event model for EventPlaza"""
    __tablename__ = 'events'

    name = Column(String(128), nullable=False, unique=True)
    description = Column(String(1024), nullable=True)
    location = Column(String(128), nullable=True)
    start_time = Column(String(128), nullable=True)
    end_time = Column(String(128), nullable=True)
    organizer_id = Column(String(60),
                          ForeignKey('organizers.id'), nullable=False)
    attendees = Column(String(128), nullable=True)

    def __init__(self, **kwargs):
        """Initializes the Event"""
        super().__init__(**kwargs)
