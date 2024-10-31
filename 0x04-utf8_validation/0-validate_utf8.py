#!/usr/bin/python3

def validUTF8(data):
    """
    method that determines if a given data set represents a
    valid UTF-8 encoding.

    Args:
        data (list): List of integers
    """
    num_bytes = [1, 2, 3, 4]
    try:
        if isinstance(data, list):
            for val in data:
                for num in num_bytes:
                    val.to_bytes(num, byteorder='big')
    except OverflowError:
        return False
    return True
