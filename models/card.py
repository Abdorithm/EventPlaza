#!/usr/bin/env python3
"""This module contains the Card class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Table
from sqlalchemy.orm import relationship


assign = Table('assign', Base.metadata,
               Column('card_id', String(60),
                      ForeignKey('cards.id', onupdate='CASCADE',
                                 ondelete='CASCADE'),
                      primary_key=True),
               Column('user_id', String(60),
                      ForeignKey('users.id', onupdate='CASCADE',
                                 ondelete='CASCADE'),
                      primary_key=True))


class Card(BaseModel, Base):
    """This class represents a Card object"""
    __tablename__ = 'cards'

    list_id = Column(String(60), ForeignKey('lists.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    assignees = relationship('User', secondary=assign,
                            back_populates='assigned_cards')
    list = relationship('List', back_populates='cards')
