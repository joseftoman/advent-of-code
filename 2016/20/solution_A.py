#!/usr/bin/python3

import sys
min = 0

intervals = sorted(
    [ tuple(map(int, line.rstrip().split('-'))) for line in sys.stdin ],
    key=lambda pair: pair[0]
)

for item in intervals:
    if item[0] > min: break
    if item[1] > min: min = item[1] + 1

print(min)
