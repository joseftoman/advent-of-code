#!/usr/bin/env python

import sys

dial = 50
password = 0


for line in sys.stdin:
    sign = -1 if line[0] == 'L' else 1
    shift = int(line[1:])
    dial = (dial + sign * shift) % 100
    if dial == 0:
        password += 1

print(password)
