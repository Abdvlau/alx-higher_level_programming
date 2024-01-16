#!/usr/bin/python3
"""Defines a function that appends a string at the end of a text file"""




def append_write(filename="", text=""):
    """Append a string to a UTF-8 text file.

    Args:
        filename (str): The name of the file to write.
        text (str): The append to the file.
    Returns:
        The number of character appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
       return f.write(text)
