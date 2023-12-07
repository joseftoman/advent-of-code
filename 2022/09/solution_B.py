#!/usr/bin/env python

import math
import sys

dirs = {'U': (0, 1), 'R': (1, 0), 'D': (0, -1), 'L': (-1, 0)}
knots = []
for _ in range(10):
    knots.append([0, 0])
visited = {(0, 0)}

for line in sys.stdin:
    direction, amount = line.split()

    for _ in range(int(amount)):
        knots[0][0] += dirs[direction][0]
        knots[0][1] += dirs[direction][1]

        for index in range(1, 10):
            if max([abs(knots[index - 1][dim] - knots[index][dim]) for dim in [0, 1]]) < 2:
                continue

            for dim in [0, 1]:
                if knots[index - 1][dim] != knots[index][dim]:
                    knots[index][dim] += math.copysign(1, knots[index - 1][dim] - knots[index][dim])
            if index == 9:
                visited.add(tuple(knots[index]))

print(len(visited))
