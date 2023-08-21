#!/usr/bin/python3
"""
Prints the ID of the State object with the specified name from the database.
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Create a database engine
    db_user = sys.argv[1]
    db_password = sys.argv[2]
    db_name = sys.argv[3]
    db_connection_string = (
        f'mysql+mysqldb://{db_user}:{db_password}@localhost:3306/{db_name}'
    )
    engine = create_engine(db_connection_string)

    # Create the required tables if they don't exist
    Base.metadata.create_all(engine)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create a new State object and add it to the session
    new_state = State(name='Louisiana')
    session.add(new_state)

    # Query and print the ID of the new State object
    new_instance = session.query(State).filter_by(name='Louisiana').first()
    print(new_instance.id)

    # Commit the changes to the database
    session.commit()
