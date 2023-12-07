#!/usr/bin/env python

import sys
import heapq

NEITHER = 0
TORCH = 1
GEAR = 2

ROCKY = 0
WET = 1
NARROW = 2

def explore_cave(cave, dist, target, depth):
    for x, y in [(x, dist - x) for x in range(0, dist + 1)]:
        if (x == 0 and y == 0) or [x, y] == target:
            geo = 0
        elif x == 0:
            geo = y * 48271
        elif y == 0:
            geo = x * 16807
        else:
            geo = cave[(x-1, y)] * cave[(x, y-1)]

        erosion = (geo + depth) % 20183
        cave[(x, y)] = erosion

def main():
    depth = int(sys.stdin.readline()[7:])
    target = [int(x) for x in sys.stdin.readline()[8:].split(',')]

    moves = ((-1, 0), (1, 0), (0, -1), (0, 1))
    allowed = {
        ROCKY: set([TORCH, GEAR]),
        WET: set([NEITHER, GEAR]),
        NARROW: set([NEITHER, TORCH])
    }

    cave = {}
    best = {}
    heap = []
    heapq.heappush(heap, (0, (0, 0, TORCH)))

    max_dist = sum(target) + 10
    for dist in range(0, max_dist + 1):
        explore_cave(cave, dist, target, depth)

    while heap:
        item = heapq.heappop(heap)
        if item[1] in best:
            continue
        best[item[1]] = item[0]

        if item[1] == (*target, TORCH):
            print(item[0])
            break

        x, y = item[1][:2]

        for equip in allowed[cave[(x, y)] % 3]:
            if equip != item[1][2] and (x, y, equip) not in best:
                heapq.heappush(heap, (item[0] + 7, (x, y, equip)))

        for move in moves:
            next_x = x + move[0]
            next_y = y + move[1]
            if next_x < 0 or next_y < 0:
                continue

            if next_x + next_y > max_dist:
                max_dist = next_x + next_y
                explore_cave(cave, max_dist, target, depth)

            if item[1][2] not in allowed[cave[(next_x, next_y)] % 3]:
                continue
            if (next_x, next_y, item[1][2]) in best:
                continue

            heapq.heappush(heap, (item[0] + 1, (next_x, next_y, item[1][2])))

if __name__ == '__main__': main()
