#!/usr/bin/env python

import sys

prev = sys.stdin.readline().strip()[15:]
counter = 0
rules = {}
shift = 0

sys.stdin.readline()

for line in sys.stdin:
    left = line[:5]
    right = line[9]
    if right == '#':
        rules[left] = True

print(f' 0 [0]: {prev}')

while counter < 20:
    counter += 1
    current = ''

    pos = prev.find('#')
    shift += max(3 - pos, -2)
    if pos < 5:
        prev = ''.join(['.'] * (5 - pos)) + prev

    pos = prev.rfind('#')
    if pos >= len(prev) - 5:
        prev += ''.join(['.'] * (5 - len(prev) + pos + 1))

    for index in range(0, len(prev) - 4):
        if prev[index:index+5] in rules:
            current += '#'
        else:
            current += '.'

    print(f'%2d [{shift}]: {current}' % counter)
    prev = current

pot_sum = 0
for index, char in enumerate(current):
    if char == '#':
        pot_sum += index - shift

print(pot_sum)
