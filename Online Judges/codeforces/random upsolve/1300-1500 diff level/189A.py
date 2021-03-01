import sys, threading
import os
import math

def READ(fileName):
    script_dir = os.path.dirname(__file__)
    username = "trifiasco"
    if username in script_dir:
        sys.stdin = open(script_dir + '/' + fileName, 'r')

def momoize(f):
    dp = {}

    def inner(num, a, b, c):
        if num not in dp:
            dp[num] = f(num, a, b, c)
        return dp[num]
    return inner

@momoize
def solve(n, a, b, c):
    if n == 0:
        return 0
    if n < 0:
        return -4010

    ans = max({1 + solve(n - a, a, b, c), 1 + solve(n - b, a, b, c), 1 + solve(n - c, a, b, c)})
    return ans

def main():
    READ('in.txt')
    while True:
        try:
            n, a, b, c = map(int, input().split())
        except EOFError:
            break

        res = solve(n, a, b, c)
        print(res)
    pass

if __name__ == "__main__":
    sys.setrecursionlimit(200000)
    threading.stack_size(10240000)
    thread = threading.Thread(target=main)
    thread.start()
    

