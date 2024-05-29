#!/usr/bin/python3
"""Function to read file"""


def read_file(filename=""):
    """Read a text file and prints it."""
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read(), end='')
