#!/usr/bin/python3
"""Module base geometry"""


class BaseGeometry:
    """Base geometry class"""
   
    def area(self):
        """method that raises an Exception with the message area() is not implemented"""
        raise Exception("area() is not implemented")
