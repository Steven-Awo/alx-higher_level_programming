#!/usr/bin/python3
"""
Write a Python script that takes in a URL, sends a
request to the URL and displays the body of the
response (decoded in utf-8).
"""

import sys

from urllib import error, request


if __name__ == "__main__":
    try:
        with request.urlopen(sys.argv[1]) as response:
            bodyy = response.read()
            print(bodyy.decode('utf-8'))
    except error.HTTPError as errr:
        print('Error code: {}'.format(errr.code))
