#!/usr/bin/python3
"""
Creating the State of "California" and with the City of
"San Francisco" from the mysql DB
"""
import sys

from relationship_state import  State, Base

from sqlalchemy import create_engine

from relationship_city import City

from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    enginee = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(enginee)

    Sessionner = sessionmaker(bind=enginee)
    sessionner = Sessionner()

    newer_State = State(name='California')
    newer_City = City(name='San Francisco')
    newer_State.cities.append(newer_City)

    sessionner.add(newer_State)
    sessionner.add(newer_City)
    sessionner.commit()
