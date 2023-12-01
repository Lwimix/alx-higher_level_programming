#!/usr/bin/python3
""" This module fetches a url https://alx-intranet.hbtn.io/status
It uses the python package urllib
"""

if __name__ == "__main__":
    from urllib.request import urlopen
    url = "https://alx-intranet.hbtn.io/status"
    with urlopen(url) as response:
        content = response.read()
        print("Body response:")
        print("\t- type:".expandtabs(4), type(content))
        print("\t- content:".expandtabs(4), content)
        print("\t- utf8 content:".expandtabs(4), content.decode('utf-8'))
