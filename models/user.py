#!/usr/bin/env python3
"""This module defines the User model for EventPlaza"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.event_tables import event_organizers, event_attendens


class User(BaseModel, Base):
    """This class defines the User model for EventPlaza"""
    __tablename__ = 'users'

    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    email = Column(String(128), nullable=False, unique=True)
    password = Column(String(128), nullable=False)
    image_file = Column(String(20), nullable=False, default='default.jpg')

    organized_events = relationship('Event', secondary=event_organizers,
                                    back_populates='organizer')
    attended_events = relationship('Event', secondary=event_attendens,
                                      back_populates='attendees')
    assigned_cards = relationship('Card', secondary='assign',
                                    back_populates='assignees')
    member_committees = relationship('Committee', secondary='committee_member',
                                    back_populates='members')
    vice_committees = relationship('Committee', secondary='committee_vice',
                                    back_populates='vices')
    head_committees = relationship('Committee', secondary='committee_head',
                                    back_populates='heads')
