import sys
import os
from typing import List

LOCAL_ENV: bool = os.environ.get('USER') == 'trifiasco'

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        size: int = 2 * n
        ans: List[int] = [0]*(size)
        slow: int = 0
        fast: int = n


        current: int = 0
        while current < size:
            ans[current] = nums[slow]
            slow += 1
            current += 1
            ans[current] = nums[fast]
            fast += 1
            current += 1
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
            n = int(input())
            sol = Solution()
            # add method name below
            print(sol.shuffle(list_, n))
            # do stuff
        except EOFError:
            break
    pass
