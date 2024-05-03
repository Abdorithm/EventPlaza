#!/usr/bin/env python3
"""This module defines the Event model for EventPlaza"""
from .base_model import BaseModel
from .event_tables import event_organizers, event_attendens
from event_plaza import db


class Event(BaseModel, db.Model):
    """This class defines the Event model for EventPlaza"""
    __tablename__ = 'events'

    name = db.Column(db.String(128), nullable=False, unique=True)
    description = db.Column(db.String(1024), nullable=True)
    location = db.Column(db.String(128), nullable=True)
    date = db.Column(db.String(128), nullable=True)
    time = db.Column(db.String(128), nullable=True)
    image_file = db.Column(db.String(32), nullable=False, default='event_default.jpg')
    managers = db.relationship('User', secondary='event_managers',
                            back_populates='managed_events', lazy=True)
    organizer = db.relationship('User', secondary='event_organizers',
                             back_populates='organized_events', lazy=True)
    attendees = db.relationship('User', secondary='event_attendens',
                            back_populates='attended_events', lazy=True)
    committees = db.relationship('Committee', back_populates='event', lazy=True)
