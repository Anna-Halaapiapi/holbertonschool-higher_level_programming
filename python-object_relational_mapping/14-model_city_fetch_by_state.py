#!/usr/bin/python3
"""
prints all City objects from
the database hbtn_0e_14_usa
"""

from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
import sys
from model_state import Base, State
from model_city import City

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
        # build query stmt
        stmt = (
            select(State.name, City.id, City.name)
            .join(City, City.state_id == State.id)
            .order_by(City.id))
        # exectute query & get results
        results = session.execute(stmt).all()
        # print results
        for state_name, city_id, city_name in results:
            print(f"{state_name}: ({city_id}) {city_name}")
