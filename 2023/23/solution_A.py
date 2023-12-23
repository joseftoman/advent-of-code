#!/usr/bin/env python

from collections import defaultdict
import sys


def walk(grid, pos, visited, end):
    if pos == end:
        return len(visited)

    slopes = {'>': (0, 1), '<': (0, -1), '^': (-1, 0), 'v': (1, 0)}

    while True:
        diffs = [slopes[grid[pos]]] if grid[pos] in slopes else list(slopes.values())
        available = []
        for diff in diffs:
            new_pos = (pos[0] + diff[0], pos[1] + diff[1])
            if grid[new_pos] == '#' or new_pos in visited:
                continue
            available.append(new_pos)

        if len(available) == 0:
            return 0
        if len(available) > 1:
            break

        new_pos = available[0]
        if new_pos == end:
            return len(visited) + 1
        visited.add(pos)
        pos = new_pos

    best = 0
    for new_pos in available:
        dist = walk(grid, new_pos, visited | {pos}, end)
        if dist > best:
            best = dist

    return best


def main():
    grid = {}

    for y, line in enumerate(sys.stdin):
        end = (y, len(line.strip()) - 2)
        for x, char in enumerate(line.strip()):
            grid[(y, x)] = char

    visited = {(0, 1)}
    print(walk(grid, (1, 1), visited, end))


if __name__ == '__main__':
    main()
