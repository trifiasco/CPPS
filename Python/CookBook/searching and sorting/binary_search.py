import math


def lower_bound(arr, key):
    # lower bound - left most index where the value is greater or equal than key.
    # simply the left most index where if `key` is inserted, the array will still be sorted.
    lo = 0
    hi = len(arr) - 1

    while lo <= hi:
        mid = lo + (hi - lo) // 2  # equivalent to (lo + hi) / 2

        # in case of lower bound try to discard to right half first if possible.
        if(arr[mid] >= key):
            hi = mid - 1
        else:
            lo = mid + 1

    return lo


def higher_bound(arr, key):
    # upper bound - left most index where the value is greater than key.
    # simply the right index where if `key` is inserted, the array will still be sorted.
    lo = 0
    hi = len(arr) - 1

    while lo <= hi:
        mid = lo + (hi - lo) // 2  # equivalent to (lo + hi) / 2

        # in case of lower bound try to discard to left half first if possible.
        if(arr[mid] <= key):
            lo = mid + 1
        else:
            hi = mid - 1

    return lo


def bisection_method(x: float):
    # let's compute squre_root_of(x)

    hi = x
    lo = 0.0

    EPS = 10E-9

    while math.fabs(hi - lo) >= EPS:
        # alternative to this condition - for i = 0 to(log2(high - low)) + log2(1e9)
        # for i in range(((int)(log2(high - low)) + log2(1e9)))
        mid = lo + (hi - lo) / 2.0
        if(mid * mid >= x):
            hi = mid
        else:
            lo = mid

    return lo


if __name__ == "__main__":

    array = [1, 2, 2, 3, 4, 4, 5]

    # lower bound
    lower_bound_of_2 = lower_bound(array, 2)
    assert lower_bound_of_2 == 1
    print(lower_bound_of_2)

    lower_bound_of_3 = lower_bound(array, 3)
    assert lower_bound_of_3 == 3
    print(lower_bound_of_3)

    lower_bound_of_6 = lower_bound(array, 6)
    assert lower_bound_of_6 == 7
    print(lower_bound_of_6)

    # upper bound
    upper_bound_of_2 = higher_bound(array, 2)
    assert upper_bound_of_2 == 3
    print(upper_bound_of_2)

    upper_bound_of_3 = higher_bound(array, 3)
    assert upper_bound_of_3 == 4
    print(upper_bound_of_3)

    upper_bound_of_6 = higher_bound(array, 6)
    assert upper_bound_of_6 == 7
    print(upper_bound_of_6)

    # bisection method

    sqrt_of_4 = round(bisection_method(4), 4)
    print(sqrt_of_4)
    assert sqrt_of_4 == 2.0

    sqrt_of_8 = round(bisection_method(8), 4)
    print(sqrt_of_8)
    assert sqrt_of_8 == 2.8284

    # python builtin `bisect` module

    pass
