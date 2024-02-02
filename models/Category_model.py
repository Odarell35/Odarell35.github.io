#!/usr/bin/python3
"""Category model"""
from models.parent_model import Parentmodel, Base
from sqlalchemy import Column, String, Integer, Float
from sqlalchemy.ext.declarative import declarative_base


class Category(Parentmodel, Base):
    """category class with f.f attr
    category number, name
    """
    __tablename__ = 'Category'
    category_name = Column(String(128), nullable=False)

    def __init__(self, *args, **kwargs):
        """initializes """
        super().__init__(*args, **kwargs)
