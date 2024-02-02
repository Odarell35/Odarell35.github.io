#!/usr/bin/python3
"""Parent Model where all the class
will inherit from"""
import uuid
from datetime import datetime
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime
import models

Base = declarative_base()


class Parentmodel:
    """parent model with the f.f attr
       id, created_at, updated_at
    """
    id = Column(String(60), primary_key=True, nullable=False, unique=True)
    created_at = Column(DateTime, default=datetime.utcnow(),nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow(),nullable=False)

    def __init__(self, *args, **kwargs):
        """initialize attr"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if not kwargs:
            from models import storage
            self.id = str(uuid.uuid4())

        else:
            for i, j in kwargs.items():
                if i in ("created_at", "updated_at"):
                    j = datetime.strptime(kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')
                if "__class__" not in i:
                    setattr(self, i, j)

    def __str__(self):
        """String repr of the Parent Model Class"""
        return f"[{self.__class__.__name__}] {self.__dict__}"

    def save(self):
        """updates the attribute 'updated_at' with the current datetime"""
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of the instance"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
            (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        if '_sa_instance_state' in dictionary:
            del dictionary['_sa_instance_state']
        return dictionary
