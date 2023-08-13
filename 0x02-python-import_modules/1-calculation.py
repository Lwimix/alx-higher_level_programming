#!/usr/bin/python3
import calculator_1 as calcs
a = 10
b = 5
if __name__ == "__main__":
    print("{} + {} = {}".format(a, b, calcs.add(a, b)))
    print("{} - {} = {}".format(a, b, calcs.sub(a, b)))
    print("{} * {} = {}".format(a, b, calcs.mul(a, b)))
    print("{} / {} = {}".format(a, b, calcs.div(a, b)))
