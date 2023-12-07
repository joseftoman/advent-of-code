#!/usr/bin/env python

from collections import defaultdict
import re
import sys

area = int(sys.argv[1]) if len(sys.argv) > 1 else 4_000_000
intervals = defaultdict(list)
regex = re.compile('Sensor at x=([-0-9]+), y=([-0-9]+): closest beacon is at x=([-0-9]+), y=([-0-9]+)')

for line in sys.stdin:
    match = regex.match(line)
    sx, sy, bx, by = [int(_) for _ in match.groups()]
    dist = abs(sx - bx) + abs(sy - by)

    for row in range(max(0, sy - dist), min(area, sy + dist) + 1):
        radius = dist - abs(sy - row)
        intervals[row].append([max(0, sx - radius), min(area, sx + radius)])

for row, spans in intervals.items():
    spans.sort()

    merged = [spans[0]]
    for item in spans[1:]:
        if item[0] <= merged[-1][1] + 1:
            if item[1] > merged[-1][1]:
                merged[-1][1] = item[1]
        else:
            merged.append(item)

    if merged[0][0] > 0:
        print(row)
        break
    if merged[-1][1] < area:
        print(area * 4_000_000 + row)
        break
    if len(merged) > 1:
        print((merged[0][1] + 1) * 4_000_000 + row)
        break
