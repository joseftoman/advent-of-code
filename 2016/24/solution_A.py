#!/usr/bin/python3

import sys
import itertools

hvac = [ l.rstrip() for l in sys.stdin ]
points = []
dists = {}

def find_shortest(start, end):
    queue = [ start ]
    known = { start: 0 }

    while queue:
        pos = queue.pop(0)
        for diff in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            n = (pos[0] + diff[0], pos[1] + diff[1])
            if n[0] < 0 or n[0] >= len(hvac) or n[1] < 0 or n[1] >= len(hvac[n[0]]):
                continue
            if hvac[n[0]][n[1]] == '#':
                continue
            if n in known:
                continue
            known[n] = known[pos] + 1
            if n == end:
                return known[n]
            queue.append(n)

for y in range(0, len(hvac)):
    for x in range(0, len(hvac[y])):
        if hvac[y][x].isdigit(): points.append((int(hvac[y][x]), y, x))

for pair in itertools.combinations(points, 2):
    steps = find_shortest((pair[0][1], pair[0][2]), (pair[1][1], pair[1][2]))
    dists[(pair[0][0], pair[1][0])] = steps
    dists[(pair[1][0], pair[0][0])] = steps

min = None

for path in itertools.permutations(map(lambda x: x[0], points)):
    if path[0] != 0: continue
    steps = 0
    for i in range(1, len(path)):
        steps += dists[(path[i-1], path[i])]

    if min is None or steps < min[0]:
        min = (steps, path)

print(min[0])
