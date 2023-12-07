#!/usr/bin/env python

from collections import defaultdict
import heapq
import sys

cave = {}
visited = set()
heap = [(0, (0, 0))]

for y, line in enumerate(sys.stdin):
    for x, risk in enumerate([int(_) for _ in list(line.rstrip())]):
        cave[(x, y)] = risk

target = (len(line) - 2, y)

for x in range(0, target[0] + 1):
    for y in range(0, target[1] + 1):
        for ext_x in range(0, 5):
            for ext_y in range(0, 5):
                if ext_x == 0 and ext_y == 0:
                    continue
                risk = cave[(x, y)] + ext_x + ext_y
                if risk > 9:
                    risk -= 9
                cave[(ext_x * (target[0] + 1) + x, ext_y * (target[1] + 1) + y)] = risk

target = ((target[0] + 1) * 5 - 1, (target[1] + 1) * 5 - 1)

while heap:
    risk, pos = heapq.heappop(heap)
    if pos in visited:
        continue
    visited.add(pos)

    if pos == target:
        print(risk)
        break

    for diff in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        x = pos[0] + diff[0]
        y = pos[1] + diff[1]
        if x < 0 or y < 0 or x > target[0] or y > target[1] or (x, y) in visited:
            continue

        heapq.heappush(heap, (risk + cave[(x, y)], (x, y)))
