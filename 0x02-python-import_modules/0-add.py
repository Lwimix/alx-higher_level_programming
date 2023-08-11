#!/usr/bin/python3
def my_addition():
    """adding two numbers"""
    a = 1
    b = 2
    from add_0 import add
    print(str(a), "+", str(b), "=", str(add(a, b)))


if __name__ == "__main__":
    my_addition()
