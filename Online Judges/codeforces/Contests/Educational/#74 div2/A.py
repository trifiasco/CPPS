import sys
import os
import math

def READ(fileName):
    script_dir = os.path.dirname(__file__)
    username = "trifiasco"
    if username in script_dir:
        sys.stdin = open(script_dir + '/' + fileName, 'r')


def sieve():
    size = 1000000

    primes = []
    marked = [0 for x in range(size)]

    sqr_sz = int(math.sqrt(size))

    for i in range(3, sqr_sz, 2):
        if marked[i] == 0:
            for j in range(i*i, size, i):
                marked[j] = 1

    primes.append(2)
    for i in range(size):
        if marked[i] == 0:
            primes.append(i)

    return primes

def isPrime(primes)

if __name__ == "__main__":
    READ('in.txt')

    primes = sieve()

    t = int(input())

    for i in range(t):
        x, y = map(int, input().split())

        diff = x - y



    pass

