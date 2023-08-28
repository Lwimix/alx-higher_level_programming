#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        result = fct(*args)
    except Exception as b:
        result = None
        print(f"Exception: {b}", file=sys.stderr)
    finally:
        return result
