import sys
import os
from typing import List

LOCAL_ENV: bool = os.environ.get('USER') == 'trifiasco'

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:

        n = len(nums)
        ans: List[int] = [0]*n
        for i in range(n):
            ans[i] = nums[nums[i]]
        return ans
        

def READ():
    sys.stdin = open('in.txt', 'r');
    #sys.stdout = open('out.txt', 'w');
    pass

if __name__ == "__main__":
    if LOCAL_ENV:
        READ()

    while True:
        try:
            list_ = list(map(int, input().split(",")))
            sol = Solution()
            print(sol.buildArray(list_))
            # do stuff
        except EOFError:
            break
    pass
