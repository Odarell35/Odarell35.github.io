#!/usr/bin/python3
"""Reviews models"""
from models.parent_model import Parentmodel, Base
from sqlalchemy import Column, String, Text, ForeignKey, Integer


class Reviews(Parentmodel, Base):
    """reveiws class"""
    __tablename__ = 'Reviews'
    #Book_id = Column(String(60), ForeignKey("Books.id"), nullable=False)
    #Bookname = Column(String(60), ForeignKey("Books.title"), nullable=False)
    #user_id = Column(String(60), ForeignKey("User.id"), nullable=False)
    #username = Column(String(60), ForeignKey("User.name"), nullable=False)
    Review_text = Column(Text(1024), nullable=False)
    rating = Column(Integer, nullable=False, default=0)

    def __init__(self, *args, **kwargs):
        """initializes Review"""
        super().__init__(*args, **kwargs)
