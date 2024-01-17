#!/usr/bin/python3
""" Initialize the models package """

from os import getenv

# Check the value of HBNB_TYPE_STORAGE environment variable
storage_type = getenv('HBNB_TYPE_STORAGE')

if storage_type == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

# Load the storage data
storage.reload()
