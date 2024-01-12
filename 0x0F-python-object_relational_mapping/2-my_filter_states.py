#!/usr/bin/python3
"""This module gets a state passws as a fourth
argumwnt from a database"""
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
    query = """SELECT * FROM states WHERE states.name
LIKE BINARY '{}' ORDER BY id ASC"""
    query = query.format(args[4])
    cur.execute(query)
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
