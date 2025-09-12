#!/usr/bin/python3
from task_six import max_integer
import unittest

# test class
class TestMaxInteger(unittest.TestCase):
    def test_max_at_the_end(self):
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)
        
if __name__ == '__main__':
    unittest.main()
