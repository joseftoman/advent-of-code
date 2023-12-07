#!/usr/bin/env python

from collections import defaultdict
import sys

points = defaultdict(int)
overlaps = 0

for line in sys.stdin:
    start, end = line.split(' -> ')
    x1, y1 = [int(_) for _ in start.split(',')]
    x2, y2 = [int(_) for _ in end.split(',')]
    if not (x1 == x2 or y1 == y2):
        continue

    for i in range(min(x1, x2), max(x1, x2) + 1):
        for j in range(min(y1, y2), max(y1, y2) + 1):
            points[(i, j)] += 1
            if points[(i, j)] == 2:
                overlaps += 1

print(overlaps)
