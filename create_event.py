#!/usr/bin/env python3
"""
Create Dummy Data
"""
from models import storage
from models.event import Event
from models.user import User

event = Event(name="Event_1", description="Description_1")
user1 = User(first_name="Hazem", last_name="Osama", email="hazem@gmail.com", password="password")
user2 = User(first_name="Ahmed", last_name="Osama", email="Ahmed@gmail.com", password="password")
             
storage.new(user1)
storage.new(user2)
storage.new(event)
storage.save()

print(event.id)
for key, value in storage.all('Event').items():
    print(key, value)

