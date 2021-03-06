'''
Computational complexity = O(nlog(n))
'''
import sys


def merge_sort(arr):
    size = len(arr)

    return divide_and_conquer(arr, 0, size - 1)


def divide_and_conquer(arr, left, right):
    if(left == right):
        return [arr[left]]

    mid = left + (right - left) // 2
    left_sorted_array = divide_and_conquer(arr, left, mid)
    right_sorted_array = divide_and_conquer(arr, mid + 1, right)

    return merge_array(left_sorted_array, right_sorted_array)


def merge_array(left_arr: list, right_arr: list):
    left_len = len(left_arr)
    right_len = len(right_arr)

    merged_array = []

    left_iterator = 0
    right_iterator = 0

    while left_iterator <= left_len and right_iterator <= right_len:
        if(left_iterator == left_len):
            # just copy from right one
            while right_iterator < right_len:
                merged_array.append(right_arr[right_iterator])
                right_iterator += 1
            break

        elif(right_iterator == right_len):
            # just copy from left one
            while left_iterator < left_len:
                merged_array.append(left_arr[left_iterator])
                left_iterator += 1
            break

        elif(left_arr[left_iterator] <= right_arr[right_iterator]):
            merged_array.append(left_arr[left_iterator])
            left_iterator += 1
        elif(left_arr[left_iterator] > right_arr[right_iterator]):
            merged_array.append(right_arr[right_iterator])
            right_iterator += 1

    return merged_array


if __name__ == "__main__":

    sys.setrecursionlimit(200000)
    array = [5, 1, 3, 2, 4]

    sorted_array = merge_sort(array)

    print(sorted_array)
    print(array)

    pass
