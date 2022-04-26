"""
Singly Linked List implementation in Python 3.10

Node: (the first node is called: head)
- data: data it stored in Node
- next_node: contains the reference to next node

LinkedLists are used as: queues/stacks/graphs

"""
from typing import Any


# Create a Node:
class Node:
    """
    Class that creates each node
    - data: data that is stored in Node
    - next_node: reference to the next node
    """
    def __init__(self, data: Any, next_node: Any = None):
        self.data = data
        self.next = next_node

    def __repr__(self):
        return self.data


# Create a LinkedList:
class LinkedList:
    """
    Implementing a Linked Lists
    - nodes: list of predefined values to be treated as Node
    """
    def __init__(self, nodes = None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for i in nodes:
                node.next = Node(data=i)
                node = node.next


    def add_left(self, node):
        node.next = self.head
        self.head = node


    def add_right(self, node):
        if self.head is None:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.next = node


    def add_after(self, target, new_node):
        if self.head is None:
            raise Exception("LinkedList is empty.")

        for node in self:
            if node.data == target:
                new_node.next = node.next
                node.next = new_node
                return

        raise Exception(f"Node with data {target} not found")


    def add_before(self, target, new_node):
        if self.head is None:
            raise Exception("LinkedList is empty.")

        if self.head.data == target:
            return self.add_left(new_node)

        prev_node = self.head
        for node in self:
            if node.data == target:
                prev_node.next = new_node
                new_node.next = node
                return
            prev_node = node

        raise Exception(f"Node with data {target} not found")


    def remove(self, target):
        if self.head is None:
            raise Exception("LinkedList is empty.")

        if self.head.data == target:
            self.head = self.head.next
            return

        previous_node = self.head
        for node in self:
            if node.data == target:
                previous_node.next = node.next
                return
            previous_node = node

        raise Exception(f"Node with data {target} not found")


    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next


    def __repr__(self) -> str:
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next

        nodes.append("None")
        return " -> ".join(nodes)


