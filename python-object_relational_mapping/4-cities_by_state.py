#!/usr/bin/python3
"""
lists all cities from the database hbtn_0e_4_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # establish connection to db
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    # create cursor
    cur = conn.cursor()

    # execute query
    cur.execute(
        "SELECT cities.id, cities.name, states.name "
        "FROM cities "
        "INNER JOIN states "
        "ON cities.state_id = states.id "
        "ORDER BY cities.id ASC"
        )

    # fetch and print results
    row = cur.fetchone()

    while row is not None:
        print(row)
        row = cur.fetchone()
