#!/usr/bin/python3
"""
lists all State objects from the database hbtn_0e_6_usa
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
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

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()
    ordered_list = session.query(State).order_by(State.id).all()

    for item in ordered_list:
        print(f"{item.id}: ", end='')
        print(item.name)
