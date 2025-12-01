#!/usr/bin/env python

import sys

dial = 50
password = 0


for line in sys.stdin:
    sign = -1 if line[0] == 'L' else 1
    shift = int(line[1:])
    next_dial = dial + sign * shift

    if dial > 0 and next_dial <= 0:
        password += 1
    password += abs(next_dial) // 100

    dial = next_dial % 100

print(password)
