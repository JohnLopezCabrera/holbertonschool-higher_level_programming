#!/usr/bin/python3
def add_integer(a, b=98):
    """
    Add two integers, with b defaulting to 98 if not provided.

    Parameters:
    a: The first number, must be an integer or float.
    b: The second number, must be an integer or float. Defaults to 98.

    Returns:
    The sum of the two numbers, casted to integers.

    Raises:
    TypeError: If either a or b are not integers or floats.
    """
    
    # Check if 'a' is an integer or a float
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    # Check if 'b' is an integer or a float
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    
    # Cast both to integers if they are floats
    a = int(a)
    b = int(b)
    
    # Return the sum of the two integers
    return a + b

# Example usage:
# print(add_integer(3, 4))  # Should print 7
# print(add_integer(3.5, 4.7))  # Should print 7
# print(add_integer(3))  # Should print 101 since b defaults to 98
