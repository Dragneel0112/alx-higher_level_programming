#!/usr/bin/python3
""" Lists a state specified in args from the database"""

import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC",
                (argv[4],))
    row = cur.fetchall()
    for r in row:
        print(r)
    cur.close()
    db.close()
