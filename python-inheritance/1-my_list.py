#!/usr/bin/python3
"""
This module provides the MyList class.
"""


class MyList(list):
    """
    This class defines MyList and inherits from list.
    """

    def print_sorted(self):
        """
        prints the list, in ascending sorted order.
        """
        list_copy = self.copy()
        list_copy.sort(reverse=False)
        print(list_copy)
