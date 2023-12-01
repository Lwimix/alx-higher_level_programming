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
    try:
        my_json = result.json()
        if my_json:
            print(f"[{my_json['id']}] {my_json['name']}")
        else:
            print("No result")
    except requests.exceptions.JSONDecodeError:
        print("Not a valid JSON")
