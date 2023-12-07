#!/usr/bin/env python

import sys

orbit_map = dict()
orbit_path = dict()
total_orbits = 0

for line in sys.stdin:
    major, minor = line.rstrip().split(')')
    orbit_map[minor] = major

pos = 'YOU'
path_len = -1

while pos != 'COM':
    path_len += 1
    pos = orbit_map[pos]
    orbit_path[pos] = path_len

path_len = 0
pos = orbit_map['SAN']
while pos not in orbit_path:
    pos = orbit_map[pos]
    path_len += 1

print(path_len + orbit_path[pos])
