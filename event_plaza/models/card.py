#!/usr/bin/env python3
"""This module contains the Card class"""
from .base_model import BaseModel
from event_plaza import db
from sqlalchemy import Column, String, ForeignKey, Table
from sqlalchemy.orm import relationship


assigns = Table('assigns', db.Model.metadata,
               Column('card_id', String(60),
                      ForeignKey('cards.id', onupdate='CASCADE',
                                 ondelete='CASCADE'),
                      primary_key=True),
               Column('user_id', String(60),
                      ForeignKey('users.id', onupdate='CASCADE',
                                 ondelete='CASCADE'),
                      primary_key=True))

class Card(BaseModel, db.Model):
    """This class represents a Card object"""
    __tablename__ = 'cards'

    list_id = Column(String(60), ForeignKey('lists.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    assignees = relationship('User', secondary='assigns',
                            back_populates='assigned_cards', lazy = True)
    list = relationship('List', back_populates='cards', lazy = True)
