#!/usr/bin/python3
"""
This module provides the Node and SinglyLinkedList classes.
"""


class Node:
    """
    The Node class defines a node of a singly linked list.
    """
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    # data - getter
    @property
    def data(self):
        return self.__data

    # data - setter
    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    # next_node - getter
    @property
    def next_node(self):
        return self.__next_node

    # next_node - setter
    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    The SinglyLinkedList class defines a singly linked list.
    """
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        """
        creates a new node & assigns value to data var.
        inserts the new Node into the correct position in the list
        (list is in ascending order)
        """
        # create a new Node and assign value to data attribute
        new_node = Node(value, None)

        # insert at beginning if list is empty
        if self.__head is None:
            self.__head = new_node
            return

        # find start of list (first node)
        current_node = self.__head

        # check for insertion at beginning of non-empty list
        if (new_node.data < current_node.data):
            # insert new node at start of list
            new_node.next_node = self.__head
            self.__head = new_node
            return

        # loop through list until:
        # hitting end of list (tail/None)
        # exit method if insertion position found
        while (current_node.next_node is not None):
            # check for correct mid-list position (not start or end)
            if (new_node.data < current_node.next_node.data):
                # insert node in correct position
                new_node.next_node = current_node.next_node
                current_node.next_node = new_node
                return

            # go to next node to check for correct position
            current_node = current_node.next_node

        # if correct position not found in loop - add new node to end of list
        current_node.next_node = new_node
        new_node.next_node = None
        return

    def __str__(self):
        """
        format the output of print() in 100-main.py
        per the task requirements
        """
        formatted_string = ""

        # check if list empty
        if self.__head is None:
            return formatted_string

        # find start of singly linked list
        current_node = self.__head

        # build new string with data attributes from nodes
        while (current_node.next_node is not None):
            formatted_string = formatted_string + str(current_node.data)
            formatted_string = formatted_string + "\n"
            current_node = current_node.next_node
        formatted_string = formatted_string + str(current_node.data)
        return formatted_string
