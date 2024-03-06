#!/usr/bin/env python3
from models.event import Event
from models.organizer import Organizer

organizer = Organizer(first_name="John", last_name="Doe")
organizer.save()
event = Event(name="PSED", organizer_id=organizer.id)
event.save()

