
import sys
import os

LOCAL_ENV: bool = os.environ.get('USER') == 'trifiasco'

def solve(a, b):
    
    plus = [i for i in range(1, a + 1)];
    minus = [-i for i in range(1, b + 1)];

    if a > b:
        diff = a - b;
        sum = 0;
        iterator = b;
        cnt = 0;
        while cnt < diff:
             sum += plus[iterator];
             cnt += 1;
             iterator += 1;

        minus[b - 1] += -sum

    else:
        diff = b - a;

        sum = 0;
        iterator = a;
        cnt = 0;
        while cnt < diff:
             sum += minus[iterator];
             cnt += 1;
             iterator += 1;
        plus[a - 1] += -sum

    for i in range(a):
        print(plus[i], end=" ")
    for i in range(b):
        print(minus[i], end=" ")

    print()

    return;


    

def READ():
    sys.stdin = open('in.txt', 'r');
    #sys.stdout = open('out.txt', 'w');

if __name__ == "__main__":
    if LOCAL_ENV:
        READ()

    while True:
        try:
            a, b = map(int, input().split());
            solve(a, b)
            # do stuff
        except EOFError:
            break
    pass
