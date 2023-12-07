#!/usr/bin/env python

from collections import deque
import sys

points = []
point_index = 0
grid = {}
areas = {}

def is_empty(coords, for_point=None):
    if coords[0] in grid and coords[1] in grid[coords[0]]:
        if grid[coords[0]][coords[1]] < 0:
            return for_point is None or -for_point != grid[coords[0]][coords[1]]
        else:
            return False
    else:
        return True

def tag_point(p, tag):
    if p[0] not in grid:
        grid[p[0]] = {}
    grid[p[0]][p[1]] = tag

def mark_point(p, tag):
    if is_empty(p, tag):
        tag_point(p, -tag)

def dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

for line in sys.stdin:
    point_index += 1
    points.append([int(x) for x in line.strip().split(',')] + [False, point_index])

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

# Find points with infinite areas
for p1 in points:
    edge_points = (
        (p1[0], limits[2]),
        (p1[0], limits[3]),
        (limits[0], p1[1]),
        (limits[1], p1[1])
    )
    infinite = 4

    for e in edge_points:
        for p2 in points:
            if p1[3] == p2[3]: continue
            if dist(e, p2) <= dist(e, p1):
                infinite -= 1
                break

    if infinite:
        p1[2] = True

for p1 in points:
    if p1[2]: continue
    fifo = deque([p1[:2]])
    areas[p1[3]] = 0

    while fifo:
        p = fifo.popleft()
        if not is_empty(p, p1[3]): continue
        hit = True

        for p2 in points:
            if p1[3] == p2[3]: continue
            if dist(p, p2) <= dist(p, p1):
                mark_point(p, p1[3])
                hit = False
                break

        if hit:
            tag_point(p, p1[3])
            areas[p1[3]] += 1

            for d in directions:
                new_point = (p[0] + d[0], p[1] + d[1])
                if is_empty(new_point, p1[3]):
                    fifo.append(new_point)

best = 0
for size in areas.values():
    if size > best:
        best = size

print(best)
