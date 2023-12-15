#!/usr/bin/python3
"""Start the link's class to the table in the database
"""
import sys

from sqlalchemy import (create_engine)

from model_state import Base, State

from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    enginee = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(enginee)
    Sessionr = sessionmaker(bind=enginee)
    sessioner = Sessionr()
    for instancess in sessioner.query(State).order_by(State.id):
        print(instancess.id, instancess.name, sep=": ")
