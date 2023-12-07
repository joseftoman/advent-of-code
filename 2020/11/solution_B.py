#!/usr/bin/env python

import sys

prev = [_.strip() for _ in sys.stdin]
x_max = len(prev)
y_max = len(prev[0])
new = None
limit = 10000

def check(a, b):
    if ''.join(a) != ''.join(b):
        return None
    return ''.join(a).count('#')

while limit:
    limit -= 1
    new = []
    for x in range(0, x_max):
        new.append('')

        for y in range(0, y_max):
            if prev[x][y] == '.':
                new[x] += '.'
                continue

            occupied = 0
            for x_diff in [-1, 0, 1]:
                for y_diff in [-1, 0, 1]:
                    if not x_diff and not y_diff:
                        continue

                    dist = 1
                    while 0 <= x + x_diff * dist < x_max and 0 <= y + y_diff * dist < y_max and prev[x + x_diff * dist][y + y_diff * dist] == '.':
                        dist += 1
                    if 0 <= x + x_diff * dist < x_max and 0 <= y + y_diff * dist < y_max and prev[x + x_diff * dist][y + y_diff * dist] == '#':
                        occupied += 1

            if prev[x][y] == 'L' and not occupied:
                new[x] += '#'
            elif prev[x][y] == '#' and occupied >= 5:
                new[x] += 'L'
            else:
                new[x] += prev[x][y]

    result = check(prev, new)
    if result is not None:
        print(result)
        break

    prev = new
