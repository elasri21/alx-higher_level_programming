#!/usr/bin/python3
"""This module gets a state passws as a fourth
argument in a safe way from a database"""
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
    cur.execute("SELECT * FROM states WHERE states.name=%s ORDER BY id ASC",
               (args[4],))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
