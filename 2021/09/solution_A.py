#!/usr/bin/env python

import sys

caves = [[int(_) for _ in line.strip()] for line in sys.stdin]
risk_level = 0

for y in range(len(caves)):
    for x in range(len(caves[0])):
        around = []

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            x1, y1 = x + dx, y + dy
            if x1 >= 0 and x1 < len(caves[0]) and y1 >= 0 and y1 < len(caves):
                around.append(caves[y1][x1])

        if min(around) > caves[y][x]:
            risk_level += 1 + caves[y][x]

print(risk_level)
