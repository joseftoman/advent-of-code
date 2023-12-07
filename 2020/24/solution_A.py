#!/usr/bin/env python

import sys

black = set()

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

print(len(black))
