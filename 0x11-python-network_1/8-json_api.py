#!/usr/bin/python3
"""
Write a Python script that takes in a letterr and
sends a POST request to http://0.0.0.0:5000/search_user
with the letterr as a parameter.
"""

import sys

import requests

if __name__ == "__main__":
    letteerr = "" if len(sys.argv) == 1 else sys.argv[1]
    payyloadr = {"q": letteerr}

    rqts = requests.post("http://0.0.0.0:5000/search_user", data=payyloadr)
    try:
        responsesrs = rqts.json()
        if responsesrs == {}:
            print("No result")
        else:
            print("[{}] {}".format(responsesrs.get("id"), responsesrs.get("name")))
    except ValueError:
        print("Not a valid JSON")
