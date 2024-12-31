import sys
import math
import functools

sys.stdin = open('/home/trifiasco/my world/github-trifiasco/CPPS/codeforces/Contests/Div3/#587/in.txt', 'r')

def compare(s,t):
    if(s[0] > t[0]):
        return 1
    elif s[0] == t[0]:
        if s[1] < t[1]:
            return 1
        
    return 0

if __name__ == "__main__":
    while True:
        try:
            n = int(input())
        except EOFError:
            break

        line = list(map(int, input().split()))

        paired = [(line[x], x) for x in range(n)]

        #paired.sort(key = functools.cmp_to_key(lambda x,y : (x[0] > y[0])))
        paired.sort()
        
        paired.reverse()

        cnt = 0
        total = 0
        res = []

        for x in paired:
            total += x[0] * cnt + 1
            cnt += 1
            res.append(x[1])
        
        print(total)
        
        for x in res:
            print(x + 1, end=' ')
        print('')




    

    pass

