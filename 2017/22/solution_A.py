#!/usr/bin/python3

import sys

bursts = 10000

input_grid = [ l.rstrip() for l in sys.stdin ]
x = -(len(input_grid[0]) // 2)
y = len(input_grid) // 2

grid = {}
for line in input_grid:
    xl = x
    for char in line:
        if xl not in grid:
            grid[xl] = {}
        grid[xl][y] = 1 if char == '#' else 0
        xl += 1
    y -= 1

x = 0
y = 0
d = 0 # Direction
dirs = ((0, 1), (1, 0), (0, -1), (-1, 0)) # up, right, down, left
infection = 0

while bursts:
    bursts -= 1
    if x not in grid:
        grid[x] = {}
    if y not in grid[x]:
        grid[x][y] = 0

    if grid[x][y]:
        d = (d + 1) % 4
    else:
        d = (d - 1) % 4
        infection += 1

    grid[x][y] = (grid[x][y] + 1) % 2
    x += dirs[d][0]
    y += dirs[d][1]

print(infection)
