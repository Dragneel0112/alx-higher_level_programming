#!/usr/bin/python3
""" Lists a state specified in args from the database"""

import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("""SELECT * FROM states WHERE name LIKE %s
                   ORDER BY states.id ASC""", (sys.argv[4],))
    row = cursor.fetchall()
    for r in row:
        print(r)
    cursor.close()
    db.close()
