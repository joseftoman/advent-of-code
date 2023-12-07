#!/usr/bin/env python

import heapq
import sys

heights = {}
visited = set()
heap = []
max_x = 0
max_y = 0


for y, line in enumerate(sys.stdin):
    max_x = len(line.strip()) - 1
    max_y = y
    line = line.replace('S', 'a')

    index = line.find('E')
    if index != -1:
        line = line.replace('E', 'z')
        heap = [(0, (index, y))]
    for x, height in enumerate([ord(_) - 97 for _ in line.strip()]):
        heights[(x, y)] = height

while heap:
    steps, pos = heapq.heappop(heap)
    if pos in visited:
        continue
    visited.add(pos)

    if heights[pos] == 0:
        print(steps)
        break

    for diff in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        x = pos[0] + diff[0]
        y = pos[1] + diff[1]
        if x < 0 or y < 0 or x > max_x or y > max_y or (x, y) in visited or heights[(x, y)] < heights[pos] - 1:
            continue

        heapq.heappush(heap, (steps + 1, (x, y)))
