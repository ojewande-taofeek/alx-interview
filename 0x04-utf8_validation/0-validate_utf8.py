#!/usr/bin/python3
"""
    UTF-8 Validation
"""


def validUTF8(data):
    """
    method that determines if a given data set represents a
    valid UTF-8 encoding.

    Args:
        data (list): List of integers
    """
    
    try:
        if isinstance(data, list):
            for val in data:
                val.to_bytes(1, byteorder='big')
    except OverflowError:
        return False
    return True
