#!/usr/bin/python3
"""This module lists all cities of that state,
using the database hbtn_0e_4_usa"""
import MySQLdb
import sys

if __name__ == "__main__":
    args = sys.argv
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=args[1],
        passwd=args[2],
        db=args[3],
        charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT cities.name FROM cities "
                "JOIN states ON cities.state_id=states.id "
                "AND states.name=%s ORDER BY cities.id ASC", (args[4],))
    query_rows = cur.fetchall()
    print(', '.join(map(lambda x: x[0], query_rows)))
    cur.close()
    conn.close()
