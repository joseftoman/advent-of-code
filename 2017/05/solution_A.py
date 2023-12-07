#!/usr/bin/python3

import sys

steps = 0
ins = [ int(l.rstrip()) for l in sys.stdin ]
pos = 0

while pos < len(ins):
    ins[pos] += 1
    pos += ins[pos] - 1
    steps += 1

print(steps)
