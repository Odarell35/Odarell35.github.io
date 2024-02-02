#!/usr/bin/python3
"""User model"""
from models.parent_model import Parentmodel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
import models
from flask_login import UserMixin

class User(Parentmodel, Base, UserMixin):
    """user class"""
    __tablename__ = 'User'
    name = Column(String(128), nullable=True)
    surname = Column(String(128), nullable=True)
    email = Column(String(128), nullable=True, unique=True)
    password = Column(String(128), nullable=True)
    
    def __init__(self, *args, **kwargs):
        """initializes """
        super().__init__(*args, **kwargs)
