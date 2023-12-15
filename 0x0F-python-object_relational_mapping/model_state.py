#!/usr/bin/python3
"""
Contains all the State class and the Base,
an instance thats of declarative_base()
"""
from sqlalchemy import Column, String, Integer, MetaData
from sqlalchemy.ext.declarative import declarative_base

my_metaData = MetaData()
Base = declarative_base(metadata=my_metaData)


class State(Base):
    """
    Class thats with id and the name attributes
    thats of each state
    """
    __tablename__ = 'states'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
