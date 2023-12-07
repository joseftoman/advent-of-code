#!/usr/bin/env python

import sys

width = None
length = 0
trees = set()

for line in sys.stdin:
    line = line.strip()
    length += 1
    if width is None:
        width = len(line)

    for index, char in enumerate(line):
        if char == '#':
            trees.add((index, length - 1))

hits = 0
pos = (0, 0)
move = (3, 1)

while pos[1] < length:
    if pos in trees:
        hits += 1
    pos = ((pos[0] + move[0]) % width, pos[1] + move[1])

print(hits)
