#!/usr/bin/python3
"""
Using Requests and sys to request url and post an email request
"""
from sys import argv
import requests


if __name__ == "__main__":
    url = argv[1]
    value = {"email": argv[2]}

    req = requests.post(url, data=value)
    print(req.text)
