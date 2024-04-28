#!/usr/bin/env python3
"""This module contains the Card class"""
from .base_model import BaseModel
from event_plaza import db


assigns = db.Table('assigns', db.Model.metadata,
               db.Column('card_id', db.String(60),
                      db.ForeignKey('cards.id', onupdate='CASCADE',
                                 ondelete='CASCADE'),
                      primary_key=True),
               db.Column('user_id', db.String(60),
                      db.ForeignKey('users.id', onupdate='CASCADE',
                                 ondelete='CASCADE'),
                      primary_key=True))

class Card(BaseModel, db.Model):
    """This class represents a Card object"""
    __tablename__ = 'cards'

    list_id = db.Column(db.String(60), db.ForeignKey('lists.id'), nullable=False)
    name = db.Column(db.String(128), nullable=False)
    description = db.Column(db.String(1024), nullable=True)
    assignees = db.relationship('User', secondary='assigns',
                            back_populates='assigned_cards', lazy = True)
    list = db.relationship('List', back_populates='cards', lazy = True)
