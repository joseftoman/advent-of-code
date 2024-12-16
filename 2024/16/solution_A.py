#!/usr/bin/env python

import heapq
import sys

MOVES = {'N': (-1, 0), 'E': (0, 1), 'S': (1, 0), 'W': (0, -1)}
MOVE_TO_FACING = {val: key for key, val in MOVES.items()}
ROTATIONS = {
    'N': {'E': 1000, 'S': 2000, 'W': 1000},
    'E': {'S': 1000, 'W': 2000, 'N': 1000},
    'S': {'E': 1000, 'N': 2000, 'W': 1000},
    'W': {'N': 1000, 'E': 2000, 'S': 1000},
}


def main():
    maze = {}
    visited = set()
    heap = []
    target = None

    for y, line in enumerate(sys.stdin):
        for x, char in enumerate(line.strip()):
            maze[(y, x)] = char
            if char == 'S':
                heap = [(0, (y, x), 'E')]
            if char == 'E':
                target = (y, x)

    while heap:
        points, pos, facing = heapq.heappop(heap)
        if pos in visited:
            continue
        visited.add(pos)

        if pos == target:
            print(points)
            break

        for diff in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            y = pos[0] + diff[0]
            x = pos[1] + diff[1]
            if (y, x) in visited or maze[(y, x)] == '#':
                continue

            new_facing = MOVE_TO_FACING[diff]
            price = ROTATIONS[facing].get(new_facing, 0) + 1
            heapq.heappush(heap, (points + price, (y, x), new_facing))


if __name__ == '__main__':
    main()
