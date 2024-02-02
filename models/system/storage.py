#!/usr/bin/python3
"""Storage system"""
import models
from models.parent_model import Parentmodel, Base
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models.Review_model import Reviews
from models.User_model import User
from models.Category_model import Category
from models.Books_model import Books


class Data_storage:
    """database storage"""
    __engine = None
    __session = None

    def __init__(self):
        """initialization"""
        USER = getenv('USER')
        PWD = getenv('PWD')
        HOST = getenv('HOST')
        DATABASE = getenv('DATABASE')

        self.__engine = create_engine(f'mysql+mysqldb://{USER}:{PWD}@{HOST}/{DATABASE}',pool_pre_ping=True)

    def data(self, cls=None):
        """returns ojects depending on class
        or  all  data"""
        classes = [Books, Reviews, User, Category]
        database = {}
        if cls is not None:
            query = self.__session.query(cls).all()
            for ins in query:
                key = ins.__class__.__name__ + ':' + str(ins.id)
                database[key] = ins
        else:
            for c in classes:
                query = self.__session.query(c).all()
                for ins in query:
                    key = ins.__class__.__name__ + ':' + str(ins.id)
                    database[key] = ins
        return database

    def new(self, obj):
        """add """
        self.__session.add(obj)

    def save(self):
        """commit """
        self.__session.commit()

    def delete(self, obj=None):
        """delete """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """create tables in the database"""
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(bind=self.__engine, expire_on_commit=False))

    def close(self):
        """close session"""
        self.__session.close()

