#!/usr/bin/env python

import sys

import numpy as np

around = [np.array(_) for _ in [(0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0)]]
cubes = set()
surface = 0

for line in sys.stdin:
    cube = np.array([int(_) for _ in line.strip().split(',')])
    for item in around:
        if tuple(cube + item) in cubes:
            surface -= 1
        else:
            surface += 1
        cubes.add(tuple(cube))
    
print(surface)
