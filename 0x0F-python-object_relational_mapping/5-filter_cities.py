#!/usr/bin/python3
"""This module contains a script which displays all cities
from the hbtn_0e_4_usa database
No ORM is used in this case there it needs
understanding of MySQL queries
"""
import sys
import mariadb

try:
    connect = mariadb.connect(
            user=sys.argv[1],
            password=sys.argv[2],
            host="localhost",
            port=3306,
            database=sys.argv[3]
            )
except mariadb.Error as e:
    print("Error while connecting mariadb")
    sys.exit(1)

if __name__ == "__main__":
    cur = connect.cursor()
    query = f"""SELECT c.name FROM cities c
    INNER JOIN states s
    ON s.id = c.state_id
    WHERE s.name='{sys.argv[4]}'"""
    cur.execute(query)
    new_tup = ()
    for idx, item in enumerate(cur.fetchall()):
        new_tup = new_tup + item
    string = ", ".join(new_tup)
    print(string)
