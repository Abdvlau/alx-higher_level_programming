#!/usr/bin/python3
"""A class that inherits from list"""

class MyList(list):
    """inherits from list"""
    def print_sorted(self):
        """Method that prints the list"""
        sorted_list = sorted(self)
        print(sorted_list)

