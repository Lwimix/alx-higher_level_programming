#!/usr/bin/python3
def real_addition():
    """my addition"""
    a = 1
    b = 2
    from add_0 import add
    print(str(a), "+", str(b), "=", str(add(a, b)))


if __name__ == "__main__":
    real_addition()
