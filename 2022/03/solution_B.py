#!/usr/bin/env python

import sys

priorities = 0
group = []

for line in sys.stdin:
    line = line.strip()
    group.append(line)
    if len(group) == 3:
        item = list(set(group[0]) & set(group[1]) & set(group[2]))[0]
        offset = 38 if item < 'a' else 96
        priorities += ord(item) - offset
        group = []

print(priorities)
