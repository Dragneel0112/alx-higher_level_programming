#!/usr/bin/python3
"""
Using Requests and sys to access GitHub and display id
"""
from sys import argv
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    authorize = HTTPBasicAuth(argv[1], argv[2])
    req = requests.get("https://api.github.com/user", auth=authorize)
    print(req.json().get("id"))
