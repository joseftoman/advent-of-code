#!/usr/bin/python3

import sys

for line in [ l.rstrip() for l in sys.stdin ]:
    pos = [ 0, 0 ]
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

    pos = [ abs(pos[0]), abs(pos[1]) ]
    if pos[0] >= pos[1]:
        print(pos[0])
    else:
        print(pos[0] + (pos[1] - pos[0]) / 2)
