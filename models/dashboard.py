#!/usr/bin/env python3
"""This module contains the Dashboard class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Dashboard(BaseModel, Base):
    """This class represents the dashboard table"""
    __tablename__ = 'dashboards'

    event_id = Column(String(60), ForeignKey('events.id',
                                             onupdate='CASCADE',
                                             ondelete='CASCADE'),
                      nullable=False)

    committee_id = Column(String(60), ForeignKey('committees.id'),
                          nullable=True)

    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    lists = relationship('List', back_populates='dashboard')

    def __init__(self, **kwargs):
        """Initializes the dashboard"""
        super().__init__(**kwargs)
