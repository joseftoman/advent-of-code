#!/usr/bin/env python

import sys

grid_size = 300
gsn = 3999
grid = {}

for x in range(1, grid_size + 1):
    for y in range(1, grid_size + 1):
        grid[(x, y)] = (((x + 10) * y + gsn) * (x + 10)) % 1000 // 100 - 5

best = [None, None, None, None]
print(0)
for x in range(1, grid_size + 1):
    for y in range(1, grid_size + 1):
        power = 0
        for s in range(1, grid_size - max(x, y) + 2):
            for i in range(0, s - 1):
                power += grid[(x+i, y+s-1)]
                power += grid[(x+s-1, y+i)]
            power += grid[(x+s-1, y+s-1)]

            if best[0] is None or power > best[0]:
                best = [power, x, y, s]

    print('\033[1A\033[K', end='')
    print(x)

print('\033[1A\033[K', end='')
print(best)
