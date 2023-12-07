#!/usr/bin/env python

import sys
area = [tuple(line.rstrip()) for line in sys.stdin]
steps = 10
size = len(area)
stats = {}

OPEN = '.'
TREE = '|'
YARD = '#'

dirs = []
for x in (-1, 0, 1):
    for y in (-1, 0, 1):
        if x == 0 and y == 0: continue
        dirs.append((x, y))

for _ in range(0, steps):
    next_area = [[' '] * size for _ in range(0, size)]
    stats = {OPEN: 0, TREE: 0, YARD: 0}
    
    for x in range(0, size):
        for y in range(0, size):
            around = {OPEN: 0, TREE: 0, YARD: 0}
            for item in dirs:
                pos = (x + item[0], y + item[1])
                if pos[0] < 0 or pos[0] >= size or pos[1] < 0 or pos[1] >= size:
                    continue
                around[area[pos[0]][pos[1]]] += 1

            if area[x][y] == OPEN:
                next_area[x][y] = TREE if around[TREE] >= 3 else OPEN
            elif area[x][y] == TREE:
                next_area[x][y] = YARD if around[YARD] >= 3 else TREE
            else:
                next_area[x][y] = YARD if around[TREE] >= 1 and around[YARD] >= 1 else OPEN

            stats[next_area[x][y]] += 1

    area = next_area

print(stats[TREE] * stats[YARD])
