#!/usr/python3
def print_square(size):
    # Check if size is an integer
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    # Check if size is less than 0
    if size < 0:
        raise ValueError("size must be >= 0")

    # Iterate over rows
    for _ in range(size):
        # Print a row of '#' characters
        print("#" * size)
