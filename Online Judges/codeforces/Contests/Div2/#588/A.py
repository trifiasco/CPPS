import sys
import math

sys.stdin = open('/home/trifiasco/my world/github-trifiasco/CPPS/codeforces/Contests/Div2/#588/in.txt', 'r')

if __name__ == "__main__":
    a = list(map(int, input().split()))

    a.sort()

    flag = 0

    if (a[0] + a[1] + a[2]) == a[3]:
        flag = 1
    if a[0] + a[1] + a[3] == a[2]:
        flag = 1
    if a[0] + a[2] + a[3] == a[1]:
        flag = 1
    if a[1] + a[2] + a[3] == a[0]:
        flag = 1
    

    if a[0] + a[1] ==  (a[2] + a[3]):
        flag = 1
    if a[0] + a[2] ==  (a[1] + a[3]):
        flag = 1
    if a[0] + a[3] ==  (a[1] + a[2]):
        flag = 1
    
    if a[1] + a[2] ==  (a[0] + a[3]):
        flag = 1
    if a[1] + a[3] ==  (a[0] + a[2]):
        flag = 1

    if a[2] + a[3] ==  (a[1] + a[0]):
        flag = 1

    if flag == 1:
        print("YES")
    else:
        print("NO")
  
    pass

