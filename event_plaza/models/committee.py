#!/usr/bin/env python3
"""This module contains the Committee class"""
from .base_model import BaseModel
from sqlalchemy import Column, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from event_plaza import db


committee_member = Table('committee_member', db.Model.metadata,
                         Column('committee_id', String(60),
                                ForeignKey('committees.id', onupdate='CASCADE',
                                           ondelete='CASCADE'),
                                primary_key=True),
                         Column('user_id', String(60),
                                ForeignKey('users.id', onupdate='CASCADE',
                                           ondelete='CASCADE'),
                                primary_key=True))


committee_vice = Table('committee_vice', db.Model.metadata,
                       Column('committee_id', String(60),
                              ForeignKey('committees.id', onupdate='CASCADE',
                                         ondelete='CASCADE'),
                              primary_key=True),
                       Column('user_id', String(60),
                              ForeignKey('users.id', onupdate='CASCADE',
                                         ondelete='CASCADE'),
                              primary_key=True))


committee_head = Table('committee_head', db.Model.metadata,
                       Column('committee_id', String(60),
                              ForeignKey('committees.id', onupdate='CASCADE',
                                         ondelete='CASCADE'),
                              primary_key=True),
                       Column('user_id', String(60),
                              ForeignKey('users.id', onupdate='CASCADE',
                                         ondelete='CASCADE'),
                              primary_key=True))



class Committee(BaseModel, db.Model):
    """This class represents the committee table"""
    __tablename__ = 'committees'

    event_id = Column(String(60), ForeignKey('events.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)

    members = relationship('User', secondary='committee_member',
                           back_populates='member_committees', lazy=True)
    vices = relationship('User', secondary='committee_vice',
                         back_populates='vice_committees', lazy=True)
    heads = relationship('User', secondary='committee_head',
                         back_populates='head_committees', lazy=True)
    dashboard = relationship('Dashboard', back_populates='committee', lazy=True)
    event = relationship('Event', back_populates='committees', lazy=True)
