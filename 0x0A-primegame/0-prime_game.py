#!/usr/bin/python3
"""
    Prime Game
"""


def sieveErathosthens(n):
    """
        An algorithm to determine Prime Numbers
    """
    prime = [True for idx in range(n + 1)]

    p = 2
    while (p * p <= n):
        if prime[p] is True:
            for i in range(p*p, n + 1, p):
                prime[i] = False
        p += 1
    primeList = []
    for p in range(2, n + 1):
        if prime[p] is True:
            primeList.append(p)
    return primeList


def isWinner(x, nums):
    """
        Prime game
    """
    Maria = 0
    Ben = 0
    for idx in nums:
        primeList = sieveErathosthens(idx)
        round = 1
        MariaRound = 0
        BenRound = 0
        for primeIdx in range(len(primeList)):
            if (round <= x):
                if primeIdx % 2 == 0:
                    MariaRound += 1
                else:
                    BenRound += 1
            round += 1
        if MariaRound == BenRound:
            Ben += 1
        elif MariaRound > BenRound:
            Maria += 1
    if Maria > Ben:
        return "Maria"
    elif Ben > Maria or Maria == 0:
        return "Ben"
    else:
        return None
