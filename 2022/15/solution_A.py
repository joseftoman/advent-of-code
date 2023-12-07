#!/usr/bin/env python

import re
import sys

row = int(sys.argv[1]) if len(sys.argv) > 1 else 2_000_000
intervals = []
objects = set()
regex = re.compile('Sensor at x=([-0-9]+), y=([-0-9]+): closest beacon is at x=([-0-9]+), y=([-0-9]+)')

for line in sys.stdin:
    match = regex.match(line)
    sx, sy, bx, by = [int(_) for _ in match.groups()]
    if sy == row:
        objects.add(sx)
    if by == row:
        objects.add(bx)
    dist = abs(sx - bx) + abs(sy - by)
    if not (sy - dist <= row <= sy + dist):
        continue

    radius = dist - abs(sy - row)
    intervals.append([sx - radius, sx + radius])

intervals.sort()
objects = sorted(objects)

merged = [intervals[0]]
for item in intervals[1:]:
    if item[0] <= merged[-1][1] + 1:
        if item[1] > merged[-1][1]:
            merged[-1][1] = item[1]
    else:
        merged.append(item)

fix = 0
pos = 0
for item in objects:
    while merged[pos][1] < item:
        pos += 1

    if pos < len(merged) and merged[pos][0] <= item:
        fix += 1

print(sum(_[1] - _[0] + 1 for _ in merged) - fix)
