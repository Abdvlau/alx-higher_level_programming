#!/usr/bin/python3
"""Defines a text-writing function"""

def write_file(filename="", text=""):
    """
    :param filename: Path to the file
    :param text: String content to write to the file
    :return: Number of characters written
    """

    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
