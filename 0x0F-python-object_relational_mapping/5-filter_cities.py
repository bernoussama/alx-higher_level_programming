#!/usr/bin/python3
""" script that lists all cities from the database hbtn_0e_4_usa """

import MySQLdb
import sys
import os

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} username password database state_name".format(
            sys.argv[0]))
        exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    host = "127.0.0.1" if "ON_MYMACHINE" in os.environ else "localhost"
    state_name = sys.argv[4]

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
        """

SELECT GROUP_CONCAT(cities.name ORDER BY cities.id ASC SEPARATOR ', ')
AS city_names
FROM cities
JOIN states ON state_id = states.id
where states.name = %s
        """,
        (state_name,),
    )  # HERE I have to know SQL to grab all states in my database
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
