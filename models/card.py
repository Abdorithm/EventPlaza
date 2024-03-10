#!/usr/bin/env python3
"""This module contains the Card class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Table


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
    list_id = Column(String(60), ForeignKey('lists.id', onupdate='CASCADE',
                                            ondelete='CASCADE'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))

    def __init__(self, *args, **kwargs):
        """Initializes a Card object"""
        super().__init__(*args, **kwargs)
