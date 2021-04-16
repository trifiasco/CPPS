
import functools
import sys
import os

LOCAL_ENV: bool = os.environ.get('USER') == 'trifiasco'

def compare(a, b):
    if a[1] == b[1]:
        if a[0] > b[0]:
            return -1
        else: 
            return 1;
    else:
        if(a[1] < b[1]):
            return -1
        else:
            return 1
    pass

def NOD(n):
    divisors = 0;

    i = 1
    while i * i <= n:
        if(n % i == 0):
            divisors += 1
            if n / i != i:
                divisors += 1

        i += 1
    return divisors;

def preprocess():

    arr = []
    for i in range(1000):
       divisors = NOD(i + 1);
       arr.append((i + 1, divisors))

    arr.sort(key=functools.cmp_to_key(compare))
    return arr;


def solve(n, case, arr):
    print('Case %d: %d' %(case, arr[n][0]))

def READ():
    sys.stdin = open('in.txt', 'r');
    #sys.stdout = open('out.txt', 'w');

if __name__ == "__main__":
    if LOCAL_ENV:
        READ()

    arr = preprocess()
    T = int(input());

    for i in range(T):
        n = int(input())
        solve(n - 1, i+1, arr)
    # while True:
        # try:
            # n = int(input())
            # # do stuff
        # except EOFError:
            # break
    pass
