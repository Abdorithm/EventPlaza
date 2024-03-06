#!/usr/bin/env python3
"""Starts the storage engine"""
from models.engine.db_storage import DBStorage


storage = DBStorage()
storage.reload()
