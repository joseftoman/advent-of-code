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
