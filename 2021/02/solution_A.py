#!/usr/bin/env python

import sys

forward = 0
depth = 0

for line in sys.stdin:
    cmd, value = line.split()
    if cmd == 'forward':
        forward += int(value)
    elif cmd == 'up':
        depth -= int(value)
    else:
        depth += int(value)

print(forward * depth)
