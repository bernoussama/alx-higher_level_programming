#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError) as e:
        # sys.stderr.write()
        print(f"Exception: {e}", file=sys.stderr)
        return False
    return True
