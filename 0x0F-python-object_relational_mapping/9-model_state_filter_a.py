#!/usr/bin/python3
""" prints the frst State's object from the database called hbtn_0e_6_usa
"""
import sys
from sqlalchemy import (create_engine)
from model_state import Base, State
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    enginee = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(enginee)
    Sessioner = sessionmaker(bind=enginee)
    sessioner = Sessioner()
    for instancers in sessioner.query(State).filter(State.name.like('%a%')):
        print(instancers.id, instancers.name, sep=": ")
