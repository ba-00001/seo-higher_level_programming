#!/usr/bin/python3
"""Changes the name of a State object in the database"""


import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Connect to the MySQL server using command-line arguments
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session instance
    session = Session()

    # Query the State object with id = 2
    state = session.query(State).filter(State.id == 2).first()

    # Update the name of the State to "New Mexico"
    state.name = "New Mexico"

    # Commit the session to persist the changes in the database
    session.commit()
