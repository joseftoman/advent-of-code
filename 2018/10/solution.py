#!/usr/bin/env python

import re
import sys

if len(sys.argv) != 3:
    print(f'usage: {sys.argv[0]} probe|render FAST_FORWARD')
    sys.exit(1)

command = sys.argv[1]
skip = int(sys.argv[2])
points = []
re_point = re.compile(r'position=<\s*(-?\d+),\s*(-?\d+)>\s+velocity=<\s*(-?\d+),\s*(-?\d+)>')

def get_area():
    min_x = min_y = max_x = max_y = None

    for p in points:
        if min_x is None or p[0] < min_x: min_x = p[0]
        if min_y is None or p[1] < min_y: min_y = p[1]
        if max_x is None or p[0] > max_x: max_x = p[0]
        if max_y is None or p[1] > max_y: max_y = p[1]

    return (min_x, min_y, max_x, max_y)

def sum_area(area):
    return area[2] + area[3] - area[0] - area[1]

def go_forward(quotient=1):
    for p in points:
        p[0] += p[2] * quotient
        p[1] += p[3] * quotient

def render():
    area = get_area()
    pixels = {}

    for p in points:
        pixels[(p[0], p[1])] = 1

    for y in range(area[1], area[3] + 1):
        line = ''
        for x in range(area[0], area[2] + 1):
            line += '#' if (x, y) in pixels else ' '
        print(line)

for line in sys.stdin:
    points.append([int(x) for x in re_point.match(line).groups()])

go_forward(skip)

if sys.argv[1] == 'probe':
    for step in range(0, 10):
        print(f'{skip + step}: {sum_area(get_area())}')
        go_forward()
else:
    for step in range(0, 5):
        print(f'\nAfter {skip + step} seconds:')
        render()
        go_forward()
