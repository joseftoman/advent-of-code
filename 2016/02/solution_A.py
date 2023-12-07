#!/usr/bin/python3

import sys

steps = {
    'L': (-1, {1, 4, 7}),
    'R': ( 1, {3, 6, 9}),
    'U': (-3, {1, 2, 3}),
    'D': ( 3, {7, 8, 9}),
}
pos = 5
code = ''

for line in [ l.rstrip() for l in sys.stdin ]:
    for dir in line:
        if pos in steps[dir][1]: continue
        pos += steps[dir][0]

    code += str(pos)

print(code)
