from pylib.search_n_sort.merge_sort import merge_sort


def test_merge_sort():
    arr = [12, 11, 13, 5, 6, 7]
    assert merge_sort(arr) == [5, 6, 7, 11, 12, 13]

    arr = [38, 27, 43, 3, 9, 82, 10]
    assert merge_sort(arr) == [3, 9, 10, 27, 38, 43, 82]

    arr = [1]
    assert merge_sort(arr) == [1]

    arr = []
    assert merge_sort(arr) == []
