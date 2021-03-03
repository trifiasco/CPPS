import sys
import os
import math

LOCAL_ENV: bool = os.environ.get('USER') == 'trifiasco'


def READ(fileName):
    sys.stdin = open(
        '{path}/{fileName}'.format(path=os.path.dirname(__file__), fileName=fileName), 'r')


if __name__ == "__main__":
    if LOCAL_ENV:
        READ('in.txt')

    while True:
        try:
            n = int(input())
            # do stuff
        except EOFError:
            break
    pass
