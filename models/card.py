#!/usr/bin/env python3
"""This module contains the Card class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String


class Card(BaseModel, Base):
    """This class represents a Card object"""
    __tablename__ = 'cards'
    name = Column(String(128), nullable=False)
    description = Column(String(1024))

    def __init__(self, *args, **kwargs):
        """Initializes a Card object"""
        super().__init__(*args, **kwargs)

