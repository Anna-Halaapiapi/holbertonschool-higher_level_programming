#!/usr/bin/env python3
"""
This module provides the VerboseList class.
"""


class VerboseList(list):
    """
    defines verboselist and inherits from built-in list class.
    allows for customisation/extension of built-in list class methods.
    """

    def append(self, item):
        """
        uses built-in list's append method.
        prints message after adding item to list.
        """
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """
        uses built-in list's extend method.
        prints message after extending list with iterable.
        """
        super().extend(iterable)
        print(f"Extended the list with [{len(iterable)}] items.")

    def remove(self, item):
        """
        uses built-in list's remove method.
        prints message before removing item from start of list.
        """
        print(f"Removed [{item}] from the list")
        super().remove(item)

    def pop(self, index=None):
        """
        uses built-in list's pop method.
        prints message before removing item from list.
        """
        list_end_index = (len(self) - 1)

        if index is None:
            print(f"Popped [{self[list_end_index]}] from the list")
            super().pop()
        else:
            print(f"Popped [{self[index]}] from the list")
            super().pop(index)
