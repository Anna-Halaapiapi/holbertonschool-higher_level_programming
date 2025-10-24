#!/usr/bin/python3
"""
adds the State object “Louisiana”
to the database hbtn_0e_6_usa
"""

from sqlalchemy import create_engine, select
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
        # manually check if record already exists
        exists_stmt = select(State.name).where(State.name == "Louisiana")
        exists_result = session.execute(exists_stmt).scalars().all()

        # add record if one doesn't exist
        if len(exists_result) == 0:
            new_state = State(name="Louisiana")
            session.add(new_state)
            session.commit()

        # # query to check whole table
        # check_table = select(State).order_by(State.id)
        # check_table_result = session.execute(check_table).scalars().all()
        # for item in check_table_result:
        #     print(f"{item.id}: {item.name}")

        # Print the new states.id after creation
        get_id = (
            select(State)
            .order_by(State.id.desc())
            .where(State.name == "Louisiana"))
        last_record = session.execute(get_id).scalars().first()
        print(last_record.id)
