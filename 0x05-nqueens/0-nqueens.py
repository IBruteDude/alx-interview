#!/usr/bin/python3
""" N-Queens Solver
"""
import sys


def n_queens_solutions(N, current_col=0, occupied_slots=[]):
    """ Backtracking generator for N-Queens solutions
    """
    allowed_rows = [True] * N

    for x, y in occupied_slots:
        allowed_rows[y] = False
        if 0 <= y + (current_col - x) < N:
            allowed_rows[y + (current_col - x)] = False
        if 0 <= y - (current_col - x) < N:
            allowed_rows[y - (current_col - x)] = False

    for row in range(N):
        if allowed_rows[row]:
            new_slots = occupied_slots.copy()
            new_slots.append([current_col, row])
            if current_col == N - 1:
                yield new_slots
            else:
                yield from n_queens_solutions(N, current_col + 1, new_slots)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: nqueens N")
        exit(1)
    try:
        N = int(sys.argv[1])
    except Exception:
        print("N must be a number")
        exit(1)
    if N < 4:
        print("N must be at least 4")
        exit(1)
    for solution in n_queens_solutions(N):
        print(solution)
