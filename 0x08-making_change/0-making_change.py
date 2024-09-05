#!/usr/bin/python3
"""Module for coin change solver
"""
from typing import List, Dict


def makeChange(coins: List[int], total: int) -> int:
    """Coin change iterative dp solver
    """
    if total <= 0:
        return 0

    if len(coins) == 0:
        return -1

    memo = [total + 1] * (total + 1)
    memo[0] = 0

    coins = sorted(coins)
    minCoin = coins[0]
    if minCoin == -1:
        return -1

    for i in range(1, minCoin):
        memo[i] = -1

    for i in range(minCoin, total + 1):
        coinChanges = []
        for coin in coins:
            if coin <= i:
                if memo[i - coin] >= 0:
                    coinChanges.append(memo[i - coin])
            else:
                break
        if len(coinChanges) == 0:
            continue
        memo[i] = 1 + min(coinChanges)

    return -1 if memo[total] > total else memo[total]


if __name__ == '__main__':
    print(makeChange([1, 2, 25], 37))
    print(makeChange([1256, 54, 48, 16, 102], 1453))

    ##################################################################

    import time

    start = time.time()
    for i in range(10):
        makeChange([1, 4, 5, 10], 1278652)
    end = time.time()

    avg = (end - start) / 10
    if avg > 3:
        print("Runtime too long")
    else:
        print("OK")

    ##################################################################

    start = time.time()
    for i in range(10):
        makeChange([2, 4, 6, 10], 1278653)
    end = time.time()

    avg = (end - start) / 10
    if avg > 3:
        print("Runtime too long")
    else:
        print("OK")
