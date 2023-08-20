#!/usr/bin/python3
"""
Starts a link class to a table in the database.
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine

if __name__ == "__main__":
    # Create a database engine
    db_user = sys.argv[1]
    db_password = sys.argv[2]
    db_name = sys.argv[3]
    db_connection_string = """
    f'mysql+mysqldb://{db_user}:{db_password}@localhost/{db_name}'
    """
    engine = create_engine(db_connection_string, pool_pre_ping=True)

    # Create the required tables if they don't exist
    Base.metadata.create_all(engine)
