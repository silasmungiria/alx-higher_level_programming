#!/usr/bin/python3
"""
Prints the State and City objects from the database.
"""
import sys
from relationship_state import Base, State
from relationship_city import City
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

    # Query and print State and associated City objects
    for state_instance in session.query(State).order_by(State.id):
        print(state_instance.id, state_instance.name, sep=": ")

        for city_instance in state_instance.cities:
            print("    ", end="")
            print(city_instance.id, city_instance.name, sep=": ")
