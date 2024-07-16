#!/usr/bin/python3
""" Module for a matrix rotating function
"""


def rotate_2d_matrix(matrix):
    """ In-place matrix rotating function
    """
    newmatrix = list(map(list, zip(*reversed(matrix))))
    for i in range(len(newmatrix)):
        matrix[i] = newmatrix[i]


if __name__ == "__main__":
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    rotate_2d_matrix(matrix)
    print(matrix)
