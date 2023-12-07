#!/usr/bin/env python

import sys

stacks = None
buffer = []

for line in sys.stdin:
    if not line.strip():
        stacks = [[] for _ in range(len(buffer[-1].split()))]
        for layer in buffer[-2::-1]:
            for index in range(len(stacks)):
                pos = index * 4 + 1
                char = ' ' if pos >= len(layer) else layer[pos]
                if char != ' ':
                    stacks[index].append(char)
        continue

    if stacks is None:
        buffer.append(line)
        continue

    tokens = line.split()
    amount, source, target = int(tokens[1]), int(tokens[3]) - 1, int(tokens[5]) - 1
    stacks[target].extend(reversed(stacks[source][-amount:]))
    del stacks[source][-amount:]

print(''.join(' ' if not _ else _[-1] for _ in stacks))
