#!/usr/bin/python3
"""
Using URLlib and sys to request url and post an email request
"""
from sys import argv
import urllib


if __name__ == "__main__":
    url = argv[1]
    value = {"email": argv[2]}
    data = urllib.parse.urlencode(value)
    data = data.encode("ascii")

    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as res:
        print(res.read().decode("ascii"))
