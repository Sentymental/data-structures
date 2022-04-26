"""
Creating own LinkedList
- add_left
- add_right
- add_before
- add_after
- remove
- iter
- repr
"""
from typing import Any, Generator

class Node:
    def __init__(self, data: Any, next_node: Any = None) -> None:
        self.data = data
        self.next = next_node


    def __repr__(self) -> str:
        return self.data



class LinkedList:
    def __init__(self, nodes: list[Any] = None):
        self.head = None
        if nodes is not None: # if we provide list of nodes we should check it
            node = Node(data=nodes.pop(0)) # our head node will be the first item from the list
            self.head = node # node that we define will be our head
            for elem in nodes: # loop through rest of the list and add them as node.next
                node.next = Node(data=elem) # every single node.next from our predefined list
                node = node.next # move to next node

    def add_first(self, node: Any):
        """
        We want to add a value as first in the LinkedList
        So we might want to move our current head to node.next
        And assign value as a new self.head.
        """
        node.next = self.head # we assign our current self.head to node.next
        self.head = node # we assign node that we provide as new self.head


    def add_last(self, node: Any):
        """
        We want to add a value as last item in our LinkedList
        So we might want to traverse all LinkedList to find last item
        And assign new value as a last item. But it can be that
        Our last item will be first item in LinkedList
        """
        if self.head is None: # if LinkedList is empty then our node will be treated as head node
            self.head = node # we assign node as head node
            return # return

        for current_node in self: # if the list is not empty we need to iterate over all LinkedList
            pass # just to find last node in LinkedList, so we don't need anything from that loop

        current_node.next = node # get last element from LinkedList and node.next we will assign new value


    def add_after(self, target: Any, new_node: Any):
        """
        We want to add a value just right after target value
        So w might want to search our target value
        And assign new_value as node.next
        Also we might want to make sure List is not empty and target value is in that list
        """
        if self.head is None: # if self.head is None that means List is empty
            raise Exception("LinkedList is empty.") # so if it is empty we cannot add after target value so we need to raise expcetion

        for node in self: # loop through all nodes in self
            if node.data == target: # if node.data is equal to our target we can go fruther
                new_node.next = node.next # so we want to move next node (after target) right to new_node
                node.next = new_node # and then after our target we want to assign our new_node value
                return # return

        raise Exception(f"Data {target} not found")


    def add_before(self, target: Any, new_node: Any):
        """
        We want to add a value just right before target value
        So we might want to search our target value using loop
        And assign new value just before our target value so we want to move it node.next
        Also we might want to make sure list is not empty and target value is in that list
        """
        if self.head is None: # check if linked list is not empty
            raise Exception("LinkedList is empty") # if is we need to raise an exception

        if self.head.data == target: # when our target value is equal to target
            return self.add_first(new_node) # so we want to return previously defined add_first(node)

        prev_node = self.head # we assign our previous node as head so we start doing it from the beginning
        for node in self: # we loop through
            if node.data == target: # check if our current node is eqaual to our targeted value
                prev_node.next = new_node # we assign prev_node.next as a new value (inserted just before target value)
                new_node.next = node # and we assign new_node.next to our node so move it on right
                return # return

        raise Exception(f"Data {target} not found") # Exception as targeted value is not found


    def remove(self, target: Any):
        """
        We want to remove a target from our LinkedList
        Also we want to check if linked list is empty or if target is in list if not we need an exception
        """
        if self.head is None: # check if linked list is empty
            raise Exception("LinkedList is empty") # if is we want to raise an exception

        if self.head.data == target: # check if our head is our targeted value
            self.head = self.head.next # if it is we want to move our head to next node
            return # return

        prev_node = self.head # we assign self.head as our prev_node
        for node in self: # we want to loop through our all items
            if node.data == target: # if node is equal our target value
                previous_node.next = node.next # we want to use our previous_node.next to and assign node.next to remove value
                return # return
            prev_node = node # we assign prev_node to node

        raise Exception(f"Data {target} not found") # if target value is not in our LinkedList we want to raise an exception


    def __iter__(self) -> Generator[Any, None, None]:
        node = self.head # predefine our first node as head
        while node is not None: # loop through node list
            yield node # iterate over every node
            node = node.next # move to the next node


    def __repr__(self) -> str:
        node = self.head # predefine our node as first node (head)
        nodes = [] # create a list of nodes
        while node is not None: # if node is not None then append
            nodes.append(node.data) # append data  node.data (which is Node(data))
            node = node.next # move to the next node
        nodes.append("None") # if there is no more nodes, append "None" for our string representation
        return " -> ".join(nodes) # return string representation of LinkedList
