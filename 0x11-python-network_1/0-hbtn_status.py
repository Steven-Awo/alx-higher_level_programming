#!/usr/bin/python3
"""A script written to
- fetch https://alx-intranet.hbtn.io/status using urllib package
"""

if __name__ == '__main__':
    import urllib.request

    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as res:
        contnt = res.read()
        print("Body response:")
        print("\t- type: {}".format(type(contnt)))
        print("\t- content: {}".format(contnt))
        print("\t- utf8 content: {}".format(contnt.decode('utf-8')))
