#!/usr/bin/env python

from collections import deque
import sys


def read_bricks():
    output = []

    for line in sys.stdin:
        start, end = line.strip().split('~')
        start = [int(_) for _ in start.split(',')]
        end = [int(_) for _ in end.split(',')]

        x1, x2 = sorted([start[0], end[0]])
        y1, y2 = sorted([start[1], end[1]])
        z1, z2 = sorted([start[2], end[2]])

        output.append(((x1, y1, z1), (x2, y2, z2)))

    return output


def main():
    bricks = []
    cubes = {}
    heights = {}

    for index, brick in enumerate(sorted(read_bricks(), key=lambda brick: brick[0][2])):
        drop = brick[0][2] - max(heights.get(x, {}).get(y, 0) for x in range(brick[0][0], brick[1][0] + 1) for y in range(brick[0][1], brick[1][1] + 1)) - 1

        # tuple of 2 sets:
        # - set no.1: bricks directly below (supporting) the given brick
        # - set no.2: bricks directly above (supported by) the given brick
        bricks.append((set(), set()))

        for x in range(brick[0][0], brick[1][0] + 1):
            for y in range(brick[0][1], brick[1][1] + 1):
                if x not in heights:
                    heights[x] = {}
                heights[x][y] = brick[1][2] - drop

                for z in range(brick[0][2] - drop, brick[1][2] + 1 - drop):
                    if x not in cubes:
                        cubes[x] = {}
                    if y not in cubes[x]:
                        cubes[x][y] = {}
                    cubes[x][y][z] = index

                below = cubes[x][y].get(brick[0][2] - drop - 1)
                if below is not None:
                    bricks[below][1].add(index)
                    bricks[index][0].add(below)

    total = 0
    for index, brick in enumerate(bricks):
        dropped = set()
        to_drop = deque([index])

        while to_drop:
            removed = to_drop.popleft()
            dropped.add(removed)
            for above in bricks[removed][1]:
                if len(bricks[above][0] - dropped) == 0:
                    to_drop.append(above)

        total += len(dropped) - 1

    print(total)


if __name__ == '__main__':
    main()
