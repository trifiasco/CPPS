"""
Computational complexity = O(nlog(n))
"""


def merge_sort(arr: list[int]) -> list[int]:
    size: int = len(arr)
    if size == 0:
        return []

    return divide_and_conquer(arr, 0, size - 1)


def divide_and_conquer(arr: list[int], left: int, right: int) -> list[int]:
    if left == right:
        return [arr[left]]

    mid: int = left + (right - left) // 2
    left_sorted_array: list[int] = divide_and_conquer(arr, left, mid)
    right_sorted_array: list[int] = divide_and_conquer(arr, mid + 1, right)

    return merge_array(left_sorted_array, right_sorted_array)


def merge_array(left_arr: list[int], right_arr: list[int]) -> list[int]:
    left_len: int = len(left_arr)
    right_len: int = len(right_arr)

    merged_array: list[int] = []

    left_iterator: int = 0
    right_iterator: int = 0

    while left_iterator <= left_len and right_iterator <= right_len:
        if left_iterator == left_len:
            # just copy from right one
            while right_iterator < right_len:
                merged_array.append(right_arr[right_iterator])
                right_iterator += 1
            break

        elif right_iterator == right_len:
            # just copy from left one
            while left_iterator < left_len:
                merged_array.append(left_arr[left_iterator])
                left_iterator += 1
            break

        elif left_arr[left_iterator] <= right_arr[right_iterator]:
            merged_array.append(left_arr[left_iterator])
            left_iterator += 1
        elif left_arr[left_iterator] > right_arr[right_iterator]:
            merged_array.append(right_arr[right_iterator])
            right_iterator += 1

    return merged_array
