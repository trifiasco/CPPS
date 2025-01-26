from pylib.data_structures.disjoint_set import DisjointSet


def test_disjoint_set():
    ds = DisjointSet(5)
    ds.union(0, 1)
    ds.union(1, 2)
    ds.union(3, 4)
    assert ds.is_same_set(0, 2)
    assert not ds.is_same_set(0, 3)
    assert not ds.is_same_set(2, 3)
    assert ds.is_same_set(3, 4)
