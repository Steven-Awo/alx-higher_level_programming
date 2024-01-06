#!/usr/bin/python3
"""
Write a Python script that fetches
https://alx-intranet.hbtn.io/status with requests package
"""
import requests


if __name__ == "__main__":
    rqt = requests.get('https://alx-intranet.hbtn.io/status')
    tt = rqt.text
    print('Body response:\n\t- type: {}\n\t- content: {}'.format(type(tt), tt))
