#!/usr/bin/env python

import re
import sys

cubes = set()
inst = re.compile('^(on|off) x=(-?\d+)\.\.(-?\d+),y=(-?\d+)\.\.(-?\d+),z=(-?\d+)\.\.(-?\d+)$')

for line in sys.stdin:
    match = inst.match(line)
    for x in range(max(-50, int(match.group(2))), min(50, int(match.group(3))) + 1):
        for y in range(max(-50, int(match.group(4))), min(50, int(match.group(5))) + 1):
            for z in range(max(-50, int(match.group(6))), min(50, int(match.group(7))) + 1):
                if match.group(1) == 'on':
                    cubes.add((x, y, z))
                else:
                    cubes.discard((x, y, z))

print(len(cubes))
