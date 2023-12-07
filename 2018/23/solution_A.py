#!/usr/bin/env python

import sys
import re

regex = re.compile(r'pos=<(-?\d+),(-?\d+),(-?\d+)>,\s+r=(\d+)')
bots = []

for line in sys.stdin:
    bots.append([int(x) for x in regex.match(line.rstrip()).groups()])

bots.sort(key=lambda x: -x[3])

hits = 1
for bot in bots[1:]:
    dist = 0
    for index in range(0, 3):
        dist += abs(bots[0][index] - bot[index])
    if dist <= bots[0][3]:
        hits += 1

print(hits)
