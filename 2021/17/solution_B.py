#!/usr/bin/env python

import math
import re
import sys

match = re.match(r'target area: x=([0-9-]+)\.\.([0-9-]+), y=([0-9-]+)\.\.([0-9-]+)', sys.stdin.readline())
target = [int(_) for _ in match.groups()]
hits = 0

min_x = math.floor(math.sqrt(target[0] * 2))
while True:
    reach = min_x * (min_x + 1) / 2
    if reach >= target[0]:
        break
    min_x += 1

for start_x in range(min_x, target[1] + 1):
    for start_y in range(target[2], target[2] * -1):
        x, y = 0, 0
        dx, dy = start_x, start_y

        while True:
            x += dx
            y += dy
            dx = max(0, dx - 1)
            dy -= 1

            if target[0] <= x <= target[1] and target[2] <= y <= target[3]:
                hits += 1
                break
            if x > target[1] or y < target[2]:
                break


print(hits)
