#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    ret_val = True
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError) as b:
        ret_val = False
        print(f"Exception: {b}", file=sys.stderr)
    finally:
        return ret_val
