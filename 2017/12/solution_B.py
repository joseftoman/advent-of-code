#!/usr/bin/python3

import sys
import re

node_map = {}
sets = {}

for line in [ l.rstrip() for l in sys.stdin ]:
    m = re.match(r'(\d+) <-> (.*)', line)
    nodes = set([ int(m.group(1)) ] + [ int(x) for x in m.group(2).split(', ') ])

    cur_set = None
    for n in nodes:
        if n in node_map and (cur_set is None or node_map[n] < cur_set): cur_set = node_map[n]

    if cur_set is None:
        set_label = min(nodes)
        sets[set_label] = nodes
        for n in nodes:
            node_map[n] = set_label
    else:
        for n in nodes:
            if n not in node_map:
                node_map[n] = cur_set
                sets[cur_set].add(n)
            elif node_map[n] != cur_set:
                to_merge = sets.pop(node_map[n])
                sets[cur_set] |= to_merge
                for n2 in to_merge:
                    node_map[n2] = cur_set


print(len(sets))
