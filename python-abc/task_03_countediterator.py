#!/usr/bin/env python3
"""
This module provides the CountedIterator class.
"""


class CountedIterator:
    """
    extends built-in iter function
    """
    def __init__(self, iterable_object):
        self.iterator = iter(iterable_object)
        self.counter = 0

    def get_count(self):
        return self.counter

    def __next__(self):
        """
        overrides __next__ method
        increments counter when next is called
        returns next item in iterable
        raises exception when no items left to iterate
        """
        item = next(self.iterator)
        self.counter += 1
        return item
