from pylib.data_structures.trie import Trie


def test_trie():
    trie = Trie()
    trie.insert("hello")
    trie.insert("world")
    trie.insert("hell")

    assert trie.search("hello")
    assert trie.search("world")
    assert trie.search("hell")
    assert not trie.search("h")
