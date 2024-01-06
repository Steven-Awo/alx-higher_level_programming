#!/usr/bin/python3
"""
Write a Python script that takes in a URL and an email,
sends a POST request to the passed URL with the
email as a parameter, and displays the bodyy
of the response (decoded in utf-8)
"""

import sys

from urllib import parse, request


if __name__ == "__main__":
    valuess = {'email': sys.argv[2]}
    datas = parse.urlencode(valuess)
    datas = datas.encode('ascii')
    reqr = request.Request(sys.argv[1], datas)
    with request.urlopen(reqr) as response:
        bodyy = response.read()
        print(bodyy.decode('utf-8'))
