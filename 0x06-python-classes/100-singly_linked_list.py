#!/usr/bin/python3
"""To define classes for a singly-linked list."""


class Node:
    """To represent a node in the singly-linked list."""

    def __init__(self, data, next_node=None):
        """To initialize a newer Node.

        Args:
            data (int): The data of the newer Node.
            next_node (Node): The next node in the newer Node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """To Set or get the the data of the Node."""
        return (self.__data)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """To Set or get the next_node of the Node."""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

class SinglyLinkedList:
    """To represent the singly-linked list."""

    def __init__(self):
        """To initalize a newer SinglyLinkedList."""
        self.__head = None

    def sorted_insert(self, value):
        """To insert a newer Node into the SinglyLinkedList.

        The node is then inserted into the list in the correct
        ordered numerical position.

        Args:
            value (Node): The newer Node to be insert.
        """
        newer = Node(value)
        if self.__head is None:
            newer.next_node = None
            self.__head = newer
        elif self.__head.data > value:
            newer.next_node = self.__head
            self.__head = newer
        else:
            tmpr = self.__head
            while (tmpr.next_node is not None and
                    tmpr.next_node.data < value):
                tmpr = tmpr.next_node
            newer.next_node = tmpr.next_node
            tmpr.next_node = newer

    def __str__(self):
        """Define the print() representation of a SinglyLinkedList."""
        values = []
        tmpr = self.__head
        while tmpr is not None:
            values.append(str(tmpr.data))
            tmpr = tmpr.next_node
        return ('\n'.join(values))

