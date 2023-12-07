#!/usr/bin/env python

import math
import sys

def win_range(time, distance):
    min_speed = math.ceil((time - abs(math.sqrt((time ** 2) - 4 * distance))) / 2)
    if min_speed * (time - min_speed) == distance:
        min_speed += 1
    return time - 2 * min_speed + 1

times = [int(_) for _ in next(sys.stdin).split()[1:]]
distances = [int(_) for _ in next(sys.stdin).split()[1:]]

total = 1
for t, d in zip(times, distances):
    total *= win_range(t, d)

print(total)
