#!/usr/bin/env python

import math
import sys

geo_to_diff = {'N': (0, 1), 'E': (1, 0), 'S': (0, -1), 'W': (-1, 0)}
ship = (0, 0)
waypoint = (10, 1)

def rotate(point, angle):
    angle = angle / 180 * math.pi
    return (
        round(math.sin(angle) * point[1] + math.cos(angle) * point[0]),
        round(math.cos(angle) * point[1] - math.sin(angle) * point[0]),
    )

for action, value in [(line[0], int(line[1:])) for line in sys.stdin]:
    if action == 'F':
        ship = (ship[0] + waypoint[0] * value, ship[1] + waypoint[1] * value)
    elif action == 'L':
        waypoint = rotate(waypoint, -value)
    elif action == 'R':
        waypoint = rotate(waypoint, value)
    else:
        diff = geo_to_diff[action]
        waypoint = (waypoint[0] + diff[0] * value, waypoint[1] + diff[1] * value)

print(abs(ship[0]) + abs(ship[1]))
