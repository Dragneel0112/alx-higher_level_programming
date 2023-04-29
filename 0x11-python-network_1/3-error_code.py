#!/usr/bin/python3
"""
Using URLlib and sys to send requests and handle errors
"""


if __name__ == "__main__":
    from sys import argv
    from urllib import request, error

    try:
        with request.urlopen(argv[1]) as res:
            print(res.read().decode('UTF-8'))
    except error.HTTPError as e:
        print('Error code:', e.code)
