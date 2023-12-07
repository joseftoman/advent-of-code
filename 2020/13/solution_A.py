#!/usr/bin/env python

import sys

timestamp = int(sys.stdin.readline().strip())
buses = [int(bus) for bus in sys.stdin.readline().strip().split(',') if bus != 'x']
best = None

for bus in buses:
    wait = bus - (timestamp % bus)
    if best is None or wait < best[0]:
        best = (wait, bus)

print(best[0] * best[1])
