#!/usr/bin/python3

import sys
import re
import itertools

nodes = []
node_re = re.compile('.*-x(\d+)-y(\d+)\s+\d+T\s+(\d+)T\s+(\d+)')
viable = 0

for line in sys.stdin:
    m = node_re.match(line)
    if m is None: continue
    nodes.append(tuple(map(int, m.groups())))

for pair in itertools.combinations(nodes, 2):
    if pair[0][2] > 0 and pair[0][2] <= pair[1][3]:
        viable += 1

    if pair[1][2] > 0 and pair[1][2] <= pair[0][3]:
        viable += 1

print(viable)
