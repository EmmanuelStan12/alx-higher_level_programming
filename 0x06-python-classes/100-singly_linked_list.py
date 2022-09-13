#!/usr/bin/python3
class Node:
    """
    Singly linked list
    """
    def __init__(self, data, next_node=None):
        if type(data) is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = data
        if next_node is None:
            self.__next_node = None
        elif not isinstance(next_node, Node):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value

class SinglyLinkedList:
    """
    Singly Linked List
    """
    def __init__(self):
        self.__head = None
        self.__size = 0

    def sorted_insert(self, value):
        head = self.__head
        if head is None:
            self.__head = Node(value)
            self.__size += 1
        elif head.data >= value:
            current = self.__head
            new_node = Node(value, current)
            self.__head = new_node
        else:
            current = head
            while current.next_node is not None:
                if current.next_node.data > value:
                    new_node = Node(value, current.next_node)
                    current.next_node = new_node
                    return
                current = current.next_node
            new_node = Node(value)
            current.next_node = new_node

    def __str__(self):
        current = self.__head
        s = ''
        while current is not None:
            s += "{}".format(current.data)
            if current.next_node is not None:
                s += '\n'
            current = current.next_node
        return s
