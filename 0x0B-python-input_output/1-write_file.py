#!/usr/bin/python3
"""Defines a text file written"""

def write_file(filename="", text=""):
    """
    :param filename: Path to the file
    :param text: String content to write to the file.
    :return: Number of characters written
    """

    with open(filename, 'w', encoding="utf-8") as f:
        chars_written = f.write(text)
        return chars_written
