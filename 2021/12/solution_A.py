#!/usr/bin/env python

from collections import defaultdict
import sys

caves = defaultdict(set)
paths = 0

for line in sys.stdin:
    a, b = line.strip().split('-')
    caves[a].add(b)
    caves[b].add(a)

def extend(cave, visited):
    global paths
    global caves

    if cave == 'end':
        paths += 1
        return

    for option in caves[cave]:
        if option == option.lower() and option in visited:
            continue
        extend(option, {*visited, cave})


extend('start', set())
print(paths)
