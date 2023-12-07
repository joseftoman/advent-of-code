#!/usr/bin/python3

import sys
import re
from collections import Counter

nodes = {}

def find_imballance(node_name):
    n = nodes[node_name]
    if len(n[1]) == 0: return n[0]

    w = {}
    for child in n[1]: w[child] = find_imballance(child)

    c = Counter(w.values())
    diff = c.most_common()
    if len(diff) == 2:
        for child in n[1]:
            if w[child] == diff[1][0]:
                print(nodes[child][0] + diff[0][0] - diff[1][0])
                exit()

    return n[0] + sum(w.values())

for line in [ l.rstrip() for l in sys.stdin ]:
    m = re.match(r'(\w+) \((\d+)\)(?: -> (.*))?', line)
    g = m.groups()
    nodes[g[0]] = (int(g[1]), g[2].split(', ') if g[2] else [])

roots = dict.fromkeys(nodes.keys())
for n in nodes.values():
    for k in n[1]: roots.pop(k, None)

root = list(roots.keys())[0]
find_imballance(root)
