#!/usr/bin/python3

import sys
import re

prev = []
factors = (16807, 48271)
masks = (4, 8)
steps = int(5e6)
judge_mask = 2 ** 16 - 1

modulo = 2 ** 31 - 1
matches = 0

for line in [ l.rstrip() for l in sys.stdin ]:
    m = re.search(r'(\d+)$', line)
    prev.append(int(m.group(1)))

for i in range(0, steps):
    for i in (0, 1):
        while True:
            prev[i] = (prev[i] * factors[i]) % modulo
            if prev[i] & (masks[i] - 1) == 0:
                break

    if bin(prev[0] & judge_mask)[2:].zfill(16) == bin(prev[1] & judge_mask)[2:].zfill(16):
        matches += 1

print(matches)
