#!/usr/bin/env python

from collections import Counter
import sys

size = None
counts = []

for line in sys.stdin:
    line = line.strip()
    if size is None:
        size = len(line)
        for _ in range(size):
            counts.append(Counter())

    for index, bit in enumerate(line):
        counts[size - index - 1][bit] += 1

gamma = 0
epsilon = 0

for index in range(size):
    if counts[index].most_common(1)[0][0] == '0':
        epsilon += 2 ** index
    else:
        gamma += 2 ** index

print(gamma * epsilon)
