import sys
import os
import math

def READ(fileName):
    script_dir = os.path.dirname(__file__)
    username = "trifiasco"
    if username in script_dir:
        sys.stdin = open(script_dir + '/' + fileName, 'r')


if __name__ == "__main__":
    READ('in.txt')
    q = int(input())

    while q != 0:
       
        s = list(input())
        t = list(input())
        #print(s)
        length = len(s)
        flag = 1

        if length == 1:
            if s != t:
                flag = 0
        
        else:
            flag = 0
            frequency = [0 for x in range(26)]
            for i in range(length):
                char = ord((s[i])) - 97
                frequency[char] = 1
            
            for i in range(length):
                char = ord((t[i])) - 97
                if frequency[char] == 1:
                    flag = 1
                    break
            
        if flag :
            print("YES")
        else:
            print("NO")
        q -= 1

    pass

