#!/usr/bin/python3
"""
takes the name of a state as an arg,
lists all cities of that state
using the database hbtn_0e_4_usa
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
        (
        f"SELECT cities.name "
        f"FROM cities "
        f"INNER JOIN states "
        f"ON cities.state_id = states.id "
        f"WHERE states.name = '{sys.argv[4]}'"
        f"ORDER BY cities.id ASC"
        )
    )

    # fetch and print results
    results = cur.fetchall()

    for row in results[0:-1]:
        if row is not None:
            print(f"{row[0]}, ", end='')
    print(row[0])