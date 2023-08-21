#!/usr/bin/python3
"""
Prints the State names and associated City details from the database.
"""
import sys
from model_state import Base, State
from model_city import City
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

    # Query and print State names and associated City details
    for instance in session.query(
        State.name, City.id, City.name
    ).filter(State.id == City.state_id):
        state_name, city_id, city_name = instance
        print(f"{state_name}: ({city_id}) {city_name}")
