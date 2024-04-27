#!/usr/bin/env python3
"""This module defines the Event model for EventPlaza"""
from .base_model import BaseModel
from .event_tables import event_organizers, event_attendens
from event_plaza import db
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Event(BaseModel, db.Model):
    """This class defines the Event model for EventPlaza"""
    __tablename__ = 'events'

    name = Column(String(128), nullable=False, unique=True)
    description = Column(String(1024), nullable=True)
    location = Column(String(128), nullable=True)
    start_time = Column(String(128), nullable=True)
    end_time = Column(String(128), nullable=True)
    organizer = relationship('User', secondary='event_organizers',
                             back_populates='organized_events', lazy=True)
    attendees = relationship('User', secondary='event_attendens',
                            back_populates='attended_events', lazy=True)
    dashboards = relationship('Dashboard', back_populates='event',
                              cascade='all, delete-orphan', lazy=True)
    committees = relationship('Committee', back_populates='event', lazy=True)
