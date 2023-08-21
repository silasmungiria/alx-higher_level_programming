#!/usr/bin/python3
"""
Creates the State "California" with the City "San Francisco" in a database.
"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    # Create a database engine
    db_user = sys.argv[1]
    db_password = sys.argv[2]
    db_name = sys.argv[3]
    db_connection_string = (
        f'mysql+mysqldb://{db_user}:{db_password}@localhost:3306/{db_name}'
    )
    engine = create_engine(db_connection_string, pool_pre_ping=True)

    # Create the required tables if they don't exist
    Base.metadata.create_all(engine)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create a new State and City objects
    new_state = State(name='California')
    new_city = City(name='San Francisco')

    # Associate the City with the State
    new_state.cities.append(new_city)

    # Add and commit the changes to the database
    session.add(new_state)
    session.commit()
