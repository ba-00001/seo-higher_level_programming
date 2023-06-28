#!/usr/bin/python3
"""Adds the State object 'Louisiana' to the database"""


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

    # Create a new State object
    new_state = State(name="Louisiana")

    # Add the new_state to the session
    session.add(new_state)

    # Commit the session to persist the changes in the database
    session.commit()

    # Print the new_state's id
    print(new_state.id)
