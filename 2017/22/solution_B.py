#!/usr/bin/python3

import sys

bursts = 1e7

input_grid = [ l.rstrip() for l in sys.stdin ]
x = -(len(input_grid[0]) // 2)
y = len(input_grid) // 2

grid = {}
for line in input_grid:
    xl = x
    for char in line:
        if xl not in grid:
            grid[xl] = {}
        grid[xl][y] = 2 if char == '#' else 0
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

    if grid[x][y] == 0:
        d = (d - 1) % 4
    elif grid[x][y] == 1:
        infection += 1
    elif grid[x][y] == 2:
        d = (d + 1) % 4
    elif grid[x][y] == 3:
        d = (d + 2) % 4

    grid[x][y] = (grid[x][y] + 1) % 4
    x += dirs[d][0]
    y += dirs[d][1]

print(infection)
