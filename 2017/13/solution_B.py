#!/usr/bin/python3

import sys
import re

layers = []

def test_time(t):
    for l in layers:
        if (l[0] + t) % ((l[1] - 1) * 2) == 0:
            return False

    return True

for line in [ l.rstrip() for l in sys.stdin ]:
    m = re.match(r'(\d+): (\d+)', line)
    layer = int(m.group(1))
    depth = int(m.group(2))
    layers.append((layer, depth))

time = 0
while not test_time(time):
    time += 1

print(time)
