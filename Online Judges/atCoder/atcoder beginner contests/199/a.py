

import sys
import os

LOCAL_ENV: bool = os.environ.get('USER') == 'trifiasco'

def solve(a, b, c):

    left = a * a + b * b;
    right = c * c;

    if left < right:
        print("Yes");

    else:
        print("No")

def READ():
    sys.stdin = open('in.txt', 'r');
    #sys.stdout = open('out.txt', 'w');

if __name__ == "__main__":
    if LOCAL_ENV:
        READ()


    # sys.setrecursionlimit(200000)
    while True:
        try:
            a, b, c = map(int, input().split()) 

            solve(a, b, c)
            # do stuff
        except EOFError:
            break
    pass
