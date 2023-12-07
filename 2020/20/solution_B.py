#!/usr/bin/env python

import re
import sys

from grid import get_grid, rotate

monster = (
    (18, 0),
    (0, 1), (5, 1), (6, 1), (11, 1), (12, 1), (17, 1), (18, 1), (19, 1),
    (1, 2), (4, 2), (7, 2), (10, 2), (13, 2), (16, 2), 
)
monter_width = 20
monster_height = 3


def tile_content(x, y, grid):
    return [line[1:-1] for line in grid[(x, y)].dump()[1:-1]]


def join_tiles(grid, edges):
    image = []

    for y in range(edges['top'], edges['bottom'] - 1, -1):
        rows = tile_content(edges['left'], y, grid)

        for x in range(edges['left'] + 1, edges['right'] + 1):
            for i, chunk in enumerate(tile_content(x, y, grid)):
                rows[i] += chunk

        image.extend(rows)

    return image


def find_monsters(sea):
    hits = 0
    rough = set()

    for y, line in enumerate(sea):
        for x, ch in enumerate(line):
            if ch == '#':
                rough.add((x, y))
    
    for x in range(0, len(sea[0]) - monter_width + 1):
        for y in range(0, len(sea) - monster_height + 1):
            hit = True
            for point in monster:
                if sea[y + point[1]][x + point[0]] != '#':
                    hit = False
                    break
            if hit:
                hits += 1
                for point in monster:
                    rough.discard((x + point[0], y + point[1]))

    return len(rough) if hits else 0


def try_rotations(sea):
    for _ in range(0, 4):
        roughness = find_monsters(sea)
        if roughness:
            return roughness
        else:
            sea = rotate(sea)

    return 0

sea = join_tiles(*get_grid())
roughness = try_rotations(sea[:])
if roughness:
    print(roughness)
else:
    sea = [line[::-1] for line in sea]
    print(try_rotations(sea))
