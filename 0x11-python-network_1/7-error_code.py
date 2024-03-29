#!/usr/bin/python3
"""
Using Requests and sys to send requests and handle errors
"""
from sys import argv
import requests


if __name__ == "__main__":
    url = argv[1]

    req = requests.get(url)
    if req.status_code >= 400:
        print("Error code: {}".format(req.status_code))
    else:
        print(req.text)
