#!/usr/bin/env python

from collections import defaultdict
from functools import lru_cache
import heapq
import math
import sys

start = None
target = None
max_row = 0
max_col = 0
modulo = 0
blizzards = defaultdict(set)

diffs = {'<': (0, -1), '>': (0, 1), '^': (-1, 0), 'v': (1, 0)}
options = {(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)}


def distance(a, b):
    return sum(abs(a[_] - b[_]) for _ in range(len(a)))


def apply(pos, diff):
    if (pos == (0, 0) and diff == (-1, 0)) or (pos == start and diff == (0, 0)):
        return start

    return ((pos[0] + diff[0]) % (max_row + 1), (pos[1] + diff[1]) % (max_col + 1))


def move(pos, direction, steps = 1):
    return apply(pos, tuple(steps * _ for _ in diffs[direction]))


def available_moves(pos, steps):
    if pos == start:
        adjacent = {start, (start[0] + 1, start[1])}
    elif pos == target:
        adjacent = {target, (target[0] - 1, target[1])}
    else:
        adjacent = set()
        for option in options:
            if pos[0] == 0 and option[0] == -1:
                continue
            if pos[0] == max_row and option[0] == 1:
                continue
            if pos[1] == 0 and option[1] == -1:
                continue
            if pos[1] == max_col and option[1] == 1:
                continue
            adjacent.add(apply(pos, option))
        
        if pos == (start[0] + 1, start[1]):
            adjacent.add(start)
        if pos == (target[0] - 1, target[1]):
            adjacent.add(target)

    blizzards = forecast_blizzards(steps)
    return [_ for _ in adjacent if not blizzards[_]]


@lru_cache(maxsize=10)
def forecast_blizzards(steps):
    forecast = defaultdict(set)

    for pos, directions in blizzards.items():
        for direction in directions:
            forecast[move(pos, direction, steps)].add(direction)

    return forecast


def find_shortest(start_pos, target_pos, steps):
    heap = [(steps, distance(start_pos, target_pos), start_pos)]
    visited = set()

    while heap:
        steps, dist, pos = heapq.heappop(heap)
        if (steps % modulo, pos) in visited:
            continue
        visited.add((steps % modulo, pos))

        if pos == target_pos:
            return steps
            break

        current_blizzards = forecast_blizzards(steps)
        for next_pos in available_moves(pos, steps + 1):
            if next_pos == target_pos:
                return steps + 1
            if ((steps + 1) % modulo, next_pos) in visited:
                continue
            heapq.heappush(heap, (steps + 1, distance(next_pos, target_pos), next_pos))


def main():
    global start, target, max_row, max_col, modulo, blizzards

    for row, line in enumerate(sys.stdin, -1):
        line = line.strip()
        if row == -1:
            start = (row, line.index('.') - 1)
            max_col = len(line) - 3
            continue
        if row >= 0 and line[:2] == '##':
            target = (row, line.index('.') - 1)
            max_row = row - 1
            break

        for col, char in enumerate(line[1:-1]):
            if char != '.':
                blizzards[(row, col)].add(char)

    modulo = (max_row + 1) * (max_col + 1) // math.gcd(max_row + 1, max_col + 1)

    there = find_shortest(start, target, 0)
    back = find_shortest(target, start, there)
    there_again = find_shortest(start, target, back)
    print(there_again)


if __name__ == '__main__':
    main()
