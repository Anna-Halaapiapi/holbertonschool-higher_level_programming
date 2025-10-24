#!/usr/bin/python3
"""
changes the name of a State object
from the database hbtn_0e_6_usa
"""

from sqlalchemy import create_engine, update
from sqlalchemy.orm import Session
import sys
from model_state import Base, State
from sqlalchemy.dialects.mysql import insert

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
        # build update stmt
        stmt = update(State).where(State.id == 2).values(name="New Mexico")
        # execute stmt and commit transaction
        session.execute(stmt)
        session.commit()
