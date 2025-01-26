from dataclasses import dataclass
from typing import Self, Iterator


@dataclass
class Node:
    data: int
    left: Self | None = None
    right: Self | None = None


@dataclass
class Tree:
    def __init__(self, root: int | None = None) -> None:
        self.root: Node | None = Node(root) if root is not None else None

    def insert(self, data: int) -> None:
        # BST insertion
        if self.root is None:
            self.root = Node(data)
            return

        current = self.root
        while True:
            if data < current.data:
                if current.left is None:
                    current.left = Node(data)
                    break
                current = current.left
            else:
                if current.right is None:
                    current.right = Node(data)
                    break
                current = current.right
        return

    def insert_level_order(
        self, arr: list[int], root: Node | None, i: int, n: int
    ) -> Node | None:
        if i < n:
            temp = Node(arr[i])
            root = temp

            root.left = self.insert_level_order(arr, root.left, 2 * i + 1, n)
            root.right = self.insert_level_order(arr, root.right, 2 * i + 2, n)
        return root

    def inorder(self, node: Node | None) -> Iterator[int]:
        def _inorder(node: Node | None) -> Iterator[int]:
            if node:
                yield from _inorder(node.left)
                yield node.data
                yield from _inorder(node.right)

        yield from _inorder(node)

    def preorder(self, node: Node | None) -> Iterator[int]:
        def _preorder(node: Node | None) -> Iterator[int]:
            if node:
                yield node.data
                yield from _preorder(node.left)
                yield from _preorder(node.right)

        yield from _preorder(node)

    def postorder(self, node: Node | None) -> Iterator[int]:
        def _postorder(node: Node | None) -> Iterator[int]:
            if node:
                yield from _postorder(node.left)
                yield from _postorder(node.right)
                yield node.data

        yield from _postorder(node)
