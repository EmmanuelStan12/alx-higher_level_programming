#!/usr/bin/python3
"""
This file displays all states in mysql
"""
if __name__ == "__main__":
    import sys
    import MySQLdb
    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost", user=user,
        port=3306, database=database, password=password)
    cur = db.cursor()
    cur.execute("SELECT c.id, c.name, s.name FROM cities AS c"
                " LEFT OUTER JOIN states AS s ON c.state_id = "
                "s.id ORDER BY c.id ASC")
    result = cur.fetchall()
    for entry in result:
        print(entry)
    cur.close()
    db.close()
