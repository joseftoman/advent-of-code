#!/usr/bin/env python

from collections import defaultdict
import heapq
import sys

cave = {}
heap = [
    (0, (0, 0), 0, (1, 0)),
    (0, (0, 0), 0, (0, 1)),
]

for y, line in enumerate(sys.stdin):
    for x, loss in enumerate([int(_) for _ in list(line.rstrip())]):
        cave[(x, y)] = loss

target = (len(line) - 2, y)
visited = set()
best = 0

while heap:
    loss, pos, straight, previous = heapq.heappop(heap)
    if (pos, straight, previous) in visited:
        continue
    visited.add((pos, straight, previous))

    if pos == target and straight >= 4:
        print(loss)
        break

    forbidden = previous[0] * -1, previous[1] * -1

    for diff in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        if diff == forbidden:
            continue
        if diff == previous:
            if straight == 10:
                continue
            else:
                new_straight = straight + 1
        elif straight < 4:
            continue
        else:
            new_straight = 1

        x = pos[0] + diff[0]
        y = pos[1] + diff[1]
        if x < 0 or y < 0 or x > target[0] or y > target[1] or ((x, y), new_straight, diff) in visited:
            continue

        heapq.heappush(heap, (loss + cave[(x, y)], (x, y), new_straight, diff))
