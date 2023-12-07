#!/usr/bin/env python

import math
import sys

vaporization_target = 200

asteroid_map = set()
width = None
height = 0

def get_visible(choice):
    global asteroid_map, width, height
    pool = set(asteroid_map)
    pool.remove(choice)
    order = sorted(pool, key=lambda x: abs(choice[0] - x[0]) + abs(choice[1] - x[1]))

    for pos in order:
        if pos not in pool:
            continue

        diff = (pos[0] - choice[0], pos[1] - choice[1])
        if diff[0] == 0:
            diff = (0, 1 if diff[1] > 0 else -1)
        elif diff[1] == 0:
            diff = (1 if diff[0] > 0 else -1, 0)
        else:
            gcd = math.gcd(*diff)
            diff = (diff[0] / gcd, diff[1] / gcd)
        pos = (pos[0] + diff[0], pos[1] + diff[1])

        while pos[0] >= 0 and pos[1] >= 0 and pos[0] < width and pos[1] < height:
            if pos in pool:
                pool.remove(pos)
            pos = (pos[0] + diff[0], pos[1] + diff[1])

    return pool

def get_vaporization_key(base, asteroid):
    hypot = math.sqrt(math.pow(asteroid[0] - base[0], 2) + math.pow(asteroid[1] - base[1], 2))
    if asteroid[0] >= base[0] and asteroid[1] <= base[1]:
        return (asteroid[0] - base[0]) / hypot
    elif asteroid[0] >= base[0] and asteroid[1] > base[1]:
        return (asteroid[1] - base[1]) / hypot + 10
    elif asteroid[0] < base[0] and asteroid[1] > base[1]:
        return (base[0] - asteroid[0]) / hypot + 20
    else:
        return (base[1] - asteroid[1]) / hypot + 30

for row, line in enumerate(sys.stdin):
    height += 1
    if width is None:
        width = len(line.strip())

    for column, char in enumerate(line.strip()):
        if char == '#':
            asteroid_map.add((column, row))

best = None

for asteroid in asteroid_map:
    visible = get_visible(asteroid)
    if best is None or len(visible) > best[0]:
        best = (len(visible), asteroid)
        #print('MAX:', asteroid)

base = best[1]
v_count = 0

while len(asteroid_map) > 1:
    visible = get_visible(base)
    for asteroid in sorted(visible, key=lambda v: get_vaporization_key(base, v)):
        asteroid_map.remove(asteroid)
        #print('Vaporized:', asteroid)
        v_count += 1
        if v_count == vaporization_target:
            print(100 * asteroid[0] + asteroid[1])
            sys.exit(0)

print('Not enough asteroids')
