"""
Computational complexity = O(log(n))
"""

import math


def lower_bound(arr: list[int], key: int) -> int:
    # lower bound - left most index where the value is greater or equal than key.
    # simply the left most index where if `key` is inserted, the array will still be sorted.
    lo = 0
    hi = len(arr) - 1

    while lo <= hi:
        mid = lo + (hi - lo) // 2  # equivalent to (lo + hi) / 2

        # in case of lower bound try to discard to right half first if possible.
        if arr[mid] >= key:
            hi = mid - 1
        else:
            lo = mid + 1

    return lo


def upper_bound(arr: list[int], key: int) -> int:
    # upper bound - left most index where the value is greater than key.
    # simply the right index where if `key` is inserted, the array will still be sorted.
    lo = 0
    hi = len(arr) - 1

    while lo <= hi:
        mid = lo + (hi - lo) // 2  # equivalent to (lo + hi) / 2

        # in case of upper bound try to discard to left half first if possible.
        if arr[mid] <= key:
            lo = mid + 1
        else:
            hi = mid - 1

    return lo


def bisection_method(x: float) -> float:
    # let's compute squre_root_of(x)

    hi = x
    lo = 0.0

    EPS = 10e-9

    while math.fabs(hi - lo) >= EPS:
        # alternative to this condition - for i = 0 to(log2(high - low)) + log2(1e9)
        # for i in range(((int)(log2(high - low)) + log2(1e9)))
        mid = lo + (hi - lo) / 2.0
        if mid * mid >= x:
            hi = mid
        else:
            lo = mid

    return lo
