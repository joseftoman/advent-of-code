#!/usr/bin/env python

import sys


def main():
    total = 0
    grid = [_.strip() for _ in sys.stdin]

    for col in range(len(grid[0])):
        next_weight = len(grid)
        for row in range(len(grid)):
            if grid[row][col] == 'O':
                total += next_weight
                next_weight -= 1
            elif grid[row][col] == '#':
                next_weight = len(grid) - row - 1

    print(total)


if __name__ == '__main__':
    main()
