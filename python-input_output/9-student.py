#!/usr/bin/python3
""" Define a student class module.
"""


class Student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        """Initializes a Student inst.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a dict rep of a Student inst.

        Returns:
            dict: A dictionary containing the attributes
            of the Student instance.
        """
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age
        }
