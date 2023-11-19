#!/usr/bin/python3
"""This module contains a script which
lists all states starting with "N" from the hbtn_0e_0_usa database
No ORM is used in this case there it needs
understanding of MySQL queries
"""
import sys
import mariadb


connect = mariadb.connect(
        user=sys.argv[1],
        password=sys.argv[2],
        host="localhost",
        port=3306,
        database="hbtn_0e_0_usa"
        )

if __name__ == "__main__":
    cur = connect.cursor()
    cur.execute("""SELECT * FROM states
                WHERE states.name like 'N%'
                ORDER BY states.id ASC""")
    for row in cur.fetchall():
        print(row)
