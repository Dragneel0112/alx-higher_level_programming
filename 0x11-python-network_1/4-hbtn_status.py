#!/usr/bin/python3
"""
Using Requests to GET url and display response
"""

if __name__ == '__main__':
    import requests

    url = requests.get('https://alx-intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(url.text.__class__))
    print("\t- content: {}".format(url.text))
