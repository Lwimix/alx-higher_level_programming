#!/usr/bin/python3
import sys


def args(argv):
    """argument info"""
    if len(argv) == 1:
        print("0 arguments.")
    else:
        no = 1
        ar = "argument:"
        ar = "arguments:"
        if len(argv) > 2:
            ar = "arguments:"
        else:
            ar = "argument:"
        print(str(len(argv) - 1), ar)
        while no < len(argv):
            print(str(no) + ":", argv[no])
            no = no + 1


if __name__ == "__main__":
    args(sys.argv)
