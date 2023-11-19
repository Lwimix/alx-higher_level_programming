#!/usr/bin/python3
"""This module contains a script which displays all states
where the argument matches states.name from the hbtn_0e_0_usa database
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
    query = """SELECT * FROM states
    WHERE states.name LIKE '{:s}'
    ORDER BY states.id ASC;""".format(sys.argv[4])
    cur.execute(query)
    for row in cur.fetchall():
        print(row)
    connect.close()
