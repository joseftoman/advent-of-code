#!/usr/bin/env python

import sys


def cpu_cycles():
    register = 1

    for line in sys.stdin:
        tokens = line.split()

        if tokens[0] == 'noop':
            yield register
        elif tokens[0] == 'addx':
            yield register
            yield register
            register += int(tokens[1])

    raise StopIteration()


for cycle, register in enumerate(cpu_cycles(), 1):
    if register - 1 <= (cycle - 1) % 40 <= register + 1:
        print('#', end='')
    else:
        print('.', end='')
    if cycle % 40 == 0:
        print()

    if cycle == 240:
        break
