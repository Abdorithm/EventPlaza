#!/usr/bin/env python3
"""This module contains the List class"""
from .base_model import BaseModel
from event_plaza import db


class List(BaseModel, db.Model):
    """This class represents the list table"""
    __tablename__ = 'lists'

    dashboard_id = db.Column(db.String(60),
                          db.ForeignKey('dashboards.id', onupdate='CASCADE',
                                     ondelete='CASCADE'), nullable=False)
    name = db.Column(db.String(128), nullable=False)
    description = db.Column(db.String(1024), nullable=True)
    cards = db.relationship('Card', back_populates='list', lazy=True)
    dashboard = db.relationship('Dashboard', back_populates='lists', lazy=True)
