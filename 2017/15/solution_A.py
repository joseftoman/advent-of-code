#!/usr/bin/python3

import sys
import re

prev = []
factors = (16807, 48271)
steps = int(4e7)
mask = 2 ** 16 - 1
modulo = 2 ** 31 - 1
matches = 0

for line in [ l.rstrip() for l in sys.stdin ]:
    m = re.search(r'(\d+)$', line)
    prev.append(int(m.group(1)))

for i in range(0, steps):
    prev[0] = (prev[0] * factors[0]) % modulo
    prev[1] = (prev[1] * factors[1]) % modulo

    if bin(prev[0] & mask)[2:].zfill(16) == bin(prev[1] & mask)[2:].zfill(16):
        matches += 1

print(matches)
