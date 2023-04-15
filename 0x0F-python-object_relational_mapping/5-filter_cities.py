#!/usr/bin/python3
""" Lists cities from database specified by their state in args"""

import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", charset="utf8", user=argv[1],
                         passwd=argv[2], db=argv[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities JOIN states ON \
                cities.state_id = states.id WHERE states.name LIKE %s \
                ORDER BY cities.id", (argv[4],))
    row = cur.fetchall()
    print(", ".join(city[0] for city in row))
    cur.close()
    db.close()
