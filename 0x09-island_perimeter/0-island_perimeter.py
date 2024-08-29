#!/usr/bin/python3
"""Module for island perimeter calculator
"""


def island_perimeter(grid) -> int:
    """Island perimeter calculator
    """
    h = len(grid)
    if h == 0:
        return 0
    w = len(grid[0])
    if w == 0:
        return 0

    sidecount = 0

    for i in range(h):
        for j in range(w):
            if grid[i][j] == 1:
                sidecount += i == h-1 or grid[i+1][j] == 0
                sidecount += j == w-1 or grid[i][j+1] == 0
                sidecount += i == 0 or grid[i-1][j] == 0
                sidecount += j == 0 or grid[i][j-1] == 0
    return sidecount


if __name__ == "__main__":
    grid = [
        [1, 0, 0, 0, 0, 0],
        [1, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 1]
    ]
    print(island_perimeter(grid))
