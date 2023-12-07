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

while counter < 1000:
    counter += 1
    current = ''

    prev = '.....' + prev
    shift -= 3

    pos = prev.rfind('#')
    if pos >= len(prev) - 5:
        prev += ''.join(['.'] * (5 - len(prev) + pos + 1))

    for index in range(0, len(prev) - 4):
        if prev[index:index+5] in rules:
            current += '#'
        else:
            current += '.'

    pos = current.find('#')
    current = current[pos:]
    shift += pos

    print('%6d [%3d]: %s' % (counter, shift, current))
    prev = current
