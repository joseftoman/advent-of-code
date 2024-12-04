#!/usr/bin/env python

import sys


def find_xmas(line: str) -> int:
    total = 0
    total += len(line.split('XMAS')) - 1
    total += len(line[::-1].split('XMAS')) - 1
    return total


def main():
    lines = [_.strip() for _ in sys.stdin]
    total = 0

    # rows
    for line in lines:
        total += find_xmas(line)

    for col in range(len(lines)):
        # columns
        line = ''.join(_[col] for _ in lines)
        total += find_xmas(line)

        # lower left triangle
        line = ''.join(lines[col + row][row] for row in range(len(lines) - col))
        total += find_xmas(line)

        # lower right triangle
        line = ''.join(lines[col + row][len(lines) - row - 1] for row in range(len(lines) - col))
        total += find_xmas(line)

        if col == 0:
            continue

        # upper right triangle
        line = ''.join(lines[row][col + row] for row in range(len(lines) - col))
        total += find_xmas(line)

        # upper left triangle
        line = ''.join(lines[row][len(lines) - 1 - col - row] for row in range(len(lines) - col))
        total += find_xmas(line)

    print(total)


if __name__ == '__main__':
    main()
