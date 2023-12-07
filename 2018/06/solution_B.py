#!/usr/bin/env python

from collections import deque
import sys

points = []
grid = {}
area_size = 0
limit = 10_000

def is_empty(coords):
    return False if coords[0] in grid and coords[1] in grid[coords[0]] else True

def mark_point(p):
    if p[0] not in grid:
        grid[p[0]] = {}
    grid[p[0]][p[1]] = True

def dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

for line in sys.stdin:
    points.append([int(x) for x in line.strip().split(',')])

limits = (
    min([p[0] for p in points]),
    max([p[0] for p in points]),
    min([p[1] for p in points]),
    max([p[1] for p in points]),
)
directions = (
    (-1, -1), ( 0, -1), ( 1, -1),
    (-1,  0),           ( 1,  0),
    (-1,  1), ( 0,  1), ( 1,  1)
)

first = ((limits[0] + limits[1]) // 2, (limits[2] + limits[3]) // 2)
fifo = deque([first])
mark_point(first)

while fifo:
    coord = fifo.popleft()
    if sum([dist(coord, p) for p in points]) >= limit: continue

    area_size += 1

    for d in directions:
        new_point = (coord[0] + d[0], coord[1] + d[1])
        if is_empty(new_point):
            fifo.append(new_point)
            mark_point(new_point)

print(area_size)
