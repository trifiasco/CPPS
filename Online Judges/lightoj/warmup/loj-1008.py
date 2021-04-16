
import sys
import os
import math

LOCAL_ENV: bool = os.environ.get('USER') == 'trifiasco'

def sol(n, case):
    if(n == 1):
        print("Case %d: %d %d" %(case, 1, 1))
        return
    if(n == 2):
        print("Case %d: %d %d" %(case, 1, 2))
        return
    if(n == 3):
        print("Case %d: %d %d" %(case, 2, 2))
        return
    if(n == 4):
        print("Case %d: %d %d" %(case, 2, 1))
        return
    series = math.ceil(math.sqrt(n));
    
    non = 2 * series - 1
    isReversed = series % 2 == 1

    indexN = n % (((series - 1) * (series - 1)) + 1 ) + 1
    halfway = math.ceil(non / 2);

    x = 0
    y = 0
    if indexN <= halfway:
          x = indexN 
          y = series
    else:
          x = series
          y =  halfway - (indexN % series) 

    if isReversed:
        x,y = y,x
    print("Case %d: %d %d" %(case, x, y))
    return

def READ():
    #sys.stdin = open('in.txt', 'r');
    #sys.stdout = open('out.txt', 'w');
    pass

if __name__ == "__main__":
    if LOCAL_ENV:
        READ()
    T = int(input())
    for i in range(T):
        n = int(input())
        sol(n, i + 1);
