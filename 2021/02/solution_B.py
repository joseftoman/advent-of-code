#!/usr/bin/env python

import sys

aim = 0
forward = 0
depth = 0

for line in sys.stdin:
    cmd, value = line.split()
    if cmd == 'forward':
        forward += int(value)
        depth += aim * int(value)
    elif cmd == 'up':
        aim -= int(value)
    else:
        aim += int(value)

print(forward * depth)
