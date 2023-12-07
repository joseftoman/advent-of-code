#!/usr/bin/env python

import sys

octo = [[int(_) for _ in line.strip()] for line in sys.stdin]
step = 0

while True:
    ripe = set()
    step += 1
    flashes = 0

    for y in range(10):
        for x in range(10):
            octo[y][x] += 1
            if octo[y][x] > 9:
                ripe.add((x, y))

    while ripe:
        x, y = ripe.pop()
        flashes += 1
        octo[y][x] = 0

        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                x1 = x + dx
                y1 = y + dy
                if (dx == 0 and dy == 0) or x1 < 0 or x1 > 9 or y1 < 0 or y1 > 9:
                    continue
                if octo[y1][x1] == 0:
                    continue

                octo[y1][x1] += 1
                if octo[y1][x1] > 9:
                    ripe.add((x1, y1))

    if flashes == 100:
        break

print(step)
