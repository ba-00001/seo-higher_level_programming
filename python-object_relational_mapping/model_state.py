#!/usr/bin/python3

"""Start link class to table in database"""


import sys
from model_state import Base, State

from sqlalchemy import create_engine

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://'
                           '{}:{}@localhost/{}'.format(sys.argv[1],
                                                       sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
class State(Base):
    """
    State class to represent a state and its attributes.

    Attributes:
        id: An auto-generated, unique integer representing the state's ID.
        name: A string representing the state's name.
    """
