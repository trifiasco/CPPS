import sys
import math

sys.stdin = open('/home/trifiasco/my world/github-trifiasco/CPPS/codeforces/Contests/Div3/#587/in.txt', 'r')

if __name__ == "__main__":
    n = int(input())

    a = list(input())

    cnt = 0
    a_cnt = 0
    b_cnt = 0

    for i in range(n):
        if a[i] == 'a':
            a_cnt += 1
        elif a[i] == 'b':
            b_cnt += 1
        
        if i != 0 and i % 2 == 1:
            if a_cnt != b_cnt:
                if a[i] == 'a':
                    a[i] = 'b'
                    b_cnt += 1
                    a_cnt -= 1
                    cnt += 1

                elif a[i] == 'b':
                    a[i] = 'a'
                    b_cnt -= 1
                    a_cnt += 1
                    cnt += 1
    
    print(cnt)
    print("".join(a))

    pass

