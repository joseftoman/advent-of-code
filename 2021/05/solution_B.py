#!/usr/bin/env python

from collections import defaultdict
import sys

points = defaultdict(int)
overlaps = 0

for line in sys.stdin:
    start, end = line.split(' -> ')
    x1, y1 = [int(_) for _ in start.split(',')]
    x2, y2 = [int(_) for _ in end.split(',')]
    
    inc_x = 0 if x1 == x2 else (1 if x2 > x1 else -1)
    inc_y = 0 if y1 == y2 else (1 if y2 > y1 else -1)

    for dist in range(max(abs(x1 - x2), abs(y1 - y2)) + 1):
        point = x1 + dist * inc_x, y1 + dist * inc_y

        points[point] += 1
        if points[point] == 2:
            overlaps += 1

print(overlaps)
