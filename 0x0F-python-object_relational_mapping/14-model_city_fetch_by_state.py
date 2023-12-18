#!/usr/bin/python3
"""
Module that lists all State objects from the database hbtn_0e_14_usa
"""

import sys
import os
from sqlalchemy import create_engine
from model_state import State
from model_city import City
from sqlalchemy.orm import sessionmaker

Session = sessionmaker()

if __name__ == "__main__":
    username = sys.argv[1]
    pwd = sys.argv[2]
    host = "localhost" if "ON_MYMACHINE" not in os.environ else "127.0.0.1"
    db = sys.argv[3]

    engine = create_engine(
        f"mysql+mysqldb://{username}:{pwd}@{host}/{db}",
        pool_pre_ping=True,  # echo=True
    )
    Session.configure(bind=engine)  # once engine is available

    session = Session()

    cities = session.query(City, State).join(
        State, City.state_id == State.id).all()
    if not cities:
        print("Nothing")
        exit(1)
    else:
        for city, state in cities:
            print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()
