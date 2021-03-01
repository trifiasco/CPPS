import sys
import math

sys.stdin = open('/home/trifiasco/my world/github-trifiasco/CPPS/codeforces/Contests/Div2/#588/in.txt', 'r')

if __name__ == "__main__":
    
    while True:
        try:
            n, k = input().split()
            n = int(n)
            k = int(k)
        except EOFError:
            break

        s = list(input())
        #print(s)
        for i in range(n):
            if(i == 0):
                if(n == 1 and k > 0):
                    s[i] = '0'
                    k -= 1
                elif(s[i] == '1'):
                    continue
                else:
                    if s[i] != '1' and k > 0:
                        s[i] = '1'
                        k -= 1
                    
            else:
                if s[i] != '0' and k > 0:
                    s[i] = '0'
                    k -= 1
                
        print("".join(s))

     
  
    pass

