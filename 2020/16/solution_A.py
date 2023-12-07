#!/usr/bin/env python

import sys

available = set()
state = 1
error = 0

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    if line == 'your ticket:':
        state = 2
        continue
    if line == 'nearby tickets:':
        state = 3
        continue

    if state == 1:
        _, seats = line.split(': ')
        for interval in seats.split(' or '):
            x, y = [int(_) for _ in interval.split('-')]
            for seat in range(x, y + 1):
                available.add(seat)

    if state == 3:
        for seat in [int(_) for _ in line.split(',')]:
            if seat not in available:
                error += seat

print(error)
