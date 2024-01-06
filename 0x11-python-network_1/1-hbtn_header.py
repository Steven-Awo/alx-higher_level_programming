#!/usr/bin/python3
"""
Write a Python script that takes in a URL, sends a request
to the URL and displays the value of the X-Request-Id variable
found in the header of the response.
"""
import sys

import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        htmll = response.info()
        print(htmll.get('X-Request-Id'))
