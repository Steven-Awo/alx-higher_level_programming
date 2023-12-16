#!/usr/bin/python3
"""
Creating the State of "California" and with the City of
"San Francisco" from the mysql DB
"""
import sys

from relationship_state import  State, Base

from sqlalchemy import (create_engine)

from relationship_city import City

from sqlalchemy.orm import relationship

from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    enginee = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(enginee)

    Sessionner = sessionmaker(bind=enginee)
    sessionner = Sessionner()

    for instancer in sessionner.query(State).order_by(State.id):
        for city_instnc in instancer.cities:
            print(city_instnc.id, city_instnc.name, sep=": ", end="")
            print(" -> " + instancer.name)
