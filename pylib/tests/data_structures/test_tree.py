from pylib.data_structures.tree import Tree


def test_tree():
    tree = Tree(5)
    tree.insert(2)
    tree.insert(1)
    tree.insert(3)
    tree.insert(4)

    assert list(tree.inorder(tree.root)) == [1, 2, 3, 4, 5]
    assert list(tree.preorder(tree.root)) == [5, 2, 1, 3, 4]
    assert list(tree.postorder(tree.root)) == [1, 4, 3, 2, 5]
