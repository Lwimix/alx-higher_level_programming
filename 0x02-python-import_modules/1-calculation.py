#!/usr/bin/python3
def calculator ():
    """four calculations at once"""
    a = 10
    b = 5
    import calculator_1 as calcs
    print (str (a), "+", str (b), "=", str (calcs.add(a,b)))
    print (str (a), "-", str (b), "=", str (calcs.sub(a,b)))
    print (str (a), "*", str (b), "=", str (calcs.mul(a,b)))
    print (str (a), "/", str (b), "=", str (calcs.div(a,b)))
if __name__ == "__main__":
    calculator()
