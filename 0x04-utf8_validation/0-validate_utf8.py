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
    num_bytes = 0
    if isinstance(data, list):
        for val in data:
            if num_bytes == 0:  # 1-byte Character
                if (val >> 7) == 0:
                    num_bytes = 0
                elif (val >> 5) == 0b110:  # 2-bytes Character
                    num_bytes = 1
                elif (val >> 4) == 0b1110:  # 3-bytes Character
                    num_bytes = 2
                elif (val >> 3) == 0b11110:  # 4-bytes Character
                    num_bytes = 3
                else:                 # first val does not match any character
                    return False
            else:
                if (val >> 6) != 0b10:     # Not a continuation sequence
                    return False
                num_bytes -= 1
        return num_bytes == 0
