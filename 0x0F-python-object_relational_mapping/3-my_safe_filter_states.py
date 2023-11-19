#!/usr/bin/python3
"""This module contains a script which displays all states
where the argument matches states.name from the hbtn_0e_0_usa database
It is free from SQL injections. No ORM is used in this case there it needs
understanding of MySQL queries
"""
import sys
import MySQLdb


if __name__ == "__main__":
    def no_injections(username, passwd, database, state_name):
        """
        This function eliminates the possibility of SQL injections
        """
        connect = MySQLdb.connect(
                user=username,
                password=passwd,
                host="localhost",
                port=3306,
                database=database
                )
        cur = connect.cursor()
        query = """SELECT * FROM states
        WHERE states.name LIKE '{:s}'
        ORDER BY states.id ASC;""".format(state_name)
        cur.execute(query)
        for row in cur.fetchall():
            print(row)
        connect.close()

    no_injections(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
