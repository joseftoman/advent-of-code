#!/usr/bin/env python

import re
import sys

def get_adjacent(level, index):
    row = index // 5
    col = index % 5
    response = []

    if col > 0 and (col, row) != (3, 2):
        response.append((level, index - 1))
    if col < 4 and (col, row) != (1, 2):
        response.append((level, index + 1))
    if row > 0 and (col, row) != (2, 3):
        response.append((level, index - 5))
    if row < 4 and (col, row) != (2, 1):
        response.append((level, index + 5))

    if (col, row) == (3, 2):
        response.extend([(level + 1, _) for _ in [4, 9, 14, 19, 24]])
    if (col, row) == (1, 2):
        response.extend([(level + 1, _) for _ in [0, 5, 10, 15, 20]])
    if (col, row) == (2, 3):
        response.extend([(level + 1, _) for _ in [20, 21, 22, 23, 24]])
    if (col, row) == (2, 1):
        response.extend([(level + 1, _) for _ in [0, 1, 2, 3, 4]])

    if col == 0:
        response.append((level - 1, 11))
    if col == 4:
        response.append((level - 1, 13))
    if row == 0:
        response.append((level - 1, 7))
    if row == 4:
        response.append((level - 1, 17))

    return response


def print_bugs(layout):
    print(layout[:5])
    print(layout[5:10])
    print(layout[10:15])
    print(layout[15:20])
    print(layout[20:])
    print()


bugs = ''
for line in sys.stdin:
    bugs += line.strip()

levels = {_: '.' * 12 + '?' + '.' * 12 for _ in range(-201, 202)}
levels[0] = bugs

for minute in range(1, 201):
    new_levels = levels.copy()

    for level in range(-minute, minute + 1):
        new_bugs = ''

        for index, space in enumerate(levels[level]):
            if index == 12:
                new_bugs += '?'
                continue

            bugs_around = len([True for pos in get_adjacent(level, index) if levels[pos[0]][pos[1]] == '#'])
            if (space == '#' and bugs_around == 1) or (space == '.' and 1 <= bugs_around <= 2):
                new_bugs += '#'
            else:
                new_bugs += '.'

        new_levels[level] = new_bugs

    levels = new_levels

total_bugs = 0
for bugs in levels.values():
    total_bugs += bugs.count('#')
print(total_bugs)
