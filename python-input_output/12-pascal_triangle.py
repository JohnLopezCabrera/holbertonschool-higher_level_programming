#!/usr/bin/python3
"""
A module to generate Pascal's triangle
"""


def pascal_triangle(n):
    """Generate Pascal's triangle of size n.

    Args:
        n (int): The number of rows in the triangle.

    Returns:
        list: A list of lists of integers representing the Pascal's triangle.
    """
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        row = [1]
        if i > 0:
            for j in range(1, i):
                row.append(triangle[i-1][j-1] + triangle[i-1][j])
            row.append(1)

        triangle.append(row)

    return triangle
