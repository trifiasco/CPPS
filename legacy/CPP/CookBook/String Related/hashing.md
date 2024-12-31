# Hashing

```
Hashing is an improvement over Direct Access Table. The idea is to use hash function that converts a given phone number or any other key to a smaller number and uses the small number as index in a table called hash table.
```

### Hash function

a hash function maps a big number or string to a small integer that can be used as index in hash table.
A good hash function should have following properties

- Efficiently computable.
- Should uniformly distribute the keys (Each table position equally likely for each key)

### Hash Table

An array to store values corresponding to a key (got from from hash function).

### Collision Handling

- Chaining - each key would point to a linked list of values.

- Open addressing - keep probing until an empty slot is found.

  if hash(x) % S is booked, then check hash(x) + 1 % S and so on.

  - probing technique can be `linear` like the previous example. but it will create **clustering**. So you can do a `quadratic probing`.

  - quadratic probing: try i^2th slot in ith iteration.
  - double hashing: you can use another hash function - (hash(x) + i\*hash2(x)) % S
  - A popular second hash function is `hash2(x) = Prime - (x%Prime)`, where `Prime` is less than table size.

### Load factor and Rehashing

[follow this article](https://www.geeksforgeeks.org/load-factor-and-rehashing/)

### Need to Explore

1. MD5
2. SHA256

### Hashing a string

```
void hash(string x)
  for each char in x
    hash_table[i] = (hash_table[i-1] * base + (char - 97)) % mod

int query(int left, int right)
    ret1 = (hash_table[right] - hash_table[left - 1]*base^(right-left +1))% mod
```

In case of double hashing -

```
long hash1 = query1(0,n)
long hash2 = query2(0,n)

long double hash = (hash1 << 31) | hash2
```
