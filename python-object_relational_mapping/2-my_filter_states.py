#!/usr/bin/python3
"""
takes an arg and displays all values
in states table of hbtn_0e_0_usa
where name matches the arg.
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

    # execute the SQL query using format per task requirements
    cur.execute(
        (
            "SELECT * FROM states "
            "WHERE states.name = '{a}' "
            "ORDER BY states.id ASC"
        ).format(a=sys.argv[4])
    )

    # using f - string:
    # cur.execute(
    #     (
    #         f"SELECT * FROM states "
    #         f"WHERE states.name = '{sys.argv[4]}' "
    #         f"ORDER BY states.id ASC"
    #     )
    # )

    # using parameter placeholders:
    # sql_query = (
    #     "SELECT * FROM states WHERE states.name = %s "
    #     "ORDER BY states.id ASC"
    # )
    # arg = sys.argv[4]
    # cur.execute(sql_query, (arg,))

    # fetch single tuple per task output
    result = cur.fetchone()

    print(result)
