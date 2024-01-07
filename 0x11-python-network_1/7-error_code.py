#!/usr/bin/python3
"""
Write a Python script that takes in a URL, sends a request
to the URL and displays the body of the response.
"""

import sys

import requests

if __name__ == "__main__":
    rqts = requests.get(sys.argv[1])
    if rqts.status_code >= 400:
        print("Error code: {}".format(rqts.status_code))
    else:
        print(rqts.text)
