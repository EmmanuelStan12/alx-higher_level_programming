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
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost", user=user,
        port=3306, database=database, password=password)
    cur = db.cursor()
    cur.execute("SELECT name FROM cities AS c WHERE c.state_id = "
                "(SELECT id FROM states WHERE name = %s)",
                (state_name,))
    result = cur.fetchall()
    for i, entry in enumerate(result):
        print("{}".format(entry[0]), end="")
        if i != len(result) - 1:
            print(", ", end="")
    print()
    cur.close()
    db.close()
