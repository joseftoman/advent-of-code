#!/usr/bin/env python

from collections import defaultdict
import sys

total = 0
digits = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
schema = []
gears = defaultdict(list)

for line in sys.stdin:
    schema.append(line.strip())

for y, row in enumerate(schema):
    x = 0
    buffer = ''
    while x < len(row):
        if row[x] in digits:
            buffer += row[x]
            if x == len(row) - 1 or row[x + 1] not in digits:
                left = max(0, x - len(buffer))
                right = min(x + 1, len(row) - 1)
                around = []

                if y > 0:
                    for pos in range(left, right + 1):
                        around.append((y - 1, pos))
                if x - len(buffer) >= 0:
                    around.append((y, x - len(buffer)))
                if x + 1 <= len(row) - 1:
                    around.append((y, x + 1))
                if y + 1 < len(schema):
                    for pos in range(left, right + 1):
                        around.append((y + 1, pos))

                for pos in around:
                    char = schema[pos[0]][pos[1]]
                    if char == '*':
                        gears[pos].append(int(buffer))

                buffer = ''
        x += 1

for gear in gears.values():
    if len(gear) == 2:
        total += gear[0] * gear[1]

print(total)
