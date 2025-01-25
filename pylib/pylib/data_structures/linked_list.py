from __future__ import annotations
from dataclasses import dataclass
from typing import Iterator


@dataclass
class Node[T]:
    value: T
    next: Node[T] | None = None


class SingleLinkedList[T]:
    def __init__(self) -> None:
        self.head: Node[T] | None = None
        self.size = 0

    def append(self, value: T) -> None:
        if self.head is None:
            self.head = Node(value)
            self.size += 1
            return

        iterator = self.head
        while iterator.next is not None:
            iterator = iterator.next

        iterator.next = Node(value)
        self.size += 1

    def prepend(self, value: T) -> None:
        node = Node(value)
        node.next = self.head
        self.head = node
        self.size += 1

    def delete(self, value: T) -> None:
        if self.head is None:
            return

        if self.head.value == value:
            self.head = self.head.next
            self.size -= 1
            return

        iterator = self.head
        while iterator.next is not None:
            if iterator.next.value == value:
                iterator.next = iterator.next.next
                self.size -= 1
                return
            iterator = iterator.next

    def reverse(self) -> None:
        prev = None
        current = self.head

        while current is not None:
            # each iteration, we are reversing the link
            # of the current node to the previous node.
            # so, we need to store the next node before

            # prev represents the reversed list
            # current represents the list to be reversed
            # each iteration, we are prepending the current node to prev(reversed list)
            next = current.next
            current.next = prev
            prev = current
            current = next

        self.head = prev

    def __len__(self) -> int:
        return self.size

    def __iter__(self) -> Iterator[T]:
        iterator = self.head
        while iterator is not None:
            yield iterator.value
            iterator = iterator.next
