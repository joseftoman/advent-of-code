#!/usr/bin/env python

import sys

calories = 0
best = 0

for line in sys.stdin:
    line = line.strip()
    if not line:
        if calories > best:
            best = calories
        calories = 0
    else:
        calories += int(line)

if calories > best:
    best = calories

print(best)
