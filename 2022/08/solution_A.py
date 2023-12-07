#!/usr/bin/env python

import sys

trees = [[int(_) for _ in row.strip()] for row in sys.stdin]
visible = set()

for y, row in enumerate(trees):
    top = None
    for x in range(0, len(row)):
        if top is None or row[x] > top:
            visible.add((x, y))
        if top is None or row[x] > top:
            top = row[x]
            if top == 9:
                break

    top = None
    for x in range(len(row) - 1, -1, -1):
        if top is None or row[x] > top:
            visible.add((x, y))
        if top is None or row[x] > top:
            top = row[x]
            if top == 9:
                break

for x in range(0, len(trees[0])):
    top = None
    for y in range(0, len(trees)):
        if top is None or trees[y][x] > top:
            visible.add((x, y))
        if top is None or trees[y][x] > top:
            top = trees[y][x]
            if top == 9:
                break

    top = None
    for y in range(len(trees) - 1, -1, -1):
        if top is None or trees[y][x] > top:
            visible.add((x, y))
        if top is None or trees[y][x] > top:
            top = trees[y][x]
            if top == 9:
                break

print(len(visible))
