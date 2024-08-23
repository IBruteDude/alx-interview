#!/usr/bin/python3
"""Module for coin change solver
"""
from typing import List, Dict


def _makeChange(coins: List[int], total: int, minCoin: int, memo: List[int]) -> int:
	"""Recursive dp coin change function
	"""
	if total < 0: return -1
	if total == 0: return 0
	if memo[total] != 0: return memo[total]

	minCount = -1 # the reasonable max
	for coin in coins:
		result = _makeChange(coins, total - coin, minCoin, memo)
		if result == -1:
			continue
		if minCount == -1:
			minCount = 1 + result
		else:
			minCount = min(minCount, 1 + result)
	memo[total] = minCount
	return minCount


def makeChange(coins: List[int], total: int) -> int:
	"""Coin change solver
	"""
	if total <= 0: return 0
	return _makeChange(coins, total, min(coins), [0] * (total + 1))


if __name__ == '__main__':
	print(makeChange([1, 2, 25], 37))
	print(makeChange([1256, 54, 48, 16, 102], 1453))
