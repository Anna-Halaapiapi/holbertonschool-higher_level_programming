#!/usr/bin/python3
"""Module to find the max integer in a list
"""


def max_integer(list=[]):
    """Function to find and return the max integer in a list of integers
        If the list is empty, the function returns None
    """
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result


import unittest
from math import inf

# test class
class TestMaxInteger(unittest.TestCase):
    def test_max_at_end(self):
        result = max_integer([1, 2, 3, 4])
        self.assertEqual(result, 4)
    
    def test_int_max_at_mid(self):
        result = max_integer([1, 3, 4, 2])
        self.assertEqual(result, 4)

    def test_int_max_at_start(self):
        result = max_integer([4, 3, 1, 2])
        self.assertEqual(result, 4)

    def test_int_multiple_max(self):
        result = max_integer([4, 3, 4, 2])
        self.assertEqual(result, 4)

    def test_int_negative(self):
        result = max_integer([-4, 3, 4, -1])
        self.assertEqual(result, 4)

    def test_float(self):
        result = max_integer([1.0, 3.0, 4.0])
        self.assertEqual(result, 4.0)

    def test_list_str(self):
        result = max_integer(["Hey", "My", "Name", "is"])
        self.assertEqual(result, "is")
    
    def test_single_str(self):
        result = max_integer("Anna")
        self.assertEqual(result, "n")

    def test_mixed_values(self):
        with self.assertRaises(TypeError):
            max_integer([5, 6.0, "Name", True])
    
    def test_empty_list(self):
        result = max_integer([])
        self.assertEqual(result, None)

    def test_empty_arg(self):
        result = max_integer()
        self.assertEqual(result, None)
    
    def test_2_args(self):
        with self.assertRaises(TypeError):
            max_integer([1, 2, 3], [3, 2, 1])

    def test_int_overflow(self):
        result = max_integer([float('inf'), 9])
        self.assertEqual(result, inf)
    
    def test_float_nan(self):
        result = max_integer([1, 2, float('nan')])
        self.assertEqual(result, 2)

    def test_zero(self):
        result = max_integer([0])
        self.assertEqual(result, 0)
    
if __name__ == '__main__':
    unittest.main()
