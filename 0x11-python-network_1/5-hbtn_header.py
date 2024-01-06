#!/usr/bin/python3
"""
Write a Python script that takes in a URL, sends a request
to the URL and displays the value of the variable
X-Request-Id in the response header
"""

import sys

import requests

if __name__ == "__main__":
    urlls = sys.argv[1]
    rqts = requests.get(urlls)
    print(rqts.headers.get("X-Request-Id"))
