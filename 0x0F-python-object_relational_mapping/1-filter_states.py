#!/usr/bin/python3
""" Lists all states from the database with names starting with N """
import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=argv[1],
                         passwd=argv[2], db=argv[3], port=3306)
    cur = db.cursor()
    cur.execute("""SELECT * FROM states WHERE name
                LIKE 'N%' ORDER BY states.id ASC """)
    row = cur.fetchall()
    for r in row:
        print(r)
    cur.close()
    db.close()
