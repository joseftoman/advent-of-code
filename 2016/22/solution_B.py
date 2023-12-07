#!/usr/bin/python3

import sys
import re
import itertools

nodes = ['.'] * 31 * 31
node_re = re.compile('.*-x(\d+)-y(\d+)\s+(\d+)T\s+(\d+)T')

for line in sys.stdin:
    m = node_re.match(line)
    if m is None: continue

    pos = int(m.group(2)) * 31 + int(m.group(1))
    if pos == 30:
        nodes[pos] = 'G'
    elif int(m.group(3)) > 100:
        nodes[pos] = '#'
    elif int(m.group(4)) == 0:
        nodes[pos] = '_'

for i in range(0, 31):
    print(''.join(nodes[31*i:31*(i+1)]))

# It's more effective to find the shortest path manually...
