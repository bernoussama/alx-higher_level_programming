#!/usr/bin/python3

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
    for instance in session.query(State).order_by(State.id):
        print("{}: {}".format(instance.id, instance.name))
    session.close()
