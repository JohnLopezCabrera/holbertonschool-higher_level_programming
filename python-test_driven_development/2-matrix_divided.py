#!/usr/bin/pyhon3
def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a given divisor.

    Parameters:
    matrix: A list of lists of integers or floats.
    div: The divisor, must be a number (integer or float).

    Returns:
    A new matrix with all elements divided by the divisor, rounded to 2 decimal places.

    Raises:
    TypeError: If the matrix is not a list of lists of integers/floats, or if div is not a number.
    TypeError: If the rows of the matrix are not of the same size.
    ZeroDivisionError: If div is zero.
    """
    
    # Check if matrix is a list of lists of integers/floats
    if not (isinstance(matrix, list) and all(isinstance(row, list) for row in matrix)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    for row in matrix:
        if not all(isinstance(elem, (int, float)) for elem in row):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check if each row of the matrix has the same size
    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")

    # Check if div is a number (integer or float)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check if div is zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Divide all elements by div and round to 2 decimal places
    new_matrix = []
    for row in matrix:
        new_row = [round(elem / div, 2) for elem in row]
        new_matrix.append(new_row)

    return new_matrix
