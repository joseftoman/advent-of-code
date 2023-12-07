#!/usr/bin/env python

import sys

cubes = set()

for x, line in enumerate(sys.stdin):
    for y, char in enumerate(line.strip()):
        if char == '#':
            cubes.add((x, y, 0))

for _ in range(6):
    new = set()
    done = set()

    for cube in cubes:
        x, y, z = cube
        for x1 in range(-1, 2):
            for y1 in range(-1, 2):
                for z1 in range(-1, 2):
                    to_test = (x + x1, y + y1, z + z1)
                    if to_test in done:
                        continue
    
                    around = 0
                    for x2 in range(-1, 2):
                        for y2 in range(-1, 2):
                            for z2 in range(-1, 2):
                                if x2 == 0 and y2 == 0 and z2 == 0:
                                    continue
                                neighbour = (x + x1 + x2, y + y1 + y2, z + z1 + z2)
                                if neighbour in cubes:
                                    around += 1

                    if to_test in cubes and 2 <= around <= 3:
                        new.add(to_test)
                    if to_test not in cubes and around == 3:
                        new.add(to_test)
                    done.add(to_test)

    cubes = new

print(len(cubes))
