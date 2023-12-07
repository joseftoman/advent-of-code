#!/usr/bin/env python

import sys

black = set()
around = ((2, 0), (1, -1), (-1, -1), (-2, 0), (-1, 1), (1, 1))

def inspect(x, y, is_black, new):
    hits = 0
    for diff in around:
        if (x + diff[0], y + diff[1]) in black:
            hits += 1
    
    if is_black and 1 <= hits <= 2:
        new.add((x, y))
    if not is_black and hits == 2:
        new.add((x, y))


for path in sys.stdin:
    path = path.rstrip()
    pos = 0
    x = 0
    y = 0

    while pos < len(path):
        if path[pos] == 'e':
            x += 2
            pos += 1
        elif path[pos] == 'w':
            x -= 2
            pos += 1
        elif path[pos] == 'n':
            y += 1
            if path[pos + 1] == 'e':
                x += 1
            else:
                x -= 1
            pos += 2
        else:
            y -= 1
            if path[pos + 1] == 'e':
                x += 1
            else:
                x -= 1
            pos += 2

    if (x, y) in black:
        black.remove((x, y))
    else:
        black.add((x, y))

for d in range(100):
    done = set()
    new_black = set()
    
    for x, y in black:
        inspect(x, y, True, new_black)
        done.add((x, y))

        for diff in around:
            xa = x + diff[0]
            ya = y + diff[1]
            if (xa, ya) in done:
                continue
            inspect(xa, ya, False, new_black)
            done.add((xa, ya))

    black = new_black

print(len(black))
