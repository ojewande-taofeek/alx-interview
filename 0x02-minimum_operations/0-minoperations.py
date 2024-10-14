#!/usr/bin/python3
"""
    In a text file, there is a single character H. Your
    text editor can execute only two operations in this file:
    Copy All and Paste. Given a number n, write a method that
    calculates the fewest number of operations needed to result
    in exactly n H characters in the file.

    Prototype: def minOperations(n)
    Returns an integer
    If n is impossible to achieve, return 0
"""


def minOperations(n):
    """
    A function that returns the min number of a character as exlained above

    Args:
        n (int): Expected number of characters

    Returns:
        int: Min number of operations
    """
    if n < 2:
        return 0
    elif n <= 5:
        print(n)
        return
    div_list = []
    div = 2
    half = n // div
    while (div <= half):
        if (n % div == 0):
            n //= div
            div_list.append(div)
        else:
            div += 1
    return sum(div_list)
