#!/usr/bin/python3
"""This module contains a script which handles
data from the hbtn_0e_0_usa database
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
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    for row in cur.fetchall():
        print(row)
