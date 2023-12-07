#!/usr/bin/env python

import sys

elf = 0
calories = []

for line in sys.stdin:
    line = line.strip()
    if not line:
        calories.append(elf)
        elf = 0
    else:
        elf += int(line)

calories.append(elf)

calories.sort()
print(sum(calories[-3:]))
