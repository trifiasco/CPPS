import sys
import math

#sys.stdin = open('in.txt', 'r')

relevant = []

power = 1

while True:
    relevant.append(power)
    power *= 2
    if(power > 2048):
        break

query = int(input())

while query != 0:
    n = int(input())
    mp = dict(zip(relevant, [0 for i in range(len(relevant))]))

    nums = list(map(int, input().split()))

    for i in range(n):
        inp = nums[i]
        if(inp > 2048):
            continue
        mp[inp] += 1
    
    for p in relevant:
        if(p == 2048):
            break
        full = mp[p] / 2
        #rem = mp[p] % 2

        mp[p*2] += full
        #mp[]
    
    if(mp[2048] >= 1):
        print("YES")
    else:
        print("NO")
    

    query -= 1
