"""
LinkedList implementation in Python 3.10
"""


class Node:
    def __init__(self, data, prev_node=None, next_node=None):
        self.data = data
        self.prev_node = prev_node
        self.next_ndoe = next_node

    def __repr__(self):
        return self.data


class LinkedList:
    def __init__(self, data=None):
        self.head = None
        self.tail = None
        if data is not None:
            self.add_multiple_nodes(data)

    def __repr__(self) -> str:
        return " -> ".join(str(node) for node in self)


    def __len__(self):
        count = 0
        node = self.head
        while node:
            count += 1
            node = node.next

        return count


    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next

