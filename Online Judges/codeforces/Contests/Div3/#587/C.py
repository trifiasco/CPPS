import sys
import math

sys.stdin = open('/home/trifiasco/my world/github-trifiasco/CPPS/codeforces/Contests/Div3/#587/in.txt', 'r')

def isInside(x1, y1, x2, y2, x3, y3, x4, y4):
    #check if first one is inside second one

    if (x1 >= x3 and x2 <= x4) and (y1 >= y3 and y2 <= y4):
        return True
    return False

def isOverlapping(x1, y1, x2, y2, x3, y3, x4, y4):
    if x1 > x4 or x3 > x2:
        return False
    if y1 > y4 or y3 > y2:
        return False
    return True

if __name__ == "__main__":
    while True:
        try:
            x1, y1 , x2, y2 = (input().split())
        except EOFError:
            break
        
        x3, y3 , x4, y4 = (input().split())
        x5, y5 , x6, y6 = (input().split())

        x1 = int(x1)
        x2 = int(x2)
        x3 = int(x3)
        x4 = int(x4)
        x5 = int(x5)
        x6 = int(x6)

        y1 = int(y1)
        y2 = int(y2)
        y3 = int(y3)
        y4 = int(y4)
        y5 = int(y5)
        y6 = int(y6)

        flag = 1

        if isOverlapping(x3, y3, x4, y4, x5, y5, x6, y6):
            #print('overlapping')
            # if isInside(x1, y1, x2, y2, min(x3, x5), max(y3, y5), max(x4, x6), min(y4, y6)):
            #     flag = 0

            if x3 < x5:
                # left is x3,y3
                if x4 > x6:
                    #right is x4, y4
                    if isInside(x1, y1, x2, y2, x3, y3, x4, y4):
                        flag = 0
                else:
                    #right is x6, y6
                    if isInside(x1, y1, x2, y2, x3, y3, x6, y6):
                        flag = 0
            else:
                #left is x5, y5
                if x4 > x6:
                    #right is x4, y4
                    if isInside(x1, y1, x2, y2, x5, y5, x4, y4):
                        flag = 0
                else:
                    #right is x6, y6
                    if isInside(x1, y1, x2, y2, x5, y5, x6, y6):
                        flag = 0

            #vertical check
            if x3 > x5:
                # left is x3,y3
                if x4 < x6:
                    #right is x4, y4
                    if isInside(x1, y1, x2, y2, x3, y3, x4, y4):
                        flag = 0
                else:
                    #right is x6, y6
                    if isInside(x1, y1, x2, y2, x3, y3, x6, y6):
                        flag = 0
            else:
                #left is x5, y5
                if x4 < x6:
                    #right is x4, y4
                    if isInside(x1, y1, x2, y2, x5, y5, x4, y4):
                        flag = 0
                else:
                    #right is x6, y6
                    if isInside(x1, y1, x2, y2, x5, y5, x6, y6):
                        flag = 0

            # if isInside(x1, y1, x2, y2, x3, y3, x6, y6) or isInside(x1, y1, x2, y2, x5, y5, x4, y4):
            #     flag = 0

        else:
            # if isInside(x1, y1, x2, y2, min(x3, x5), max(y3, y5), max(x4, x6), min(y4, y6)):
            #     print('complex')
            #     flag = 0
            if isInside(x1, y1, x2, y2, x3, y3, x4, y4):
                #print('first')
                flag = 0
            if isInside(x1, y1, x2, y2, x5, y5, x6, y6):
                #print('second')
                flag = 0
        
        if flag == 1:
            print("YES")
        else:
            print("NO")



    pass

