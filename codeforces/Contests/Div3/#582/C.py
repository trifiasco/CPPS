import sys
import math

sys.stdin = open('/home/trifiasco/my world/github-trifiasco/CPPS/codeforces/Contests/Div3/#582/in.txt', 'r')

if __name__ == "__main__":
    t = int(input())

    for i in range(t):
        n,m = input().split()
        n = int(n)
        m = int(m)

        cnt = n // m

        if cnt == 0:
            print('0')
            continue
        
        digits = [((x + 1) * m)%10 for x in range(10)]

        digits_sum = sum(digits)
        #print(digits_sum)
        total = digits_sum * (cnt//10)

        rem = cnt % 10

        for i in range(rem):
            total += digits[i]

        print(total)

    pass

