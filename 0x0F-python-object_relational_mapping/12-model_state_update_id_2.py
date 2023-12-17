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

    engine = create_engine(
        f"mysql+mysqldb://{username}:{pwd}@{host}/{db}",
        pool_pre_ping=True,  # echo=True
    )
    Session.configure(bind=engine)  # once engine is available

    session = Session()
    state_2 = session.query(State).filter(State.id == 2).one_or_none()
    state_2.name = "New Mexico"
    session.commit()
    session.close()
