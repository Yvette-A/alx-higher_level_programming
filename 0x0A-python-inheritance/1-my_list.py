#!usr/bin/python3

"""defines a class"""


class MyList(list):
    """inherited from the built-in list function"""
    def print_sorted(self):
        """Prints a list in assending sorted order"""
        print(sorted(self))
