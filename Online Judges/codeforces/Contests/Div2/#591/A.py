import sys
import os
import math

def READ(fileName):
    script_dir = os.path.dirname(__file__)
    username = "trifiasco"
    if username in script_dir:
        sys.stdin = open(script_dir + '/' + fileName, 'r')


if __name__ == "__main__":
    READ('in.txt')
    q = int(input())

    while q != 0:
        n = int(input())

        res = 0
        if n == 2:
            res = 2
        else:
            left = n // 2
            right = n - left

            if left != right:
                res = 1
        
        print(res)



        q -= 1

    pass

