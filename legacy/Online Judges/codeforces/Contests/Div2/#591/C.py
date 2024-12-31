import sys
import os
import math

def READ(fileName):
    script_dir = os.path.dirname(__file__)
    username = "trifiasco"
    if username in script_dir:
        sys.stdin = open(script_dir + '/' + fileName, 'r')

def process(prices, x, a, y, b, k):
        prices.sort(reverse=True)
        #print(prices)

        total = 0

        first = 0
        second = 0
        curr = 1
        cnt = 0

        results = [0 for x in range(n)]
        new_prices = [0 for x in range(n)]

        for index in range(a - 1, n , a):
            if second == n:
                break
            p = prices[second]
            now = (p // 100) * (x)
            second += 1
            results[index] += now
            new_prices[index] = p

        #print(results, new_prices)

        for index in range(b - 1, n , b):
            if results[index] != 0:
                p = new_prices[index]
                now = (p // 100) * (y)
                #print(now)
                results[index] += now
            else:
                if second == n:
                    break
                p = prices[second]
                now = (p // 100) * (y)
                second += 1
                results[index] += now
        #print(results)

        total = 0
        cnt = 0
        for i in range(n):
            total += results[i]
            cnt += 1
            if total >= k:
                break

        if total >= k:
            return cnt
        else:
            return -1

if __name__ == "__main__":
    READ('in.txt')
    q = int(input())

    while q != 0:
        n = int(input())

        prices = list(map(int, input().split()))

        x, a = map(int, input().split())
        y, b = map(int, input().split())
        
        k = int(input())

        if y > x:
            x, y = y, x
            a, b = b, a
        res1 = process(prices, x, a, y, b, k)
        res2 = process(prices, y, b, x, a, k)

        
        if res1 != -1 and res2 != -1:
            print(min(res1, res2))
        
        else:
            if(res1 != -1):
                print(res1)
            elif res2 != -1:
                print(res2)
            else:
                print('-1')
        


        q -= 1

    pass

