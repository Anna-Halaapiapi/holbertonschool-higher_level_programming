#!/usr/bin/python3
"""
a script that lists all states from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys

# establish connection to the db
conn = MySQLdb.connect(
    host="localhost",
    port=3306,
    user=sys.argv[1],
    passwd=sys.argv[2],
    db=sys.argv[3]
)

# create a cursor obj
cur = conn.cursor()

# get all rows of states table in ASC order
cur.execute("SELECT * FROM states ORDER BY states.id ASC")

# fetch all results and print each row
result = cur.fetchall()
for row in result:
    print(row)
