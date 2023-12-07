#!/usr/bin/env python

from collections import deque
import sys

caves = [[int(_) for _ in line.strip()] for line in sys.stdin]
basins = []
sizes = []
basin_index = 0


def get_neighbours(x, y, basin=False):
    points = []

    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        x1, y1 = x + dx, y + dy
        if x1 < 0 or x1 >= len(caves[0]) or y1 < 0 or y1 >= len(caves):
            continue
        if basin and (caves[y1][x1] == 9 or basins[y1][x1] is not None):
            continue
        points.append((x1, y1))

    return points


def measure_basin(x, y, index):
    size = 0
    queue = deque([(x, y)])

    while queue:
        x, y = queue.popleft()
        if basins[y][x] is not None:
            continue
        basins[y][x] = index
        size += 1
        queue.extend(get_neighbours(x, y, True))

    return size


for _ in caves:
    basins.append([None] * len(caves[0]))

for y in range(len(caves)):
    for x in range(len(caves[0])):
        around = [caves[item[1]][item[0]] for item in get_neighbours(x, y)]

        if min(around) > caves[y][x]:
            basin_index += 1
            sizes.append(measure_basin(x, y, basin_index))

sizes.sort()
print(sizes[-1] * sizes[-2] * sizes[-3])
