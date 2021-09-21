import sys
import os
from typing import List

LOCAL_ENV: bool = os.environ.get('USER') == 'trifiasco'

class Solution:
    pass
        

def READ():
    sys.stdin = open('in.txt', 'r');
    #sys.stdout = open('out.txt', 'w');
    pass

if __name__ == "__main__":
    if LOCAL_ENV:
        READ()

    while True:
        try:
            list_ = list(map(int, input().split(",")))
            sol = Solution()
            # add method name below
            print(sol.(list_))
            # do stuff
        except EOFError:
            break
    pass
