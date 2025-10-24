#!/usr/bin/python3
"""
lists all State objects that contain the letter a
from the database hbtn_0e_6_usa
"""

from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
import sys
from model_state import Base, State

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

        # build query statement
        stmt = select(State).order_by(State.id).where(State.name.like("%a%"))
        # execute statement & fetch results
        results = session.execute(stmt).scalars().all()

        # print per task requirements
        for item in results:
            print(f"{item.id}: {item.name}")
