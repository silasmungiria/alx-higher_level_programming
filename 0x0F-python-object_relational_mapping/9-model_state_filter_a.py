#!/usr/bin/python3
"""
Prints State objects from the 'hbtn_0e_6_usa' database where,
the name contains 'a'.
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

    # Query and print State objects with names containing 'a'
    for instance in session.query(State).filter(State.name.like('%a%')):
        print(instance.id, instance.name, sep=": ")
