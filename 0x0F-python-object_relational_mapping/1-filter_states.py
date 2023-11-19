#!/usr/bin/python3
"""This module contains a script which
lists all states starting with "N" from the hbtn_0e_0_usa database
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
    query = "SELECT * FROM states WHERE states.name like 'N%' "
    part_2query = "ORDER BY states.id ASC"
    fullquery = query + part_2query
    cur.execute(fullquery)
    for row in cur.fetchall():
        print(row)
    connect.close()
