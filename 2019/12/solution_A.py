#!/usr/bin/env python

import re
import sys

regex_input = re.compile(r'^<x=(-?\d+), y=(-?\d+), z=(-?\d+)>$')
moons = []
finish_time = 1000

for moon in sys.stdin:
    match = regex_input.match(moon.strip())
    moons.append([*[int(_) for _ in match.groups()], 0, 0, 0])

for time in range(0, finish_time):
    next_moons = []

    for m1 in moons:
        next_moon = m1[:]

        for m2 in moons:
            if m1 is m2:
                continue

            for pos in range(0, 3):
                if m1[pos] < m2[pos]:
                    next_moon[pos + 3] += 1
                elif m1[pos] > m2[pos]:
                    next_moon[pos + 3] -= 1

        for pos in range(0, 3):
            next_moon[pos] += next_moon[pos + 3]

        next_moons.append(next_moon)

    moons = next_moons

energy = 0

for moon in moons:
    moon = list(map(abs, moon))
    energy += sum(moon[:3]) * sum(moon[3:])

print(energy)
