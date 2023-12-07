#!/usr/bin/env python

from collections import defaultdict
import sys

caves = defaultdict(set)
paths = 0

for line in sys.stdin:
    a, b = line.strip().split('-')
    caves[a].add(b)
    caves[b].add(a)

def extend(cave, visited, small_revisited):
    global paths
    global caves

    if cave == 'end':
        paths += 1
        return

    for option in caves[cave]:
        if option == option.lower() and (option == 'start' or (option in visited and small_revisited)):
            continue

        extend(option, {*visited, cave}, small_revisited or (option == option.lower() and option in visited))


extend('start', set(), False)
print(paths)
