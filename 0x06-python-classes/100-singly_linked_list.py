#!/usr/bin/python3
""" Singly Linked List Implementation"""


class Node:
    """Singly Linked List Node"""

    def __init__(self, data, next_node=None) -> None:
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if isinstance(value, int):
            self.__data = value
        else:
            raise TypeError("data must be an integer")

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if isinstance(value, Node) or value is None:
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """Singly Linked List"""

    def __init__(self) -> None:
        self.__head = None

    def __str__(self) -> str:
        ptr = self.__head
        values = []
        while ptr is not None:
            values.append(str(ptr.data))
            ptr = ptr.next_node

        return "\n".join(values)

    def sorted_insert(self, value):
        ptr = self.__head
        if self.__head is None:
            self.__head = Node(value)
            return

        elif self.__head.data >= value:
            self.__head = Node(value, next_node=ptr)
            return

        else:
            ptr0 = ptr
            while ptr is not None:
                if ptr.data >= value:
                    break
                ptr0 = ptr
                ptr = ptr.next_node

            new = Node(value, next_node=ptr)
            ptr0.next_node = new
            return

    # def sorted_insert(self, value):
    #     """Insert Node while keeping the list sorted (increasingly)"""
    #
    #     new_node = Node(value)
    #
    #     # Handle an empty list or inserting as the new head
    #     if self.__head is None or self.__head.data >= value:
    #         new_node.next_node = self.__head
    #         self.__head = new_node
    #         return
    #
    #     current = self.__head
    #
    #     # Traverse the list to find the insertion point
    #     while current.next_node is not None and current.next_node.data < value:
    #         current = current.next_node
    #
    #     # Insert the new node after the current node
    #     new_node.next_node = current.next_node
    #     current.next_node = new_node
