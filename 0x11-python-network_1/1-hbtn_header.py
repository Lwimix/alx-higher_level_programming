#!/usr/bin/python3
""" This module takes in a URL, sends a reuest to it for a
variable X-Request-Id and displays this value. It only
imports from urllib and sys packages
"""
if __name__ == "__main__":
    from urllib.request import urlopen
    import sys
    url = sys.argv[1]
    with urlopen(url) as resp:
        header = resp.getheader("X-Request-Id")
        print(header)
