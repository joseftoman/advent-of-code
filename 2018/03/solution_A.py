#!/usr/bin/env python

import sys
import re

fabric_size = 10_000
fabric = [[0] * fabric_size for _ in range(0, fabric_size)]
parser = re.compile(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)$')
overlaps = 0

for line in sys.stdin:
    (rid, left, top, width, height) = [int(group) for group in parser.match(line.strip()).groups()]
    for row in range(top, top + height):
        for col in range(left, left + width):
            fabric[row][col] += 1
            if fabric[row][col] == 2:
                overlaps += 1

print(overlaps)
