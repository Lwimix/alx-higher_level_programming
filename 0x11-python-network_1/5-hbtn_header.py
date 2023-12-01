#!/usr/bin/python3
""" This module takes in a URL, sends a reuest to it for a
variable X-Request-Id and displays this value. It only
imports from requewts and sys packages
"""
if __name__ == "__main__":
    import requests
    import sys
    url = sys.argv[1]
    response = requests.get(url)
    headers = response.headers
    my_header = headers.get('X-Request-Id')
    print(my_header)
