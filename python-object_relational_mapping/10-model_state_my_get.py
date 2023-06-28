#!/usr/bin/python3
"""Prints the State object with the given name from the database"""


import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Connect to the MySQL server using command-line arguments
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session instance
    session = Session()

    # Get the State object with the given name
    state = session.query(State).filter(State.name == sys.argv[4]).first()

    # Print the result
    if state is None:
        print("Not found")
    else:
        print(state.id)
