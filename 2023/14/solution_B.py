#!/usr/bin/env python

import sys

REPEATS = 1_000_000_000

def get_load(grid):
    total = 0

    for i, row in enumerate(grid):
        for char in row:
            if char == 'O':
                total += len(grid) - i

    return total


def cycle(grid):
    for _ in range(4):
        new_grid = [list(row) for row in grid]

        for col in range(len(grid[0])):
            next_stone = 0
            for row in range(len(grid)):
                if grid[row][col] == 'O':
                    new_grid[row][col] = '.'
                    new_grid[next_stone][col] = 'O'
                    next_stone += 1
                elif grid[row][col] == '#':
                    next_stone = row + 1

        # clock-wise rotation
        grid = [list(_) for _ in zip(*new_grid[::-1])]

    return tuple(tuple(_) for _ in grid)


def main():
    grid = tuple(tuple(_.strip()) for _ in sys.stdin)
    seen = {grid: 0}
    counter = 0

    while True:
        counter += 1
        grid = cycle(grid)
        if grid in seen:
            loop = counter - seen[grid]
            counter = (REPEATS - counter) % loop
            break
        else:
            seen[grid] = counter

    for _ in range(counter):
        grid = cycle(grid)

    print(get_load(grid))


if __name__ == '__main__':
    main()
