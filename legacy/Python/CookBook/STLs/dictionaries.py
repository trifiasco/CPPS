'''
Info - key, value pair
- indexed by keys, keys can be any immutable type. mutable types can't be keys.
- declared with curly brace({}) or dict() function.
'''

if __name__ == "__main__":

    # The dict() constructor builds dictionaries directly from sequences of key-value pairs:
    # dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])

    # using dict as c++ map

    mp = dict()
    basic_list = [5, 4, 3, 2, 1]
    for x in basic_list:
        if mp.get(x, 0) == 0:
            mp[x] = 0
        mp[x] += 1

    print(mp)

    # looping technique
    for k, v in mp.items():
        print(k, v)
    pass
