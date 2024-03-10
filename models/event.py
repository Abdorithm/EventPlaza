#!/usr/bin/env python3
"""This module defines the Event model for EventPlaza"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Table
from sqlalchemy.orm import relationship

event_organizer = Table('event_organizer', Base.metadata,
                        Column('event_id', String(60),
                               ForeignKey('events.id', onupdate='CASCADE',
                                          ondelete='CASCADE'),
                               primary_key=True),
                        Column('user_id', String(60),
                               ForeignKey('users.id', onupdate='CASCADE',
                                          ondelete='CASCADE'),
                               primary_key=True))

attendee_event = Table('attendee_event', Base.metadata,
                          Column('event_id', String(60),
                                ForeignKey('events.id', onupdate='CASCADE',
                                          ondelete='CASCADE'),
                                primary_key=True),
                          Column('user_id', String(60),
                                ForeignKey('users.id', onupdate='CASCADE',
                                          ondelete='CASCADE'),
                                primary_key=True))

class Event(BaseModel, Base):
    """This class defines the Event model for EventPlaza"""
    __tablename__ = 'events'

    name = Column(String(128), nullable=False, unique=True)
    description = Column(String(1024), nullable=True)
    location = Column(String(128), nullable=True)
    start_time = Column(String(128), nullable=True)
    end_time = Column(String(128), nullable=True)
    organizer = relationship('User', secondary=event_organizer,
                             back_populates='organized_events')

    def __init__(self, **kwargs):
        """Initializes the Event"""
        super().__init__(**kwargs)
