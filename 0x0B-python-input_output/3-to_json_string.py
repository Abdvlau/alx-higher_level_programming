#!/usr/bin/python3
"""Defines a function that return JSON representation of an object"""

import json
def to_json_string(my_obj):
    """
    Convert a Python object to a JSON-formatted string.

    :param my_obj: Object to be converted
    :return: JSON-formatted string.
    """
    return json.dumps(my_obj)
