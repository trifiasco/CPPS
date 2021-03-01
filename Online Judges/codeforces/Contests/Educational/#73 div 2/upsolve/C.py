import sys
import math

#sys.stdin = open('in.txt', 'r')

def solve(a:int, b:int, c:int):
    ideal = min(a, b)
    a -= ideal
    b -= ideal

    rest = a + b + c
    option2 = ideal - math.ceil((ideal - rest) / 3)
    ideal = min(ideal, option2)

    print(ideal) 

if __name__ == "__main__":
    q = int(input())

    while q != 0:
        a, b, c = input().split()
        solve(int(a), int(b), int(c))
        q -= 1

    pass

