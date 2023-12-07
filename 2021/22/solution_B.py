#!/usr/bin/env python

import re
import sys

import numpy as np

inst = re.compile('^(on|off) x=(-?\d+)\.\.(-?\d+),y=(-?\d+)\.\.(-?\d+),z=(-?\d+)\.\.(-?\d+)$')
cubes = {}

for line in sys.stdin:
    match = inst.match(line)
    cubes[((int(match.group(2)), int(match.group(3)) + 1), (int(match.group(4)), int(match.group(5)) + 1), (int(match.group(6)), int(match.group(7)) + 1))] = match.group(1) == 'on'

xs, ys, zs = map(np.unique, zip(*cubes))
xd, yd, zd = map(np.diff, [xs, ys, zs])
sizes = np.einsum('i, j, k', xd,yd,zd)
state = np.zeros(sizes.shape, bool)

f = lambda xs,x: slice(*np.searchsorted(xs,x))
for (x, y, z), s in cubes.items():
    state[f(xs,x), f(ys,y), f(zs,z)] = s

print((state*sizes).sum())
