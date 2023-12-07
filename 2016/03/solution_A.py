#!/usr/bin/python3

import sys

ok = 0

for line in sys.stdin:
    sides = sorted([ int(x) for x in line.split() ])
    if sides[0] + sides[1] > sides[2]: ok += 1

print(ok)
