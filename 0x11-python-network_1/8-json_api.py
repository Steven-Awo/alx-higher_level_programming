#!/usr/bin/python3
"""
Write a Python script that takes in a letterr and
sends a POST request to http://0.0.0.0:5000/search_user
with the letterr as a parameter.
"""

import sys

import requests

if __name__ == "__main__":
    letterr = "" if len(sys.argv) == 1 else sys.argv[1]
    payyloadr = {"q": letterr}

    rqts = requests.post("http://0.0.0.0:5000/search_user",
            data=payyloadr)
    try:
        responsesr = rqts.json()
        if responsesr == {}:
            print("No result")
        else:
            print("[{}] {}".format(responsesr.get("id"),
                responsesr.get("name")))
    except ValueError:
        print("Not a valid JSON")
