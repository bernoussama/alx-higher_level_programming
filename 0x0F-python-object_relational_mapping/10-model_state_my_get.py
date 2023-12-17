#!/usr/bin/python3
"""
Module that lists all State objects from the database hbtn_0e_6_usa
containing a in the name
"""

import sys
import os
from sqlalchemy import create_engine
from model_state import State
from sqlalchemy.orm import sessionmaker

Session = sessionmaker()

if __name__ == "__main__":
    username = sys.argv[1]
    pwd = sys.argv[2]
    host = "localhost" if "ON_MYMACHINE" not in os.environ else "127.0.0.1"
    db = sys.argv[3]
    state_name = sys.argv[4]

    engine = create_engine(
        f"mysql+mysqldb://{username}:{pwd}@{host}/{db}",
        pool_pre_ping=True,  # echo=True
    )
    Session.configure(bind=engine)  # once engine is available

    session = Session()
    instance = session.query(State).filter(
        State.name == state_name).one_or_none()
    if instance is None:
        print("Not found")
    else:
        print("{}".format(instance.id))
    session.close()
