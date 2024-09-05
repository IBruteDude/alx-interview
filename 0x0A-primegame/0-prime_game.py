#!/usr/bin/python3
""" Prime counting contest
"""


def isWinner(x, nums):
    """ Prime counting contest
    """
    n = max(nums[:x]) + 1
    primesieve = [1] * n
    primesieve[1] = primesieve[0] = 0
    for i in range(2, n):
        for j in range(i * i, n, i):
            primesieve[j] = 0
    # print(primesieve)
    for i in range(3, n):
        primesieve[i] += primesieve[i-1]
    # print(primesieve)

    round_results = map(lambda i: primesieve[i] % 2, nums)
    # print(list(map(lambda i: primesieve[i], nums)))
    # print(list(map(lambda i: "Maria" if primesieve[i] % 2 else "Ben", nums)))
    marias = len(list(filter(lambda x: bool(x), round_results)))
    bens = len(nums) - marias
    if bens > marias:
        return "Ben"
    elif bens < marias:
        return "Maria"
    return None


if __name__ == '__main__':
    print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
    print("Winner: {}".format(isWinner(3, [4, 5, 1])))
