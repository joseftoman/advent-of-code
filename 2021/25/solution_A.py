#!/usr/bin/env python

import sys

east = set()
south = set()
width = 0
height = 0

for line in sys.stdin:
    if height == 0:
        width = len(line.strip())
    for index, pos in enumerate(list(line)):
        if pos == '>':
            east.add((index, height))
        elif pos == 'v':
            south.add((index, height))
    height += 1

step = 0
while True:
    step += 1
    moves = 0
    new_south = set()
    new_east = set()

    for c in east:
        new_c = ((c[0] + 1) % width, c[1])
        if new_c not in east and new_c not in south:
            new_east.add(new_c)
            moves += 1
        else:
            new_east.add(c)

    for c in south:
        new_c = (c[0], (c[1] + 1) % height)
        if new_c not in new_east and new_c not in south:
            new_south.add(new_c)
            moves += 1
        else:
            new_south.add(c)

    if not moves:
        break

    east = new_east
    south = new_south

print(step)
