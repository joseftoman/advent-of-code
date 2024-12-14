#!/usr/bin/env python

from collections import defaultdict
import sys

WIDTH = 101
HEIGHT = 103


def main():
    robots = []
    step = 0

    for line in sys.stdin:
        robots.append([list(map(int, _[2:].split(','))) for _ in line.split()])

    while True:
        step += 1

        for robot in robots:
            robot[0] = [(robot[0][0] + robot[1][0]) % WIDTH, (robot[0][1] + robot[1][1]) % HEIGHT]

        groups = {}
        sizes = defaultdict(int)
        next_group = 0

        # In a general case, merging of groups would have to be considered.
        # But because we are expecting a tree-shaped group, iterating the tiles
        # top-to-bottom should work just fine.

        for tile in sorted((tuple(_[0]) for _ in robots), key=lambda x: (x[1], x[0])):
            hit = False

            for diff in [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]:
                near = (tile[0] + diff[0], tile[1] + diff[1])
                if near in groups:
                    groups[tile] = groups[near]
                    sizes[groups[near]] += 1
                    hit = True
                    break

            if not hit:
                groups[tile] = next_group
                sizes[next_group] += 1
                next_group += 1

        if max(sizes.values()) > len(robots) // 5:
            print(step)

            # Render the Christmas tree:
            # tiles = set(tuple(_[0]) for _ in robots)
            # for y in range(HEIGHT):
            #     print(''.join('+' if (x, y) in tiles else ' ' for x in range(WIDTH)))

            break


if __name__ == '__main__':
    main()
