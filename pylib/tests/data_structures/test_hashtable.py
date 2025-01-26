from pylib.data_structures.hashtable import HashTable


def test_hashtable():
    hashtable_src = HashTable(5)
    hashtable_src.makeForwardHashTable("hello")
    hashtable_txt = HashTable(5)
    hashtable_txt.makeForwardHashTable("hello")
    assert hashtable_src.getForwardHashingQuery(
        0, 4
    ) == hashtable_txt.getForwardHashingQuery(0, 4)

    hashtable_txt = HashTable(5)
    hashtable_txt.makeForwardHashTable("llo")
    assert hashtable_src.getForwardHashingQuery(
        2, 4
    ) == hashtable_txt.getForwardHashingQuery(0, 2)
