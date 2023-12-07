#!/usr/bin/env python

import sys

grid_size = 300
gsn = 3999
grid = {}

for x in range(1, grid_size + 1):
    for y in range(1, grid_size + 1):
        grid[(x, y)] = (((x + 10) * y + gsn) * (x + 10)) % 1000 // 100 - 5

best = [None, None, None]
for x in range(1, grid_size - 2):
    for y in range(1, grid_size - 2):
        power = 0
        for i in (0, 1, 2):
            for j in (0, 1, 2):
                power += grid[(x+i, y+j)]

        if best[0] is None or power > best[0]:
            best = [power, x, y]

print(best)
