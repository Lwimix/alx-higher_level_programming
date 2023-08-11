#!/usr/bin/python3
import sys


def infinity(argv):
    args = 0
    idx = 1
    while idx < len(argv):
        args = args + int(argv[idx])
        idx = idx + 1
    print(str(args))


if __name__ == "__main__":
    infinity(sys.argv)
