#!/usr/bin/python3
""" This script takes in a letter and sends a
POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter
"""
if __name__ == "__main__":
    import requests
    import sys

    def search_api(val=""):
        var = {"q": val}
        url = "http://0.0.0.0:5000/search_user"
        respo = requests.post(url, data=var)
        return respo

    param = ""
    if len(sys.argv) == 2:
        param = sys.argv[1]
    result = search_api(param)
    if len(result.text) != 0:
        my_dict = dict(result.text)
        print(my_dict["name"])
