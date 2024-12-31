import sys
import math

#sys.stdin = open('in.txt', 'r')

def solve(n:int):

    for i in range(n):
        line = ''
        for j in range(n):
            if (i + j) % 2 == 0:
                line += 'W'
            else:
                line += 'B'
        print(line)
    return

if __name__ == "__main__":

    n = int(input())

    solve(n)

    pass

