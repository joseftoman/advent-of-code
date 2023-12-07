#!/usr/bin/python3

import sys

def dist(x, y):
    x = abs(x)
    y = abs(y)

    if x >= y:
        return x
    else:
        return x + (y - x) / 2

for line in [ l.rstrip() for l in sys.stdin ]:
    pos = [ 0, 0 ]
    max = 0

    for step in line.split(','):
        if step == 'ne':
            pos[0] += 1
            pos[1] += 1
        if step == 'nw':
            pos[0] += -1
            pos[1] += 1
        if step == 'se':
            pos[0] += 1
            pos[1] += -1
        if step == 'sw':
            pos[0] += -1
            pos[1] += -1
        if step == 'n':
            pos[1] += 2
        if step == 's':
            pos[1] += -2

        x = dist(pos[0], pos[1])
        if x > max: max = x

    print(max)
