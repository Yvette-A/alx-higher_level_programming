#!/usr/bin/python3
"""test cases for rectangle.py"""


import sys
import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    """class to test rectangle"""
    def test_args(self):
        self.assertEqual(Rectangle(10,2), 1)
