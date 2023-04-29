#!/usr/bin/python3
"""
Using URLlib and sys to send request to url and retrieve Id from header
"""
from sys import argv
import urllib.request

if __name__ == "__main__":
    url = argv[1]

    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as res:
        print(dict(res.headers).get("X-Request-Id"))
