#!/usr/bin/python3

import sys

counts = []
msg = ''

for line in sys.stdin:
    line = line.rstrip()

    for i in range(0, len(line)):
        if len(counts) < i + 1: counts.append({})
        if line[i] not in counts[i]: counts[i][line[i]] = 0
        counts[i][line[i]] += 1

for pos in counts:
    msg += sorted(pos.keys(), key = lambda ch: pos[ch])[0]

print(msg)
