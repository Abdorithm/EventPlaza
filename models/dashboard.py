#!/usr/bin/env python3
"""This module contains the Dashboard class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Dashboard(BaseModel, Base):
    """This class represents the dashboard table"""
    __tablename__ = 'dashboards'

    event_id = Column(String(60), ForeignKey('events.id'), nullable=False)
    committee_id = Column(String(60), ForeignKey('committees.id'),
                          nullable=True)

    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    lists = relationship('List', back_populates='dashboard')
    event = relationship('Event', back_populates='dashboards')
    committee = relationship('Committee', back_populates='dashboard')
