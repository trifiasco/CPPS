from pylib.data_structures.linked_list import SingleLinkedList


def test_linked_list():
    llist = SingleLinkedList[int]()
    llist.append(3)
    llist.append(1)
    llist.append(2)

    assert list(llist) == [3, 1, 2]

    llist.prepend(4)
    assert list(llist) == [4, 3, 1, 2]
    assert llist.size == 4
    assert len(llist) == 4

    current = [4, 3, 1, 2]
    current_iter = iter(current)
    for item in llist:
        assert item == next(current_iter)
    llist.delete(3)
    assert list(llist) == [4, 1, 2]

    llist.reverse()
    assert list(llist) == [2, 1, 4]
    pass
