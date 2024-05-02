#!/usr/bin/env python3
"""This module contains the Dashboard class"""
from .base_model import BaseModel
from event_plaza import db


class Dashboard(BaseModel, db.Model):
    """This class represents the dashboard table"""
    __tablename__ = 'dashboards'

    event_id = db.Column(db.String(60), db.ForeignKey('events.id'), nullable=False)
    committee_id = db.Column(db.String(60), db.ForeignKey('committees.id'),
                          nullable=True)

    name = db.Column(db.String(128), nullable=False)
    description = db.Column(db.String(1024), nullable=True)
    cards = db.relationship('Card', back_populates='dashboard')
    event = db.relationship('Event', back_populates='dashboards')
    committee = db.relationship('Committee', back_populates='dashboard')
