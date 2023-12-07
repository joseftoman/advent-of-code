#!/usr/bin/python3

import sys

ok = 0
buf = []

for line in sys.stdin:
    sides = [ int(x) for x in line.split() ]
    buf.append(sides)
    if len(buf) < 3: continue

    for i in range(0, 3):
        sides = sorted([buf[0][i], buf[1][i], buf[2][i]])
        if sides[0] + sides[1] > sides[2]: ok += 1

    buf = []

print(ok)
