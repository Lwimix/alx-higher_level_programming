#!/usr/bin/python3
"""This module contains a script which displays all cities
from the hbtn_0e_4_usa database
No ORM is used in this case there it needs
understanding of MySQL queries
"""
import sys
import MySQLdb


if __name__ == "__main__":
    connect = MySQLdb.connect(
            user=sys.argv[1],
            password=sys.argv[2],
            host="localhost",
            port=3306,
            database=sys.argv[3]
            )
    cur = connect.cursor()
    query = """SELECT c.id, c.name, s.name FROM cities c
    INNER JOIN states s ON s.id = c.state_id
    ORDER BY c.id ASC"""
    cur.execute(query)
    for row in cur.fetchall():
        print(row)
    connect.close()
