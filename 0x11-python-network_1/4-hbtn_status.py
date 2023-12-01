#!/usr/bin/python3
""" This script that fetches https://alx-intranet.hbtn.io/status
"""
if __name__ == "__main__":
    import requests
    respo = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type".expandtabs(4), type(respo.text))
    print("\t- content".expandtabs(4), respo.text)
