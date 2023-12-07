#!/usr/bin/python3

import sys
import re

nodes = {}

for line in [ l.rstrip() for l in sys.stdin ]:
    m = re.match(r'(\w+) \(\d+\)(?: -> (.*))?', line)
    g = m.groups()
    nodes[g[0]] = g[1].split(', ') if g[1] else []

roots = dict.fromkeys(nodes.keys())
for n in nodes.values():
    for k in n: roots.pop(k, None)

print(roots)
