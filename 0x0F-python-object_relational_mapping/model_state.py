#!/usr/bin/python3
""" This script uses ORM to deal with MySQL
so that you don't have to use MySQL queries.
It contains a State class which connects to the
state table from our database
"""
from sqlalchemy import ForeignKey, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()


class State(Base):
    """This is the state class.
    It inherits from the Base class
    """
    __tablename__ = "states"
    myId = Column("Id", Integer, primary_key=True, nullable=False)
    name = Column("Name", String(128), nullable=False)

    def __init__(*args, **kwargs):
        if args:
            self.myId = args[0]
            self.name = args[1]
        elif kwargs:
            for key, value in kwargs.items:
                setattr(self, key, value)
