#!/usr/bin/env python

import sys


lines = [_.strip() for _ in sys.stdin]
matches = {'MSAMS', 'MMASS', 'SSAMM', 'SMASM'}
total = 0

for row in range(1, len(lines) - 1):
    for col in range(1, len(lines) - 1):
        if ''.join([lines[row - 1][col - 1], lines[row - 1][col + 1], lines[row][col], lines[row + 1][col - 1], lines[row + 1][col + 1]]) in matches:
            total += 1

print(total)
