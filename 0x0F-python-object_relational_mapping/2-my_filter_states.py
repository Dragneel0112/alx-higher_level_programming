#!/usr/bin/python3
""" Lists states from database where name matches argument"""

import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", charset="utf8", user=argv[1],
                         passwd=argv[2], db=argv[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE '{:s}' ORDER BY \
    id ASC".format(argv[4]))
    row = cur.fetchall()
    for r in row:
        if r[1] == argv[4]:
            print(r)
    cur.close()
    db.close()
