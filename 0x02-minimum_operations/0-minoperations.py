#!/usr/bin/python3
""" Module for minimum prime factoring operation of a number
"""


def minOperations(n: int) -> int:
    """ Calculate minimum number of multiplications to reach 'n'
    """
    op_count = 0
    if n <= 1:
        return 0

    for i in range(2, n + 1):
        if n <= 1:
            break
        if n % i == 0:
            op_count += i
            n //= i
            while n % i == 0:
                op_count += i
                n //= i
    return op_count


if __name__ == '__main__':
    n = 2147483640
    print(f"Min # of operations to reach {n} char: {minOperations(n)}")

    n = 12
    print(f"Min # of operations to reach {n} char: {minOperations(n)}")
