#!/usr/bin/python3

import sys
import re

severity = 0

for line in [ l.rstrip() for l in sys.stdin ]:
    m = re.match(r'(\d+): (\d+)', line)
    layer = int(m.group(1))
    depth = int(m.group(2))
    if layer % ((depth - 1) * 2) == 0:
        severity += layer * depth

print(severity)
