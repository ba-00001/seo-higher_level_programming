#!/usr/bin/python3
""" This module is used to link a class to a table in a database. """


import sys

from model_state import Base, State

from sqlalchemy import create_engine

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/\
    {}'.format(sys.argv[1], sys.argv[2],
    sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)


class State(Base):
    """
    Represents a state in the database with attributes id and name.

    Attributes:
        id (int): An auto-generated, unique integer representing the state's ID.
        name (str): A string representing the state's name.
    """
    pass
