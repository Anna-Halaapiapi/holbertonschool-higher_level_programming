#!/usr/bin/python3
"""
takes an arg and displays all values
in states table of hbtn_0e_0_usa
where name matches the arg using parameter
placeholders instead of format string.
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

    # using parameter placeholders:
    sql_query = (
        "SELECT * FROM states WHERE BINARY states.name = %s "
        "ORDER BY states.id ASC"
    )
    arg = sys.argv[4]
    cur.execute(sql_query, (arg,))

    # fetch single tuple per task output
    row = cur.fetchone()

    while row is not None:
        print(row)
        row = cur.fetchone()
