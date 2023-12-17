#!/usr/bin/python3
"""
class definition of a State and an instance Base = declarative_base()
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# from sqlalchemy import create_engine
# import sys
# import os


Base = declarative_base()


class State(Base):
    """
    class definition of a State
    """

    __tablename__ = "states"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)


# if __name__ == "__main__":
#     username = sys.argv[1]
#     pwd = sys.argv[2]
#     host = "localhost" if "ON_MYMACHINE" not in os.environ else "127.0.0.1"
#     db = sys.argv[3]
#
#     engine = create_engine(
#         f"mysql+mysqldb://{username}:{pwd}@{host}/{db}", pool_pre_ping=True
#     )
#     Base.metadata.create_all(engine)
