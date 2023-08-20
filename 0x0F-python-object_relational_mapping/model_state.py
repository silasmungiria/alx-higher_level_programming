#!/usr/bin/python3
"""
Contains the State class and Base, an instance of declarative_base().
"""
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base

# Define a custom metadata instance
mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)


class State(Base):
    """
    Class representing each state with id and name attributes.
    """
    __tablename__ = 'states'

    # Define attributes/columns
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
