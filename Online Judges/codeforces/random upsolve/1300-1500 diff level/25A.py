import sys
import os
import math

script_dir = os.path.dirname(__file__)
username = "trifiasco"
if username in script_dir:
    sys.stdin = open(script_dir + '/in.txt', 'r')

def call(nums, flag):
    for i in range (len(nums)):
        if (nums[i] & 1) == flag:
            return i + 1

if __name__ == "__main__":
    while True:
        try:
            n = int(input())
        except EOFError:
            break

        nums = list(map(int, input().split()))

        odd = 0
        even = 0

        for i in range(3):
            if nums[i] & 1:
                odd += 1
            else:
                even += 1
        
        if odd > even:
            print(call(nums, 0))
        else:
            print(call(nums, 1))

    pass

