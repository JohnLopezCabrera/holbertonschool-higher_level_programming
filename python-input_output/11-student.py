#!/usr/bin/python3
"""Defines the Student class."""


class Student:
    """Reps a student."""

    def __init__(self, first_name, last_name, age):
        """Initializes the Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dict rep of a Student instance.

        Args:
            attrs (list): A list of strings specifying the
            attributes to retrieve.
                If None, all attributes will be retrieved.

        Returns:
            dict: A dictionary containing the
            specified attributes of the Student instance.
        """
        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr) 
                    for attr in attrs if hasattr(self, attr)}

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance
        with those from the given dictionary.

        Args:
            json (dict): A dictionary containing the new attribute values.
        """
        for key, value in json.items():
            setattr(self, key, value)
