#!/usr/bin/env python3
"""This module defines the Event model for EventPlaza"""
from models.base_model import BaseModel, Base
from models.event_tables import event_organizers, event_attendens
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Event(BaseModel, Base):
    """This class defines the Event model for EventPlaza"""
    __tablename__ = 'events'

    name = Column(String(128), nullable=False, unique=True)
    description = Column(String(1024), nullable=True)
    location = Column(String(128), nullable=True)
    start_time = Column(String(128), nullable=True)
    end_time = Column(String(128), nullable=True)
    organizer = relationship('User', secondary=event_organizers,
                             back_populates='organized_events')
    attendees = relationship('User', secondary=event_attendens,
                            back_populates='attended_events')
    dashboards = relationship('Dashboard', back_populates='event',
                              cascade='all, delete-orphan')
    committees = relationship('Committee', back_populates='event')
