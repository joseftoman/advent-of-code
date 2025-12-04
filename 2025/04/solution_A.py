#!/usr/bin/env python

import sys


def render(rolls, max_y, max_x):
    for y in range(max_y + 1):
        print(''.join('@' if (y, x) in rolls else '.' for x in range(max_x + 1)))
    print()


def main():
    rolls = set()
    access = 0

    for y, line in enumerate(_.strip() for _ in sys.stdin):
        if not line:
            break
        for x, char in enumerate(line):
            if char == '@':
                rolls.add((y, x))

    max_y = max(_[0] for _ in rolls)
    max_x = max(_[1] for _ in rolls)

    # render(rolls, max_y, max_x)

    for y in range(max_y + 1):
        for x in range(max_x + 1):
            if (y, x) not in rolls:
                continue

            around = 0
            for diff in ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)):
                if (y + diff[0], x + diff[1]) in rolls:
                    around += 1
            if around < 4:
                access += 1

    print(access)


if __name__ == '__main__':
    main()
