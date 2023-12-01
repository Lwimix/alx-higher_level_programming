#!/usr/bin/python3
""" This module takes in a URL and an email, sends a
POST request to the URL with the email as a parameter
and returns the body of the response decoded in utf-8
"""
if __name__ == "__main__":
    import requests
    import sys
    url = sys.argv[1]
    value = sys.argv[2]
    variable = {"email": value}
    respo = requests.post(url, data=variable)
    print(respo.text)
