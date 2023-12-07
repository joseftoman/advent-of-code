#!/usr/bin/env python

import sys

depth = int(sys.stdin.readline()[7:])
target = [int(x) for x in sys.stdin.readline()[8:].split(',')]

cave = {}
risk = 0

for dist in range(0, sum(target) + 1):
    for x, y in [(x, dist - x) for x in range(0, dist + 1)]:
        if (x == 0 and y == 0) or [x, y] == target:
            geo = 0
        elif x == 0:
            geo = y * 48271
        elif y == 0:
            geo = x * 16807
        else:
            geo = cave[(x-1, y)] * cave[(x, y-1)]

        erosion = (geo + depth) % 20183
        cave[(x, y)] = erosion

        if x <= target[0] and y <= target[1]:
            risk += erosion % 3

print(risk)
