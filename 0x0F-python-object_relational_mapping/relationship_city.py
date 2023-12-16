#!/usr/bin/python3
"""
Containing the class's definition of any City
"""
from relationship_state import Base

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import Column, String, Integer, ForeignKey


class City(Base):
    """
    Class that helps in defining each city
    """
    __tablename__ = 'cities'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
