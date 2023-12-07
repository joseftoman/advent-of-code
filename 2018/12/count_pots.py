#!/usr/bin/env python

import sys

shift = int(sys.argv[1])
pots = sys.argv[2]

pot_sum = 0
for index, char in enumerate(pots):
    if char == '#':
        pot_sum += index + shift

print(pot_sum)
