#!/usr/bin/env python3
"""This module contains the List class"""
from .base_model import BaseModel
from event_plaza import db
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class List(BaseModel, db.Model):
    """This class represents the list table"""
    __tablename__ = 'lists'

    dashboard_id = Column(String(60),
                          ForeignKey('dashboards.id', onupdate='CASCADE',
                                     ondelete='CASCADE'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    cards = relationship('Card', back_populates='list', lazy=True)
    dashboard = relationship('Dashboard', back_populates='lists', lazy=True)
