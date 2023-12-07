#!/usr/bin/python3

import sys

current = sys.stdin.readline().rstrip()
safe = len([ ch for ch in current if ch == '.'])
left = 399999
is_trap = set(['^..', '^^.', '.^^', '..^'])

while left > 0:
    current = '.'+current+'.'
    next = ''

    for i in range(1, len(current) - 1):
        if current[i-1:i+2] in is_trap:
            next += '^'
        else:
            next += '.'
            safe += 1

    left -= 1
    current = next

print(safe)
