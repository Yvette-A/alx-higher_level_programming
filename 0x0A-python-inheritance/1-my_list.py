#!usr/bin/python3

"""defines a class"""


class MyList(list):
    """inherited from the built-in list function"""
    def print_sorted(self):
        if all(isinstance(item, int) for item in self):
            print(sorted(self))
