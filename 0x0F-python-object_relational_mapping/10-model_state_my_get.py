#!/usr/bin/python3
"""Prints the State's object thats with the name that was
passed as an argument from database
"""
import sys

from sqlalchemy import (create_engine)

from model_state import Base, State

from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    enginee = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(enginee)
    Session = sessionmaker(bind=enginee)
    sessioner = Session()
    instancer = sessioner.query(State).filter(State.name == (sys.argv[4],))
    try:
        print(instancer[0].id)
    except IndexError:
        print("Not found")
