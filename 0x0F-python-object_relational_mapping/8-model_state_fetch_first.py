#!/usr/bin/python3
"""prints the 1st State object thats from the database
called hbtn_0e_6_usa
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
    instanceer = sessioner.query(State).first()
    if instanceer is None:
        print("Nothing")
    else:
        print(instanceer.id, instanceer.name, sep=": ")
