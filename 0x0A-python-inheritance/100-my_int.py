#!/usr/bin/python3
"""defines class MYInt"""


class MyInt(int):
    """inhererits from built in int module"""
    def __eq__(self, value):
        return self.real != value

    def __ne__(self, value):
        return self.real == value
