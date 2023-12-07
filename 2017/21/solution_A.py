#!/usr/bin/python3

import sys

rules_2 = {}
rules_3 = {}
grid = [ '.#.', '..#', '###' ]

def rows_to_vector(rows):
    s = ''.join(rows)
    return ''.join([ s[x] for x in (0, 1, 2, 5, 8, 7, 6, 3, 4) ])

def transform_2(r1, r2):
    s = r1 + r2
    c = s.count('#')
    if c == 2:
        if s == '##..' or s == '.#.#' or s == '..##' or s == '#.#.':
            c = 22
        else:
            c = 21

    return rules_2[c]

def transform_3(r1, r2, r3):
    vector = rows_to_vector(r1 + r2 + r3)
    tmp = vector
    for i in range(0, 4):
        if tmp in rules_3:
            return rules_3[tmp]
        if i < 3:
            tmp = tmp[2:-1] + tmp[:2] + tmp[-1]
    
    tmp = vector[0] + vector[-2:0:-1] + vector[-1]

    for i in range(0, 4):
        if tmp in rules_3:
            return rules_3[tmp]
        if i < 3:
            tmp = tmp[2:-1] + tmp[:2] + tmp[-1]

for line in [ l.rstrip() for l in sys.stdin ]:
    (left, right) = line.split(' => ')
    right = right.split('/')
    if len(left) == 5:
        c = left.count('#')
        if c == 2:
            if left == '##/..':
                c = 22
            else:
                c = 21
        rules_2[c] = right
    else:
        vector = rows_to_vector(left.split('/'))
        rules_3[vector] = right

for step in range(0, 5):
    if len(grid) % 2 == 0:
        mode = 2
        new_grid = [''] * (len(grid) // 2 * 3)
    else:
        mode = 3
        new_grid = [''] * (len(grid) // 3 * 4)

    for i in range(0, len(grid), mode):
        for j in range(0, len(grid), mode):
            if mode == 2:
                subgrid = transform_2(grid[i][j:j+mode], grid[i+1][j:j+mode])
            else:
                subgrid = transform_3(grid[i][j:j+mode], grid[i+1][j:j+mode], grid[i+2][j:j+mode])

            for k in range(0, mode + 1):
                new_grid[(i // mode) * (mode + 1) + k] += subgrid[k]

    grid = new_grid

count = 0
for line in grid:
    count += line.count('#')
print(count)
