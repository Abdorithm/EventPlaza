#!/usr/bin/env python3
"""This module contains the Task class"""
from .base_model import BaseModel
from event_plaza import db


assigns = db.Table('assigns', db.Model.metadata,
                   db.Column('task_id', db.String(60),
                             db.ForeignKey('tasks.id', onupdate='CASCADE',
                                           ondelete='CASCADE'),
                             primary_key=True),
                   db.Column('user_id', db.String(60),
                             db.ForeignKey('users.id', onupdate='CASCADE',
                                           ondelete='CASCADE'),
                             primary_key=True))

task_attachments = db.Table('task_attachments', db.Model.metadata,
                            db.Column('task_id', db.String(60),
                                        db.ForeignKey('tasks.id', onupdate='CASCADE',
                                                        ondelete='CASCADE'),
                                        primary_key=True),
                            db.Column('attachment_id', db.String(60),
                                        db.ForeignKey('attachments.id', onupdate='CASCADE',
                                                        ondelete='CASCADE'),
                                        primary_key=True))

class Task(BaseModel, db.Model):
    """This class represents a task object"""
    __tablename__ = 'tasks'

    name = db.Column(db.String(128), nullable=False)
    event_id = db.Column(db.String(60), db.ForeignKey('events.id'), nullable=False)
    description = db.Column(db.String(1024), nullable=True)
    assignees = db.relationship('User', secondary='assigns',
                                back_populates='assigned_tasks', lazy=True)
    attachments = db.relationship('Attachment', secondary='task_attachments',
                                  back_populates='task', lazy=True)
    status = db.Column(db.String(128), nullable=False, default='To Do')

class Attachment(BaseModel, db.Model):
    """This class represents an Attachment object"""
    __tablename__ = 'attachments'

    url = db.Column(db.String(256), nullable=False)
    task_id = db.Column(db.String(60), db.ForeignKey('tasks.id'), nullable=False)
    task = db.relationship("Task", back_populates="attachments")

