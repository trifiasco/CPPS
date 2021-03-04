'''
Info
- lists are mutable
- list.append(x) - add item to the last index
- list.insert(i, x) - add item x to the ith index
- list.remove(x) - remove the first item
- list.pop([i]) - remove ith indexed item(or the last if i is not specified) and returns the item
- list.index(x) - returns the first item index equal to x
- list.[count, sort, ...]
- list.copy - returns a shallow copy
- sorted vs list.sort() - .sort() in-place operation, changes the list(doesn't return anything). sortted doesn't return or change list  
'''

from collections import deque
import functools


def compare(a, b):
    # should return one of [-1,0,1];
    # -1 means leave a,b unchanged.
    # 0 means unchanged with respect to each other but sorted with respect to all diff elements.
    # 1 means sort b before a.
    return b[0] - a[0]
    return False


if __name__ == "__main__":
    # space separated int input
    # n, a, b, c = map(int, input().split())

    # using list as stack
    stack = [3, 4, 5]
    stack.append(6)
    print(stack)

    stack.pop()
    print(stack)

    # using list as queue.
    # better to use collection.deque
    # insert methods - append(x) - appends right, appendLeft(x)
    # remove methods - pop() - pop from right, popLeft(x)

    # list comprehensions

    squars = [x**2 for x in range(10)]
    print(squars)

    # initialize a 2d array with -1
    negative2dArray = [[-1 for y in range(5)] for x in range(5)]
    print(negative2dArray)

    # custom sorting
    paired_array = [(5, 1), (4, 1), (3, 1), (2, 1), (1, 1)]
    #paired_array.sort(key=lambda a: a[0])
    paired_array.sort(key=functools.cmp_to_key(compare))
    print(paired_array)

    pass
