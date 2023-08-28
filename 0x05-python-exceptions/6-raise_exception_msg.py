#!/usr/bin/python3
def raise_exception_msg(message=""):
    try:
        leng("help")
    except NameError:
        print(message)
