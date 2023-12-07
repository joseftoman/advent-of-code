#!/usr/bin/env python

import sys

cups = [int(_) for _ in sys.stdin.readline().rstrip()]

for _ in range(100):
    left = set(cups[4:])
    dest = cups[0] - 1
    while dest not in left:
        dest -= 1
        if dest < 1:
            dest = 9

    pos = cups.index(dest)
    cups = [*cups[4:pos], dest, *cups[1:4], *cups[pos + 1:], cups[0]]

split = cups.index(1)
print(''.join([str(_) for _ in cups[split + 1:] + cups[:split]]))
