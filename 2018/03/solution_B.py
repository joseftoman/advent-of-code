#!/usr/bin/env python

import sys
import re

fabric_size = 10_000
parser = re.compile(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)$')
claims = []

for line in sys.stdin:
    (rid, left, top, width, height) = [int(group) for group in parser.match(line.strip()).groups()]
    claims.append([True, rid, left, top, left + width - 1, top + height - 1])

claims.sort(key=lambda x: (x[4] - x[2]) * (x[5] - x[3]), reverse=True)

for c1 in claims:
    if not c1[0]: continue
    for c2 in claims:
        if c1[1] == c2[1]: continue
        if c1[2] <= c2[4] and c1[4] >= c2[2] and c1[3] <= c2[5] and c1[5] >= c2[3]:
            c1[0] = False
            c2[0] = False
            break

    if c1[0]:
        print(c1[1])
