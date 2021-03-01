import sys
import os
import math


def READ(fileName):
    script_dir = os.path.dirname(__file__)
    username = "trifiasco"
    if username in script_dir:
        sys.stdin = open(script_dir + '/' + fileName, 'r')


if __name__ == "__main__":
    # READ('in.txt')
    print('this is a test')
    pass
