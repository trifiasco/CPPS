import sys
import math

sys.stdin = open('/home/trifiasco/my world/github-trifiasco/CPPS/codeforces/Contests/Div3/#582/in.txt', 'r')

if __name__ == "__main__":
    t = int(input())

    for i in range(t):
        n = int(input())

        prices = list(map(int, input().split()))

        prices.reverse()

        length = len(prices)

        cnt = 0

        for i in range(1, length, 1):
            #print(i, end=' - ')
            if prices[i] > prices[i - 1]:
                #print(i, end=' ')
                cnt += 1
            prices[i] = min(prices[i], prices[i - 1])
        #print('')
        print(cnt)

    pass

