#!/usr/bin/python3
"""
0-main
"""
def pascal_triangle(lvl):
    """Generates a matrix of the pascal triangle
    """
    if lvl <= 0:
        return []
    elif lvl == 1:
        return [[1]]

    triangle = [[1], [1, 1]]
    while lvl > 2:
        triangle.append([1])
        for (x, y) in it.pairwise(triangle[-2]):
            triangle[-1].append(x + y)
        triangle[-1].append(1)
        lvl -= 1
    return triangle


def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    print_triangle(pascal_triangle(5))
