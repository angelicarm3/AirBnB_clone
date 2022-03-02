#!/usr/bin/python3
"""
Comments
"""
from datetime import datetime
from models import storage
import uuid


class BaseModel:
    """
    Comments
    """

    def __init__(self, *args, **kwargs):
        """ Class Constructor """
        if kwargs and len(kwargs) != 0:
            del kwargs['__class__']
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    kwargs.update({key: datetime.fromisoformat(value)})
            self.__dict__.update(**kwargs)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """ string rep of class BaseModel """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates the public instance attribute
        updated_at with the current datetime
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values
        of __dict__ of the instance
        """
        new_dict = self.__dict__.copy()
        new_dict.update({'updated_at': self.updated_at.isoformat(),
                         'created_at': self.created_at.isoformat()})
        new_dict["__class__"] = self.__class__.__name__
        return new_dict
