#!/usr/bin/python3
"""
prints the State object with the name passed as argument
from the database hbtn_0e_6_usa
"""

from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
import sys
from model_state import Base, State
from sqlalchemy.exc import NoResultFound

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

    # handles open & close session
    with Session(engine) as session:
        # get state name to search
        search_term = sys.argv[4]

        # build query statement
        stmt = select(State).where(State.name == search_term)

        # execute statement & fetch one result
        try:
            results = session.execute(stmt).scalars().one()
            print(results.id)
            # expected one, but no results returned
        except NoResultFound:
            print("Not Found")
