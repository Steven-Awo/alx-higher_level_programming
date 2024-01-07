#!/usr/bin/python3
"""
Write a Python script that takes your GitHub
credentials (username and passwordd) and uses
the GitHub API to display your id
"""

import sys

from requests import get

from requests import auth

if __name__ == "__main__":
    urlls = 'https://api.github.com/user'
    userr = sys.argv[1]
    passwordd = sys.argv[2]
    rqts = get(urlls, auth=auth.HTTPBasicAuth(userr, passwordd))
    print(rqts.json().get('id'))
