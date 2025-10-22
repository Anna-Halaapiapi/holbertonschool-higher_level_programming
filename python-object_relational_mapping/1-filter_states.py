#!/usr/bin/python3
"""
script that lists all states with
a name starting with "N" from the db hbtn_0e_0_usa
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

    cur.execute("SELECT * FROM states ORDER BY states.id ASC;")

    # fetch all results from execution
    results = cur.fetchall()

    for row in results:
        if row[1][0] == 'N':
            print(row)
