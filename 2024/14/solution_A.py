#!/usr/bin/env python

import math
import sys

WIDTH = 101
HEIGHT = 103
STEPS = 100


def main():
    robots = []
    quadrants = [0] * 4
    ignore = [WIDTH // 2, HEIGHT // 2]

    for line in sys.stdin:
        robots.append([list(map(int, _[2:].split(','))) for _ in line.split()])

    for robot in robots:
        pos = [(robot[0][0] + STEPS * robot[1][0]) % WIDTH, (robot[0][1] + STEPS * robot[1][1]) % HEIGHT]
        if pos[0] == ignore[0] or pos[1] == ignore[1]:
            continue
        quadrants[int(pos[0] > ignore[0]) + int(pos[1] > ignore[1]) * 2] += 1

    print(math.prod(quadrants))


if __name__ == '__main__':
    main()
