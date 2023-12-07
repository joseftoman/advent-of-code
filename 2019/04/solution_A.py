#!/usr/bin/env python

import sys

low, high = next(sys.stdin).strip().split('-')
low = [int(_) for _ in low]
high = int(high)

for x in range(1, len(low)):
    if low[x] < low[x - 1]:
        low[x] = low[x - 1]

hits = 0
pos = len(low) - 1

while True:
    for x in range(0, len(low) - 1):
        if low[x] == low[x + 1]:
            hits += 1
            break

    if low[pos] < 9:
        low[pos] += 1
    else:
        while pos >= 0 and low[pos] == 9:
            pos -= 1
        if pos < 0:
            break
        low[pos] += 1
        for x in range(pos + 1, len(low)):
            low[x] = low[pos]

        pos = len(low) - 1

    if int(''.join([str(_) for _ in low])) > high:
        break

print(hits)
