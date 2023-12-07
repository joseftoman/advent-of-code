#!/usr/bin/env python

import sys

orbit_map = dict()
total_orbits = 0

def count_orbits(space_object):
    if space_object == 'COM':
        return 0

    if orbit_map[space_object][1] is None:
        orbit_map[space_object][1] = 1 + count_orbits(orbit_map[space_object][0])

    return orbit_map[space_object][1]

for line in sys.stdin:
    major, minor = line.rstrip().split(')')
    orbit_map[minor] = [major, None]

for space_object in orbit_map.keys():
    total_orbits += count_orbits(space_object)
    #print(f'{space_object}: {count_orbits(space_object)}')

print(total_orbits)
