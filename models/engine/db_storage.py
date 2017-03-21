#!/usr/bin/python3
import os
from models import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DBStorage:
    __engine = None
    __session = None

    def init(self):
        user = os.getenv('HBNB_MYSQL_USER')
        pwd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db = os.getenv('HBNB_MYSQL_DB')

        if os.getenv('HBNB_MYSQL_ENV') == "test":
            """ drop all tables """

        """ host port needed? """
        self.__engine = create_engine(
                "mysql://{}:{}@{}/{}".format(user, pwd, host, db))


    def all(self, cls=None):
        queryList = ["User", "State", "City", "Amenity", "Place", "Review"]
        queryDict = {}
        s = self.__session
        if cls is None:
            for data in s.query(queryList):
                queryDict[data.id] = data
        else:
            for data in s.query(cls):
                queryDict[data.id] = data
        return queryDict


    def new(self, obj):
        s = self.__session
        if obj is not None:
            s.add(obj)

    def save(self):
        s = self.__session
        s.commit()

    def delete(self, obj=None):
        s = self.__session
        if obj is not None:
            s.delete(obj)

    def reload(self):
        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()
