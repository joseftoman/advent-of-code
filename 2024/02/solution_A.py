#!/usr/bin/env python

import sys

safe = 0

def cmp(a, b):
    if a == b or abs(a - b) > 3:
        return 0
    return -1 if a < b else 1

for line in sys.stdin:
    levels = [int(_) for _ in line.split()]
    target = cmp(levels[0], levels[1])
    if target == 0:
        continue

    ok = True
    for i in range(2, len(levels)):
        if cmp(levels[i - 1], levels[i]) != target:
            ok = False
            break

    if ok:
        safe += 1
    

print(safe)
