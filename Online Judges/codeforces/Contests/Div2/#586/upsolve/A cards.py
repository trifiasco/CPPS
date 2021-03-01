import sys
import math

sys.stdin = open('/home/trifiasco/my world/github-trifiasco/CPPS/codeforces/Contests/Div2/#586/upsolve/in.txt', 'r')

if __name__ == "__main__":
    while True:
        try:
            n = int(input())
        except EOFError:
            break

        text = input()

        ones = 0
        zeros = 0

        for char in text:
            if(char == 'n'):
                ones += 1
            elif(char == 'z'):
                zeros += 1
        
        output = ''
        for i in range(ones):
            output += '1 '
        for i in range(zeros):
            output += '0 '
        
        print(output)


    pass

