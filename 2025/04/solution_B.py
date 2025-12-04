#!/usr/bin/env python

import sys


def render(rolls, max_y, max_x):
    for y in range(max_y + 1):
        print(''.join('@' if (y, x) in rolls else '.' for x in range(max_x + 1)))
    print()


def remove_accessible(rolls, max_y, max_x) -> int:
    removed = []

    for y in range(max_y + 1):
        for x in range(max_x + 1):
            if (y, x) not in rolls:
                continue

            around = 0
            for diff in ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)):
                if (y + diff[0], x + diff[1]) in rolls:
                    around += 1
            if around < 4:
                removed.append((y, x))

    for roll in removed:
        rolls.remove(roll)

    return len(removed)


def main():
    rolls = set()
    total = 0

    for y, line in enumerate(_.strip() for _ in sys.stdin):
        if not line:
            break
        for x, char in enumerate(line):
            if char == '@':
                rolls.add((y, x))

    max_y = max(_[0] for _ in rolls)
    max_x = max(_[1] for _ in rolls)

    # render(rolls, max_y, max_x)

    while True:
        removed = remove_accessible(rolls, max_y, max_x)
        total += removed
        if not removed:
            break

    print(total)


if __name__ == '__main__':
    main()
