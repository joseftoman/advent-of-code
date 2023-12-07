#!/usr/bin/env python

import sys

total = 0
digits = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}

for line in sys.stdin:
    left = ''
    right = ''

    for char in line:
        if char in digits:
            left = char
            break
    for char in reversed(line):
        if char in digits:
            right = char
            break

    total += int(left) * 10 + int(right)

print(total)
