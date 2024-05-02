#!/usr/bin/env python3
"""This module contains the Committee class"""
from .base_model import BaseModel
from event_plaza import db


committee_member = db.Table('committee_member', db.Model.metadata,
                         db.Column('committee_id', db.String(60),
                                db.ForeignKey('committees.id', onupdate='CASCADE',
                                           ondelete='CASCADE'),
                                primary_key=True),
                         db.Column('user_id', db.String(60),
                                db.ForeignKey('users.id', onupdate='CASCADE',
                                           ondelete='CASCADE'),
                                primary_key=True))


committee_vice = db.Table('committee_vice', db.Model.metadata,
                       db.Column('committee_id', db.String(60),
                              db.ForeignKey('committees.id', onupdate='CASCADE',
                                         ondelete='CASCADE'),
                              primary_key=True),
                       db.Column('user_id', db.String(60),
                              db.ForeignKey('users.id', onupdate='CASCADE',
                                         ondelete='CASCADE'),
                              primary_key=True))


committee_head = db.Table('committee_head', db.Model.metadata,
                       db.Column('committee_id', db.String(60),
                              db.ForeignKey('committees.id', onupdate='CASCADE',
                                         ondelete='CASCADE'),
                              primary_key=True),
                       db.Column('user_id', db.String(60),
                              db.ForeignKey('users.id', onupdate='CASCADE',
                                         ondelete='CASCADE'),
                              primary_key=True))



class Committee(BaseModel, db.Model):
    """This class represents the committee table"""
    __tablename__ = 'committees'

    event_id = db.Column(db.String(60), db.ForeignKey('events.id'), nullable=False)
    name = db.Column(db.String(128), nullable=False)
    description = db.Column(db.String(1024), nullable=True)

    members = db.relationship('User', secondary='committee_member',
                           back_populates='member_committees', lazy=True)
    vices = db.relationship('User', secondary='committee_vice',
                         back_populates='vice_committees', lazy=True)
    heads = db.relationship('User', secondary='committee_head',
                         back_populates='head_committees', lazy=True)
    dashboard = db.relationship('Dashboard', back_populates='committee', lazy=True)
    event = db.relationship('Event', back_populates='committees', lazy=True)
