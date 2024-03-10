#!/usr/bin/env python3
from models.event import Event
from models.user import User

organizer = User(username="Zoo", first_name="John", last_name="Doe",
                 email="hazem@gmail.com", password="1234")
organizer.save()
event = Event(name="PSED", organizer=[organizer])
event.save()

