#!/usr/bin/python3
"""
Using Requests and sys to send request to url and retrieve Id from header
"""
from sys import argv
import requests


if __name__ == "__main__":
    url = argv[1]

    req = requests.get(url)
    print(req.headers.get("X-Request-Id"))
