#!/usr/bin/python3
""" Function which returns the dict desc with data structure
for JSON serialization of the object.
"""


def class_to_json(obj):
    """Returns the dictionary description with simple data structure
    for JSON serialization of an object.

    Args:
        obj: An instance of a class.

    Returns:
        dict: A dictionary containing the serialized attributes of the object.
    """
    json_dict = {}
    for key, value in obj.__dict__.items():
        # Ignore attributes starting with double underscores
        if not key.startswith("__"):
            json_dict[key] = value
    return json_dict
