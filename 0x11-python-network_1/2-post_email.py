#!/usr/bin/python3
""" This module takes in a URL and an email, sends a
POST request to the URL with the email as a parameter
and returns the body of the response decoded in utf-8
"""
if __name__ == "__main__":
    from urllib.request import urlopen, Request
    import sys
    from urllib.parse import urlencode
    url = sys.argv[1]
    value = sys.argv[2]
    variable = {"email": value}
    variable_encoded = urlencode(variable).encode("utf-8")
    req = Request(url, variable_encoded, method="POST")
    with urlopen(req) as resp:
        ret_email = resp.read()
        print(ret_email.decode("utf-8"))
