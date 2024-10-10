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
    if not boxes:
        return True
    box_len = len(boxes)
    unlocked_boxes = set([0])
    keys = set(boxes[0])
    while keys:
        key = keys.pop()
        print(keys)
        if key < box_len and key not in unlocked_boxes:
            unlocked_boxes.add(key)
            keys.update(boxes[key])
            print(keys)
        if len(unlocked_boxes) == box_len:
            return True
    return len(unlocked_boxes) == box_len
