#!/usr/bin/python3
"""
Useing Requests and sys to request from url and POST variable
"""
from sys import argv
import requests


if __name__ == "__main__":
    data = "" if len(argv) == 1 else argv[1]
    value = {"q": data}

    req = requests.post("http://0.0.0.0:5000/search_user", data=value)
    try:
        res = req.json()
        if res == {}:
            print("No result")
        else:
            print("[{}] {}".format(res.get("id"), res.get("name")))
    except ValueError:
        print("Not a valid JSON")
