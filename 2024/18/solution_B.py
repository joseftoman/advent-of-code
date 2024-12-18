#!/usr/bin/env python

import heapq
import math
import sys

MAX_X = 70
MAX_Y = 70
INITIAL_FILL_RATIO = 0.25


def run(fell_bytes):
    visited = set()
    heap = [(0, (0, 0))]
    target = (MAX_X, MAX_Y)

    while heap:
        steps, pos = heapq.heappop(heap)
        if pos in visited:
            continue
        visited.add(pos)

        if pos == target:
            return True

        for diff in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            x = pos[0] + diff[0]
            y = pos[1] + diff[1]
            if x < 0 or y < 0 or x > MAX_X or y > MAX_Y or (x, y) in visited or (x, y) in fell_bytes:
                continue

            heapq.heappush(heap, (steps + 1, (x, y)))

    return False


def main():
    falling_bytes = []

    for line in sys.stdin:
        x, y = [int(_) for _ in line.split(',')]
        falling_bytes.append((x, y))

    navigable = 0
    blocked = len(falling_bytes)
    next_guess = int((MAX_X + 1) * (MAX_Y + 1) * INITIAL_FILL_RATIO)
    
    while blocked - navigable > 1:
        can_walk = run(set(falling_bytes[:next_guess]))

        if can_walk:
            navigable = next_guess
        else:
            blocked = next_guess
        next_guess = navigable + (blocked - navigable) // 2
        
    print(','.join(str(_) for _ in falling_bytes[blocked - 1]))


if __name__ == '__main__':
    main()
