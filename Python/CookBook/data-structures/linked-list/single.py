
import sys
import os

LOCAL_ENV: bool = os.environ.get('USER') == 'trifiasco'

class Node():
    def __init__(self, value) -> None:
        self.value = value;
        self.next = None;

class SingleLinkedList():
    def __init__(self) -> None:
       self.head : Node = Node(None);

    def printf(self):
        iterator = self.head;

        while iterator != None:
            print(iterator.value, end=" ");
            iterator = iterator.next;

        print("");

    def insert_last(self, value):
        node = Node(value);

        if self.head.value is None:
            self.head = node;
            return;

        iterator = self.head;

        while iterator.next != None:
            iterator = iterator.next;

        iterator.next = node;


    def insert_first(self, value):
        node = Node(value);

        if self.head.value is None:
            self.head = node;
            return;

        node.next = self.head;
        self.head = node;


def READ():
    sys.stdin = open('in.txt', 'r');
    #sys.stdout = open('out.txt', 'w');

if __name__ == "__main__":
    if LOCAL_ENV:
        READ()

    sys.setrecursionlimit(200000)

    llist = SingleLinkedList();
    llist.printf()
    llist.insert_first(3)
    llist.insert_last(1)
    llist.insert_last(2)
    llist.printf()
    llist.insert_first(4)
    llist.printf()
    # while True:
        # try:
            # n = int(input())
            # # do stuff
        # except EOFError:
            # break
    pass
