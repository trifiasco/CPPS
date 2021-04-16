
import sys
import os

LOCAL_ENV: bool = os.environ.get('USER') == 'trifiasco'

def solve(case):
    x1,y1,x2,y2 = map(int, input().split())
    query = int(input())

    print("Case %d:" %(case))
    for i in range(query):
        x,y = map(int, input().split());

        if (x >= x1 and x <= x2) and (y >= y1 and y <= y2):
            print("Yes");
        else:
            print("No")

def READ():
    sys.stdin = open('in.txt', 'r');
    #sys.stdout = open('out.txt', 'w');

if __name__ == "__main__":
    if LOCAL_ENV:
        READ()

    T = int(input());

    for i in range(T):
        solve(i + 1);
    # while True:
        # try:
            # n = int(input())
            # # do stuff
        # except EOFError:
            # break
    pass
