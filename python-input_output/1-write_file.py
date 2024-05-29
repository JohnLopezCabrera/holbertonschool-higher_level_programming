#!/usr/bin/python3
def write_file(filename="", text=""):
    """Write a string to a .txt file and return number of characters."""
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
