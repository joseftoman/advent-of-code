#!/usr/bin/env python

import math
import sys

def win_range(time, distance):
    min_speed = math.ceil((time - abs(math.sqrt((time ** 2) - 4 * distance))) / 2)
    if min_speed * (time - min_speed) == distance:
        min_speed += 1
    return time - 2 * min_speed + 1

time = int(''.join(next(sys.stdin).split()[1:]))
distance = int(''.join(next(sys.stdin).split()[1:]))

print(win_range(time, distance))
