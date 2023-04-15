#!/usr/bin/python3
""" Lists cities from database with their state"""

import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", charset="utf8", user=argv[1],
                         passwd=argv[2], db=argv[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM \
                cities INNER JOIN states ON states.id=cities.state_id")
    row = cur.fetchall()
    for r in row:
        print(r)
    cur.close()
    db.close()
