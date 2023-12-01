#!/usr/bin/python3
""" This script takes in a url, sends it a request
and displays the body of the response, mainly the
error code
"""
if __name__ == "__main__":
    import sys
    from urllib.request import urlopen
    from urllib.error import HTTPError
    url = sys.argv[1]
    try:
        with urlopen(url) as respo:
            response = respo.read()
            print(response.decode('utf-8'))
    except HTTPError as e:
        print(e)
