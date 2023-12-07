#!/usr/bin/env python

import math
import sys

asteroid_map = set()
width = None
height = 0

def count_visible(choice):
    global asteroid_map, width, height
    pool = set(asteroid_map)
    pool.remove(choice)
    order = sorted(pool, key=lambda x: abs(choice[0] - x[0]) + abs(choice[1] - x[1]))

    for pos in order:
        if pos not in pool:
            continue

        diff = (pos[0] - choice[0], pos[1] - choice[1])
        if diff[0] == 0:
            diff = (0, 1 if diff[1] > 0 else -1)
        elif diff[1] == 0:
            diff = (1 if diff[0] > 0 else -1, 0)
        else:
            gcd = math.gcd(*diff)
            diff = (diff[0] / gcd, diff[1] / gcd)
        pos = (pos[0] + diff[0], pos[1] + diff[1])

        while pos[0] >= 0 and pos[1] >= 0 and pos[0] < width and pos[1] < height:
            if pos in pool:
                pool.remove(pos)
            pos = (pos[0] + diff[0], pos[1] + diff[1])

    return len(pool)

for row, line in enumerate(sys.stdin):
    height += 1
    if width is None:
        width = len(line.strip())

    for column, char in enumerate(line.strip()):
        if char == '#':
            asteroid_map.add((column, row))

best = None

for asteroid in asteroid_map:
    visible = count_visible(asteroid)
    if best is None or visible > best:
        best = visible
        print('MAX:', asteroid)

print(best)
