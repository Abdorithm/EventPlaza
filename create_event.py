#!/usr/bin/env python3
from models import storage


for key, value in storage.all('Event').items():
    print(key, value)

