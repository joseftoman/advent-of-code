#!/usr/bin/env python

import sys

output = 0
cycle = 1
register = 1

for line in sys.stdin:
    tokens = line.split()

    if tokens[0] == 'noop':
        if (cycle - 20) % 40 == 0:
            output += cycle * register
        cycle += 1
    elif tokens[0] == 'addx':
        output_cycle = cycle
        if (cycle + 1 - 20) % 40 == 0:
            output_cycle = cycle + 1
        if (output_cycle - 20) % 40 == 0:
            output += output_cycle * register
        cycle += 2
        register += int(tokens[1])

    if cycle > 220:
        break

print(output)
