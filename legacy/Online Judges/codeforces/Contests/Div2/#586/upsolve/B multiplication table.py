import sys
import math

sys.stdin = open('/home/trifiasco/my world/github-trifiasco/CPPS/codeforces/Contests/Div2/#586/upsolve/in.txt', 'r')

if __name__ == "__main__":

    while True:
        try:
            n = int(input())
        except EOFError:
            break

        mat = [[0 for x in range(n)] for y in range(n)]

        res = [0 for x in range(n)]

        for i in range(n):
            line = list(map(int, input().split()))
            for j in range(n):
                #inp = int(input())
                mat[i][j] = line[j]

        for i in range(n - 1):
            if i != 0 or i != n - 1:
                res[i] = (mat[i][i - 1] * mat[i][i + 1]) / (mat[i - 1][i + 1])
                res[i] = math.sqrt(res[i])

        res[0] = math.sqrt((mat[0][1] * mat[1][0]) / (res[1] * res[1]))
        res[n - 1] = math.sqrt((mat[n - 1][n - 2] * mat[n - 2][n - 1]) / (res[n - 2]* res[n - 2]))

        for i in range(n):
            print(int(res[i]), end=' ')
        print('')


    pass

