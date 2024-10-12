#!/usr/bin/python3
"""
    The Pascal's triangle
"""


def pascal_triangle(n):
    """
        Returns a list of lists of integers representing the
        Pascal’s triangle of n
    Args:
        n (int): The height or row of the Pascal's triangle
    """
    triangle = []
    if n <= 0:
        triangle.append([[]])
    elif n == 1:
        triangle.append([1])
    elif n == 2:
        triangle.append([1, 1])
    elif n > 2:
        triangle.append([1])
        triangle.append([1, 1])
        for row in range(2, n):
            inner_row = [1]
            for col in range(1, row):
                inner_row.append(triangle[row - 1][col] +
                                 triangle[row - 1][col - 1])
            inner_row.append(1)
            triangle.append(inner_row)
    return triangle
