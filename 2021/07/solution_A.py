#!/usr/bin/env python

import sys

crabs = [int(_) for _ in sys.stdin.readline().split(',')]
crabs.sort()
best = [None, None]

for pos in range(crabs[0], crabs[-1] + 1):
    fuel = 0
    for crab in crabs:
        fuel += abs(crab - pos)

    if best[1] is None or fuel < best[1]:
        best = [pos, fuel]

print(best[1])
