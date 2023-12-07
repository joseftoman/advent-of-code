#!/usr/bin/env python

import math
import re
import sys

regex_input = re.compile(r'^<x=(-?\d+), y=(-?\d+), z=(-?\d+)>$')
moons = []
periods = []

for moon in sys.stdin:
    match = regex_input.match(moon.strip())
    moons.append([*[int(_) for _ in match.groups()], 0, 0, 0])

for coord in range(0, 3):
    seen = set()
    current_coords = []
    for moon in moons:
        current_coords.append(moon[coord])
        current_coords.append(moon[coord + 3])
    current_coords = tuple(current_coords)

    while current_coords not in seen:
        seen.add(current_coords)
        next_coords = list(current_coords)

        for i1 in range(0, len(moons)):
            for i2 in range(0, len(moons)):
                if i1 == i2:
                    continue

                if next_coords[2 * i1] < next_coords[2 * i2]:
                    next_coords[2 * i1 + 1] += 1
                elif next_coords[2 * i1] > next_coords[2 * i2]:
                    next_coords[2 * i1 + 1] -= 1

        for pos in range(0, len(moons)):
            next_coords[2 * pos] += next_coords[2 * pos + 1]

        current_coords = tuple(next_coords)

    periods.append(len(seen))

lcm = periods[0]
for p in periods[1:]:
    lcm = lcm * p // math.gcd(lcm, p)

print(lcm)
