#!/usr/bin/env python

# Modular arithmetics: https://codeforces.com/blog/entry/72593

import re
import sys

cards = 119315717514047
shuffles = 101741582076661
target = 2020
a, b = 1, 0

regex_cut = re.compile('(-?\d+)')

for line in sys.stdin:
    line = line.strip()

    if line == 'deal into new stack':
        la, lb = -1, -1
    elif line[:3] == 'cut':
        cut = int(regex_cut.match(line[4:]).group(1))
        la, lb = 1, -cut
    else:
        la, lb = int(line[20:]), 0

    a = (la * a) % cards
    b = (la * b + lb) % cards

def inversion(a, n):
    return pow(a, n - 2, n)

comp_a = pow(a, shuffles, cards)
comp_b = (b * (comp_a - 1) * inversion(a - 1, cards)) % cards

print(((target - comp_b) * inversion(comp_a, cards)) % cards)
