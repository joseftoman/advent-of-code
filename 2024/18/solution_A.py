#!/usr/bin/env python

import heapq
import sys

MAX_X = 70
MAX_Y = 70
NUM_OF_BYTES = 1024


def main():
    fell_bytes = set()
    visited = set()
    heap = [(0, (0, 0))]
    target = (MAX_X, MAX_Y)

    for _ in range(NUM_OF_BYTES):
        x, y = [int(_) for _ in next(sys.stdin).split(',')]
        fell_bytes.add((x, y))

    while heap:
        steps, pos = heapq.heappop(heap)
        if pos in visited:
            continue
        visited.add(pos)

        if pos == target:
            print(steps)
            break

        for diff in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            x = pos[0] + diff[0]
            y = pos[1] + diff[1]
            if x < 0 or y < 0 or x > MAX_X or y > MAX_Y or (x, y) in visited or (x, y) in fell_bytes:
                continue

            heapq.heappush(heap, (steps + 1, (x, y)))


if __name__ == '__main__':
    main()
