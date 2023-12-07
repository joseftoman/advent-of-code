#!/usr/bin/env python

import math
import sys

dirs = {'U': (0, 1), 'R': (1, 0), 'D': (0, -1), 'L': (-1, 0)}
head = [0, 0]
tail = [0, 0]
visited = {(0, 0)}

for line in sys.stdin:
    direction, amount = line.split()

    for _ in range(int(amount)):
        head[0] += dirs[direction][0]
        head[1] += dirs[direction][1]

        if max([abs(head[dim] - tail[dim]) for dim in [0, 1]]) < 2:
            continue

        for dim in [0, 1]:
            if head[dim] != tail[dim]:
                tail[dim] += math.copysign(1, head[dim] - tail[dim])
        visited.add(tuple(tail))

print(len(visited))
