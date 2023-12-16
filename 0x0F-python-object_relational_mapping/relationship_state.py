#!/usr/bin/python3
"""
Containing the State's class and its Base,
an instance thats of declarative_base()
"""
from sqlalchemy import Column, String, Integer, MetaData
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

my_metaData = MetaData()
Base = declarative_base(metadata=my_metaData)


class State(Base):
    """
    Class thats with id and a name attributes just for each state
    """
    __tablename__ = 'states'
    id = Column(Integer,  nullable=False, unique=True, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="states")
