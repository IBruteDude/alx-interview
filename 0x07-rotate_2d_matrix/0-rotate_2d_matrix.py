#!/usr/bin/python3
""" Module for a matrix rotating function
"""


def rotate_2d_matrix(matrix):
    """ In-place matrix rotating function
    """
    # the more pythonic one-liner
    # newmatrix = list(map(list, zip(*reversed(matrix))))

    n = len(matrix)
    for lvl in range(n//2):
        for slot in range(lvl, n-lvl - 1):
            tmp = matrix[lvl][slot]
            matrix[lvl][slot] = matrix[n-slot-1][lvl]
            matrix[n-slot-1][lvl] = matrix[n-lvl-1][n-slot-1]
            matrix[n-lvl-1][n-slot-1] = matrix[slot][n-lvl-1]
            matrix[slot][n-lvl-1] = tmp


if __name__ == "__main__":
    matrix = [[1,  2,  3,  4],
              [5,  6,  7,  8],
              [9,  10, 11, 12],
              [13, 14, 15, 16]]

    rotate_2d_matrix(matrix)

    print(matrix)
