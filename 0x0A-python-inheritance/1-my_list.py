#!usr/bin/python3

"""defines a class"""


class MyList(list):
    """inherited from the built-in list function"""
    def __init__(self, list=None):
        self.list = []
    def print_sorted(self):
        if all(isinstance(item, int) for item in self):
            print(sorted(self))
