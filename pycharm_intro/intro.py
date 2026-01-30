#!/usr/bin/env python3

"""
CS106A Intro
"""

import sys
import platform

def check_version(version):
    vals = version.split('.')
    if len(vals) < 2:
        return float(version) >= 3.8
    outer_version = int(vals[0])
    inner_version = int(vals[1])
    return outer_version >= 3 and inner_version >= 8


def main():
    version = platform.python_version()
    if not check_version(version):
        print("ERROR: You are not using the latest version of Python! You are using version: " + platform.python_version())
        print("Please follow the instructions on the CS106A website to download the latest python version")
        return
    if len(sys.argv) != 2:
        print("Hello, CS106A! Now, try running 'python3 intro.py <YOUR NAME HERE>' in the terminal!")
    else:
        name = " ".join(sys.argv[1:])
        print("Hello, " + name + "! You're done with the PyCharm setup process!")


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
