"""
Implementation of Doubly Linked List in Python

Doubly linked list have two references:
1. The previous field
2. The next field

In Node class we need to add additional previous node reference.
This implementation would allow you to traverse a list in both directions

With doubly linked lists, deque is capable of inserting or deleting
 elements  from both ends of a queue with constant O(1) performance.
"""
from typing import Any


class Node:
    def __init__(self, data: Any):
        self.data = data  # data (value) assignment
        self.next = None  # reference to the next node
        self.previous = None  # reference to the previous node

    def __repr__(self) -> str:
        return self.data


class CircularLinkedList:
    def __init__(self):
        self.head = None

    # Adding and deleting here ...

    def traverse(self, starting_point=None):
        if starting_point is None: # if we not provide starting_point it will take self.head as a starting_point
            starting_point = self.head # assign self.head as starting_point
        node = starting_point # assign starting_point as node
        while node is not None and (node.next != starting_point): # while node is not None and there are still nodes we will iterate
            yield node # we yield each node
            node = node.next # move forward with nodes
        yield node # yield node

    def print_list(self):
        nodes = [] # we create empty list of nodes
        for node in self.traverse(starting_point): # we will use traverse method that will iterate over our nodes
            nodes.append(str(node)) # it will append our nodes in list
        print(" -> ".join(nodes)) # we will print our list of nodes
