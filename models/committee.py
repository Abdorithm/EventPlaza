#!/usr/bin/env python3
"""This module contains the Committee class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Table
from sqlalchemy.orm import relationship

committee_member = Table('committee_member', Base.metadata,
                         Column('committee_id', String(60),
                                ForeignKey('committee.id', onupdate='CASCADE',
                                           ondelete='CASCADE'),
                                primary_key=True),
                         Column('user_id', String(60),
                                ForeignKey('user.id', onupdate='CASCADE',
                                           ondelete='CASCADE'),
                                primary_key=True))


committee_vice = Table('committee_vice', Base.metadata,
                       Column('committee_id', String(60),
                              ForeignKey('committee.id', onupdate='CASCADE',
                                         ondelete='CASCADE'),
                              primary_key=True),
                       Column('user_id', String(60),
                              ForeignKey('user.id', onupdate='CASCADE',
                                         ondelete='CASCADE'),
                              primary_key=True))


committee_head = Table('committee_head', Base.metadata,
                       Column('committee_id', String(60),
                              ForeignKey('committee.id', onupdate='CASCADE',
                                         ondelete='CASCADE'),
                              primary_key=True),
                       Column('user_id', String(60),
                              ForeignKey('user.id', onupdate='CASCADE',
                                         ondelete='CASCADE'),
                              primary_key=True))


class Committee(BaseModel, Base):
    """This class represents the committee table"""
    event_id = Column(String(60), ForeignKey('events.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)

    members = relationship('User', secondary=committee_member,
                           back_populates='member_committees')
    vices = relationship('User', secondary=committee_vice,
                         back_populates='vice_committees')
    heads = relationship('User', secondary=committee_head,
                         back_populates='head_committees')

    def __init__(self, **kwargs):
        """Initializes the committee"""
        super().__init__(**kwargs)
