#!/usr/bin/python3
"""
    Function determine the fewest number of coins needed
    to meet a given amount total
"""


def makeChange(coins, total):
    """
        As explained above
    """
    if total <= 0:
        return 0

    else:
        coin = sorted(coins)
        coin.reverse()
        counter = 0
        for idx in coin:
            while(total >= idx):
                counter += 1
                total -= idx
        if total == 0:
            return counter
        return -1
