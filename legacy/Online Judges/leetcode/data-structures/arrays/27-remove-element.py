import sys
import os
from typing import List

LOCAL_ENV: bool = os.environ.get('USER') == 'trifiasco'

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        size = len(nums)
        slow: int = 0
        fast: int = 0

        while fast < size:
            while slow < size and nums[slow] != val:
                slow += 1
                fast += 1
            while fast < size and nums[fast] == val:
                fast += 1

            if fast >= size:
                break
            nums[slow] = nums[fast]
            nums[fast] = val
            slow += 1
            fast = slow
        return slow
        

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
            n = int(input())
            sol = Solution()
            # add method name below
            print(sol.removeElement(list_, n))
            print(list_)
            # do stuff
        except EOFError:
            break
    pass
