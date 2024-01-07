#!/usr/bin/python3
"""
A python script written that sends a request to the particulal
URL and then displays the value of a particular variable
in the response's header
"""

import sys

import requests

if __name__ == "__main__":
    urlls = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])

    rqts = requests.get(urlls)
    committss = rqts.json()
    try:
        for x in range(10):
            print("{}: {}".format(
                committss[x].get("sha"),
                committss[x].get("commit").get("author").get("name")))
    except IndexError:
        pass
