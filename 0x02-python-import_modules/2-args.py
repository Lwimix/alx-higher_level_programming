#!/usr/bin/python3
def args (argv):
    """argument info"""
    if len(argv) == 1:
        print ("0 arguments")
    else:
        no = 1
        arg = "argument"
        args = "arguments"
        print (str (len(argv) - 1), args if len(argv) > 1 else arg, ":")
        while no <  len(argv):
            print (str(no), ":", argv[no])
            no = no + 1
import sys
if __name__ == "__main__":
    args (sys.argv)
