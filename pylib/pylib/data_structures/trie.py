from dataclasses import dataclass
from typing import Self


@dataclass
class TrieNode:
    children: dict[str, Self]
    is_end_of_word: bool

    def __init__(self) -> None:
        self.children = {}
        self.is_end_of_word = False


@dataclass
class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, key: str) -> None:
        current = self.root
        for char in key:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.is_end_of_word = True

    def search(self, key: str) -> bool:
        current = self.root
        for char in key:
            if char not in current.children:
                return False
            current = current.children[char]
        return current.is_end_of_word

    def delete(self, key: str) -> None:
        self._delete(self.root, key, 0)

    def _delete(self, current: TrieNode, key: str, index: int) -> bool:
        if index == len(key):
            if not current.is_end_of_word:
                return False
            current.is_end_of_word = False
            return len(current.children) == 0

        char = key[index]
        if char not in current.children:
            return False

        should_delete_current_node = self._delete(
            current.children[char], key, index + 1
        )

        if should_delete_current_node:
            del current.children[char]
            return len(current.children) == 0

        return False
