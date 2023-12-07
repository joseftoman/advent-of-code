#!/usr/bin/env python

import sys

trees = [[int(_) for _ in row.strip()] for row in sys.stdin]
best = 0

for y in range(1, len(trees) - 1):
    for x in range(1, len(trees[0]) - 1):
        view = []

        dist = 1
        while x - dist > 0 and trees[y][x - dist] < trees[y][x]:
            dist += 1
        view.append(dist)

        dist = 1
        while x + dist < len(trees[0]) - 1 and trees[y][x + dist] < trees[y][x]:
            dist += 1
        view.append(dist)

        dist = 1
        while y - dist > 0 and trees[y - dist][x] < trees[y][x]:
            dist += 1
        view.append(dist)

        dist = 1
        while y + dist < len(trees) - 1 and trees[y + dist][x] < trees[y][x]:
            dist += 1
        view.append(dist)

        score = view[0] * view[1] * view[2] * view[3]
        if score > best:
            best = score

print(best)
