from sqlalchemy import Table, Column, String, ForeignKey
from models.base_model import Base

event_organizers = Table(
        'event_organizers',
        Base.metadata,
        Column('event_id', String(60), ForeignKey('events.id', onupdate='CASCADE', ondelete='CASCADE'), primary_key=True),
        Column('user_id', String(60), ForeignKey('users.id', onupdate='CASCADE', ondelete='CASCADE'), primary_key=True)
        )

event_attendens = Table(
        'event_attendens',
        Base.metadata,
        Column('event_id', String(60), ForeignKey('events.id', onupdate='CASCADE', ondelete='CASCADE'), primary_key=True),
        Column('user_id', String(60), ForeignKey('users.id', onupdate='CASCADE', ondelete='CASCADE'), primary_key=True)
        )
