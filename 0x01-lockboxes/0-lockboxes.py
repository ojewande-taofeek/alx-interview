#!/usr/bin/python3
"""
    Method that determines if all the boxes can be opened
    n number of locked boxes in front of you. Each box is
    numbered sequentially from 0 to n - 1 and each box may
    contain keys to the other boxes.
 """


def canUnlockAll(boxes):
    """
        Method that determines if all the boxes can be opened
        A key with the same number as a box opens that box
        You can assume all keys will be positive integers
        There can be keys that do not have boxes
        The first box boxes[0] is unlocked
    Args:
        boxes (list): a list of lists

    Returns:
        boolean: True if all boxes can be opened, else return False
    """
    the_set = set()
    verifier = set()
    for idx in range(len(boxes)):
        verifier.add(idx)
        for key in boxes[idx]:
            if idx == 0 or idx in the_set:
                the_set.add(key)
            elif the_set - verifier:
                remainder = (the_set - verifier)
                for val in remainder:
                    try:
                        if (boxes[val]):
                            for element in boxes[val]:
                                the_set.add(element)
                    except IndexError:
                        continue
            else:
                return False
    return True
