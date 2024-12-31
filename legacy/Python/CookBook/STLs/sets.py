'''
Info - set is an unordered collection with no duplicate elements.
- declared with curly brace({}) or set() function.
- for empty set, must use set() function.
- similar to list comprehension, set comprehension is also possible.
'''

if __name__ == "__main__":

    basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
    print(basket)


    joined = "-".join(basket);
    # for item in basket:
        # joined += item

    print(joined)

    print('orange' in basket)

    # >> >  # Demonstrate set operations on unique letters from two words
    # ...
    # >> > a = set('abracadabra')
    # >> > b = set('alacazam')
    # >> > a                                  # unique letters in a
    # {'a', 'r', 'b', 'c', 'd'}
    # >> > a - b                              # letters in a but not in b
    # {'r', 'd', 'b'}
    # >> > a | b                              # letters in a or b or both
    # {'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
    # >> > a & b                              # letters in both a and b
    # {'a', 'c'}
    # >> > a ^ b                              # letters in a or b but not both
    # {'r', 'd', 'b', 'm', 'z', 'l'}

    pass
