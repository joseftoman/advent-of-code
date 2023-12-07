#!/usr/bin/env python

import sys

import numpy as np

around = [np.array(_) for _ in [(0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0)]]
limits = [[None, None], [None, None], [None, None]]
cubes = set()

for line in sys.stdin:
    cube = tuple(int(_) for _ in line.strip().split(','))

    if limits[0][0] is None:
        limits = [[cube[0], cube[0]], [cube[1], cube[1]], [cube[2], cube[2]]]
    else:
        for index in range(3):
            if cube[index] < limits[index][0]:
                limits[index][0] = cube[index]
            if cube[index] > limits[index][1]:
                limits[index][1] = cube[index]

    cubes.add(tuple(cube))

stack = []

for x in range(limits[0][0] - 1, limits[0][1] + 2):
    for y in range(limits[1][0] - 1, limits[1][1] + 2):
        stack.append((x, y, limits[2][0] - 1))
        stack.append((x, y, limits[2][1] + 1))
for z in range(limits[2][0], limits[2][1] + 1):
    stack.extend([(limits[0][0] - 1, y, z) for y in range(limits[1][0] - 1, limits[1][1] + 2)])
    stack.extend([(limits[0][1] + 1, y, z) for y in range(limits[1][0] - 1, limits[1][1] + 2)])
    stack.extend([(x, limits[1][0] - 1, z) for x in range(limits[0][0], limits[0][1] + 1)])
    stack.extend([(x, limits[1][1] + 1, z) for x in range(limits[0][0], limits[0][1] + 1)])

wrap = set(stack)
surface = 0

while stack:
    cube = np.array(stack.pop())
    for adjacent in [tuple(cube + _) for _ in around]:
        if not (limits[0][0] <= adjacent[0] <= limits[0][1] and limits[1][0] <= adjacent[1] <= limits[1][1] and limits[2][0] <= adjacent[2] <= limits[2][1]):
            continue
        elif adjacent in wrap:
            continue
        elif adjacent in cubes:
            surface += 1
        else:
            wrap.add(adjacent)
            stack.append(adjacent)

print(surface)
