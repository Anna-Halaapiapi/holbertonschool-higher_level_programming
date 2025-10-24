#!/usr/bin/python3
"""
This module defines a City class.
The City class maps to cities table in hbtn_0e_14_usa database.
"""

from sqlalchemy import Column, Integer, String, create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
import sys
from model_state import Base


class City(Base):
    """
    Class that maps to cities table in hbtn_0e_14_usa database.
    """
    # map the class to the states table in the DB
    __tablename__ = 'cities'
    #  map the attributes to the states table columns
    id = Column(
        Integer,
        autoincrement=True,
        unique=True,
        nullable=False,
        primary_key=True
    )
    name = Column(String(128), nullable=False)
    state_id = Column(
        Integer,
        ForeignKey('states.id'),
        nullable=False
        )


if __name__ == "__main__":
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
