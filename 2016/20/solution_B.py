#!/usr/bin/python3

import sys
allowed = 0
start = 0
max = 4294967295

intervals = sorted(
    [ tuple(map(int, line.rstrip().split('-'))) for line in sys.stdin ],
    key=lambda pair: pair[0]
)

for item in intervals:
    if item[0] > start: allowed += item[0] - start
    if item[1] >= start: start = item[1] + 1

if start <= max: allowed += max + 1 - start

print(allowed)
