from event_plaza import db

event_organizers = db.Table(
        'event_organizers',
        db.Model.metadata,
        db.Column('event_id', db.String(60), db.ForeignKey('events.id', onupdate='CASCADE', ondelete='CASCADE'), primary_key=True),
        db.Column('user_id', db.String(60), db.ForeignKey('users.id', onupdate='CASCADE', ondelete='CASCADE'), primary_key=True)
        )

event_attendens = db.Table(
        'event_attendens',
        db.Model.metadata,
        db.Column('event_id', db.String(60), db.ForeignKey('events.id', onupdate='CASCADE', ondelete='CASCADE'), primary_key=True),
        db.Column('user_id', db.String(60), db.ForeignKey('users.id', onupdate='CASCADE', ondelete='CASCADE'), primary_key=True)
        )

event_managers = db.Table(
        'event_managers',
        db.Model.metadata,
        db.Column('event_id', db.String(60), db.ForeignKey('events.id', onupdate='CASCADE', ondelete='CASCADE'), primary_key=True),
        db.Column('user_id', db.String(60), db.ForeignKey('users.id', onupdate='CASCADE', ondelete='CASCADE'), primary_key=True)
        )
