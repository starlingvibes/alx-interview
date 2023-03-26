#!/usr/bin/python3

"""
Given a pile of coins of different values, determine the fewest number of coins needed to meet a given amount total.
"""


def makeChange(coins, total):
    """
    Given a pile of coins of different values, determine the fewest
    number of coins needed to meet a given amount total.
    Args:
        coins: list of the values of the coins in your possession
        total: total value to meet
        Returns:
            fewest number of coins needed to meet total
            If total is 0 or less, return 0
            If total cannot be met by any number of coins you have,
            return -1
            """
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    print(coins)
    count = 0
    for coin in coins:
        while total >= coin:
            total -= coin
            count += 1
    if total != 0:
        return -1
    return count
