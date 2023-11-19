#!/usr/bin/python3
"""This module contains a script which handles
data from the hbtn_0e_0_usa database
No ORM is used in this case there it needs
understanding of MySQL queries
"""
import sys
import mySQLdb
try:
    connect = mySQLdb.connect(
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
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    for row in cur.fetchall():
        print(row)
