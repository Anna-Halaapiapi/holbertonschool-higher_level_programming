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
        if not hasattr(iterable, '__iter__'):
            raise TypeError(f"Error: {iterable} is not an iterable")
        super().extend(iterable)
        print(f"Extended the list with [{len(iterable)}] items.")

    def remove(self, item):
        """
        uses built-in list's remove method.
        prints message before removing item from list.
        """
        try:
            print(f"Removed [{item}] from the list")
            super().remove(item)
        except ValueError:
            print(f"Error: {item} not found in list")

    def pop(self, index=-1):
        """
        uses built-in list's pop method.
        prints message before removing item from list.
        """
        self.index_validator(index)
        popped_item_value = self[index]
        print(f"Popped [{popped_item_value}] from the list")
        super().pop(index)
        return popped_item_value

    def index_validator(self, index):
        """
        validates:
        if index is an int
        if list is empty
        if index passed is valid
        """
        if not isinstance(index, int):
            raise TypeError("Error: index must be an integer")
        if len(self) == 0:
            raise ValueError("Error: list is empty")
        # index provided is greater available positive & negative indices
        if index > (len(self) - 1) or index < (-len(self)):
            raise ValueError("Error: index provided is out of range")
        return
