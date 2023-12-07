#!/usr/bin/env python

from graphlib import TopologicalSorter
from collections import defaultdict
import sys

resolved = {}
rules = {}
graph = defaultdict(set)


def resolve(name, parts):
    arg1, arg2 = resolved[parts[0]], resolved[parts[2]]
    output = 0

    if parts[1] == '+':
        output = arg1 + arg2
    elif parts[1] == '-':
        output = arg1 - arg2
    elif parts[1] == '*':
        output = arg1 * arg2
    elif parts[1] == '/':
        output = arg1 // arg2

    resolved[name] = output


for line in sys.stdin:
    tokens = line.strip().split()
    name = tokens[0][:-1]
    if len(tokens) == 2:
        resolved[name] = int(tokens[1])
    else:
        rules[name] = tokens[1:]
        graph[name].add(tokens[1])
        graph[name].add(tokens[3])

sorter = TopologicalSorter(graph)
for node in sorter.static_order():
    if node not in resolved:
        resolve(node, rules[node])
    if node == 'root':
        print(resolved[node])
        break
