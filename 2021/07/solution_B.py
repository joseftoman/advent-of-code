#!/usr/bin/env python

import sys

crabs = [int(_) for _ in sys.stdin.readline().split(',')]
crabs.sort()
best = [None, None]

for pos in range(crabs[0], crabs[-1] + 1):
    fuel = 0
    for crab in crabs:
        change = abs(crab - pos)
        fuel += int(change * (change + 1) / 2)

    if best[1] is None or fuel < best[1]:
        best = [pos, fuel]

print(best[1])
