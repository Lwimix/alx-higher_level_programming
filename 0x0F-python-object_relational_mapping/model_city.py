#!/usr/bin/python3
""" This script uses ORM to deal with MySQL
so that you don't have to use MySQL queries.
It contains a City class which connects to the
state table from our database
"""
from sqlalchemy import ForeignKey, Column, String, Integer
from model_state import Base
from sqlalchemy.orm import sessionmaker


class City(Base):
    """This is the City class.
    It inherits from the Base class
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True,
                  nullable=False, autoincrement=True, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, nullable=False, foreign_key="state_id")

    def __init__(*args, **kwargs):
        if args:
            City.name = args
        elif kwargs:
            for key, value in kwargs.items:
                setattr(self, key, value)
