#!/usr/bin/python3
"""
This module provides a function to load an object
from a text file containing JSON representation.
"""


import json


def load_from_json_file(filename):
    """
    Loads an object from a text file containing JSON representation.

    Args:
        filename (str): The name of the file to read from.

    Returns:
        object: The Python data structure loaded from the JSON file.
    """
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
