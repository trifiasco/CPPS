
import sys
import os

LOCAL_ENV: bool = os.environ.get('USER') == 'trifiasco'

def solve(arr, n):
    dp = dict();

    for i in range(1001):
        dp[i] = 0;

    for i in range(n):

        current = arr[i];

        for j in range(current[0], current[1] + 1):
            dp[j] += 1;


    res = 0;

    for i in range(1001):
        if dp[i] == n:
            res += 1;

    return res;

def READ():
    sys.stdin = open('in.txt', 'r');
    #sys.stdout = open('out.txt', 'w');

if __name__ == "__main__":
    if LOCAL_ENV:
        READ()


    # sys.setrecursionlimit(200000)
    while True:
        try:
            n = int(input())

            a = list(map(int, input().split()))
            b = list(map(int, input().split()))

            combined = []
            for i in range(n):
                combined.append((a[i], b[i]));


            combined.sort(key=lambda a: a[0]);

            print(solve(combined, n))
            # do stuff
        except EOFError:
            break
    pass
