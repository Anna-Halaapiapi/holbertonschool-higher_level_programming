#!/usr/bin/python3
"""
This module defines a State class.
The State class maps to states table in hbtn_0e_6_usa database.
"""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
import sys

# create base class to use sqlalchemy features
Base = declarative_base()


class State(Base):
    """
    Class that maps to states table in hbtn_0e_6_usa database.
    """
    # map the class to the states table in the DB
    __tablename__ = 'states'
    #  map the attributes to the states table columns
    id = Column(
        Integer,
        autoincrement=True,
        unique=True,
        nullable=False,
        primary_key=True
    )
    name = Column(String(128), nullable=False)


# create connection string
username = sys.argv[1]
password = sys.argv[2]
database_name = sys.argv[3]
port = 3306
host = "localhost"
conn_str = (
    f"mysql+mysqldb://{username}:{password}@"
    f"{host}:{port}/{database_name}"
)

# create connection between script and MySQL server
engine = create_engine(conn_str)

# create tables from class in server if they don't exist
Base.metadata.create_all(engine)
