#!/usr/bin/pyhton3
"""Books Model"""
from models.parent_model import Parentmodel, Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from os import getenv
import models
from sqlalchemy import Column, String, Integer, Float, ForeignKey

class Books(Parentmodel, Base):
    """collection of Books"""
    __tablename__ = 'Books'
    title = Column(String(128))
    Author = Column(String(128))
    Catergory_name = Column(String(128), nullable=False)
    #catergory_number = Column(String(60), ForeignKey('catergory.id'), nullable=False)
    Book_description = Column(String(1024), nullable=False)
    ref_link = Column(String(128), nullable=True)

    def __init__(self, *args, **kwargs):
        """initializes """
        super().__init__(*args, **kwargs)
