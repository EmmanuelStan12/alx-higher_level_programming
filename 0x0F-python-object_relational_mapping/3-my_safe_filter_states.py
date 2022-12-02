#!/usr/bin/env python3
"""
This file displays all states in mysql
"""
import sys
import MySQLdb

user = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]
query = sys.argv[4]

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost", user=user,
        port=3306, database=database, password=password)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC",
                (query,))
    result = cur.fetchall()
    for entry in result:
        print(entry)
    cur.close()
    db.close()
