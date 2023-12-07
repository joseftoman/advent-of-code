#!/usr/bin/env python

import sys

geo_to_int = {'N': 0, 'E': 1, 'S': 2, 'W': 3}
int_to_geo = {0: 'N', 1: 'E', 2: 'S', 3: 'W'}
geo_to_diff = {'N': (0, 1), 'E': (1, 0), 'S': (0, -1), 'W': (-1, 0)}

pos = (0, 0)
ori = 'E'

for action, value in [(line[0], int(line[1:])) for line in sys.stdin]:
    if action == 'F':
        diff = geo_to_diff[ori]
        pos = (pos[0] + diff[0] * value, pos[1] + diff[1] * value)
    elif action == 'L':
        ori = int_to_geo[(geo_to_int[ori] - value / 90) % 4]
    elif action == 'R':
        ori = int_to_geo[(geo_to_int[ori] + value / 90) % 4]
    else:
        diff = geo_to_diff[action]
        pos = (pos[0] + diff[0] * value, pos[1] + diff[1] * value)

print(abs(pos[0]) + abs(pos[1]))
