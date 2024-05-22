#!/usr/bin/python3
"""Defines object attribute lookup."""


def lookup(obj):
    """Return a list of available attributes."""
    return (dir(obj))