#!/usr/bin/python3
import calculator_1 as calcs
a = 10
b = 5
if __name__ == "__main__":
    print(str(a), "+", str(b), "=", str(calcs.add(a, b)))
    print(str(a), "-", str(b), "=", str(calcs.sub(a, b)))
    print(str(a), "*", str(b), "=", str(calcs.mul(a, b)))
    print(str(a), "/", str(b), "=", str(calcs.div(a, b)))
