#!/usr/bin/python3

import sys

steps = 0
ins = [ int(l.rstrip()) for l in sys.stdin ]
pos = 0
prev = None

while pos < len(ins):
    prev = pos
    pos += ins[pos]
    steps += 1
    if ins[prev] < 3:
        ins[prev] += 1
    else:
        ins[prev] -= 1

print(steps)
