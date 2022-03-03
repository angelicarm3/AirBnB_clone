#!/usr/bin/python3
"""
Init file for python package: models
Instances the FileStorage class and calls
on the reload method
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
