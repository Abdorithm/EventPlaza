from sqlalchemy import Table, Column, String, ForeignKey
from sqlalchemy.orm import relationship
from event_plaza import db

event_organizers = Table(
        'event_organizers',
        db.Model.metadata,
        Column('event_id', String(60), ForeignKey('events.id', onupdate='CASCADE', ondelete='CASCADE'), primary_key=True),
        Column('user_id', String(60), ForeignKey('users.id', onupdate='CASCADE', ondelete='CASCADE'), primary_key=True)
        )

event_attendens = Table(
        'event_attendens',
        db.Model.metadata,
        Column('event_id', String(60), ForeignKey('events.id', onupdate='CASCADE', ondelete='CASCADE'), primary_key=True),
        Column('user_id', String(60), ForeignKey('users.id', onupdate='CASCADE', ondelete='CASCADE'), primary_key=True)
        )
