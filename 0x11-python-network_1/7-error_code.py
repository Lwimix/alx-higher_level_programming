#!/usr/bin/python3
""" This script takes in a url, sends it a request
and displays the body of the response, mainly the
error code
"""
if __name__ == "__main__":
    import sys
    import requests
    url = sys.argv[1]
    response = requests.get(url)
    if response.status_code >= 400:
        print("Error code:", response.status_code)
    else:
        print(response.text)
