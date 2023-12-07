#!/usr/bin/env python

from collections import defaultdict
import re
import sys

dots = set()

while True:
    line = sys.stdin.readline().rstrip()
    if not line:
        break
    x, y = line.split(',')
    dots.add((int(x), int(y)))

for line in sys.stdin:
    match = re.match('fold along (x|y)=(\d+)', line)
    new_dots = set()

    for dot in dots:
        fold = int(match.group(2))
        if match.group(1) == 'y':
            if dot[1] > fold:
                new_dots.add((dot[0], fold - (dot[1] - fold)))
            else:
                new_dots.add(dot)
        else:
            if dot[0] > fold:
                new_dots.add((fold - (dot[0] - fold), dot[1]))
            else:
                new_dots.add(dot)

    dots = new_dots

sheet = defaultdict(set)
max_x = max_y = 0

for dot in dots:
    if dot[0] > max_x:
        max_x = dot[0]
    if dot[1] > max_y:
        max_y = dot[1]

    sheet[dot[1]].add(dot[0])

for y in range(max_y + 1):
    print(''.join(['#' if x in sheet[y] else '.' for x in range(max_x + 1)]))
