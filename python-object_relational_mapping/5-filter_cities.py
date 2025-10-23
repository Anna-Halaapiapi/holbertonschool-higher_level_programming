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

    # define sql query
    sql_query = (
        "SELECT cities.name "
        "FROM cities "
        "INNER JOIN states "
        "ON cities.state_id = states.id "
        "WHERE states.name = %s "
        "ORDER BY cities.id ASC"
    )

    state = sys.argv[4]

    # execute
    cur.execute(sql_query, (state,))

    # fetch and print results
    results = cur.fetchall()
    
    # find length of list
    results_length = len(results)

    # print results
    for index, row in enumerate(results):
        if row is not None:
            if index != results_length - 1:
                print(f"{row[0]}, ", end='')
            else:
                print(row[0])
