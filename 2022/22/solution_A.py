#!/usr/bin/env python

import re
import sys

walls = set()
row_limits = {}
col_limits = {}

for row, line in enumerate(sys.stdin, 1):
    if not line.strip():
        break

    line = line.rstrip()
    for col, char in enumerate(line, 1):
        if char == ' ':
            continue
        if char == '#':
            walls.add((row, col))
        if row not in row_limits:
            row_limits[row] = [col, len(line)]
        if col not in col_limits:
            col_limits[col] = [row, row]
        if row > col_limits[col][1]:
            col_limits[col][1] = row

moves = sys.stdin.readline().strip()

row, col = 1, row_limits[1][0]
facing = 0

for move in re.findall(r'(\d+|[RL])', moves):
    if move in {'R', 'L'}:
        facing = (facing + (1 if move == 'R' else -1)) % 4
        continue

    for _ in range(int(move)):
        next_row, next_col = row, col

        if facing == 0:
            next_col += 1
            if next_col > row_limits[row][1]:
                next_col = row_limits[row][0]
        elif facing == 2:
            next_col -= 1
            if next_col < row_limits[row][0]:
                next_col = row_limits[row][1]
        elif facing == 1:
            next_row += 1
            if next_row > col_limits[col][1]:
                next_row = col_limits[col][0]
        elif facing == 3:
            next_row -= 1
            if next_row < col_limits[col][0]:
                next_row = col_limits[col][1]

        if (next_row, next_col) in walls:
            break
        row, col = next_row, next_col

print(1000 * row + 4 * col + facing)
