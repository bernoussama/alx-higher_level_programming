#!/usr/bin/python3
"""
Script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa
where name matches the argument safe from MySQL injections
"""

import MySQLdb
import sys
import os

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} username password database name".format(sys.argv[0]))
        exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    name = sys.argv[4]
    host = "127.0.0.1" if "ON_MYMACHINE" in os.environ else "localhost"

    conn = MySQLdb.connect(
        host=host,
        port=3306,
        user=username,
        passwd=password,
        db=database,
        charset="utf8",
    )
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM states WHERE name = %s ORDER BY states.id ASC", (name,)
    )  # HERE I have to know SQL to grab all states in my database
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
