import sys
import math

sys.stdin = open('/home/trifiasco/my world/github-trifiasco/CPPS/codeforces/Contests/Div3/#582/in.txt', 'r')

if __name__ == "__main__":
    while True:
        try:
            n = int(input())
        except EOFError:
            break

        ordinates = list(map(int, input().split()))

        mp = dict()

        for x in ordinates:
            if mp.get(x, 0) == 0:
                mp[x] = 0
            mp[x] += 1

        unique_ordinates = list(mp)

        res = None

        for key in unique_ordinates:
            #print('key' + str(key))
            current_value = 0
            for oKey in unique_ordinates:
                if oKey == key:
                    continue

                diff = abs(key - oKey)
                diff %= 2

                current_value += diff * mp[oKey]
            #print(current_value)
            if res is None:
                res = current_value
            else:
                if current_value < res:
                    res = current_value

        print(res)

    pass

