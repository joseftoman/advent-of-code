#!/usr/bin/env python

import re
import sys


def rotate(lines, direction=1):
    rotated = []

    for i in range(0, len(lines)):
        col = i if direction == 1 else len(lines) - i - 1
        r_line = ''.join([line[col] for line in lines])
        if direction == 1:
            r_line = r_line[::-1]
        rotated.append(r_line)

    return rotated


class Tile():
    regex_title = re.compile('Tile (\d+):')

    def __init__(self, stream):
        line = stream.readline()
        if not line:
            raise Exception()
        m = self.regex_title.match(line)
        self.id = int(m.group(1))

        self._raw = []
        for line in stream:
            line = line.strip()
            if not line:
                break
            self._raw.append(line)

        self.reset()

    def reset(self):
        self._flipped = False
        self._rotation = 0

        self.top = self._raw[0]
        self.bottom = self._raw[-1]
        self.left = ''.join([row[0] for row in self._raw])
        self.right = ''.join([row[-1] for row in self._raw])


    def flip(self):
        tmp = self.left
        self.left = self.right
        self.right = tmp
        self.top = self.top[::-1]
        self.bottom = self.bottom[::-1]
        self._flipped = not self._flipped

    def rotate(self):
        tmp = self.top
        self.top = self.left[::-1]
        self.left = self.bottom
        self.bottom = self.right[::-1]
        self.right = tmp
        self._rotation = (self._rotation + 1) % 4

    def dump(self):
        lines = self._raw
        if self._flipped:
            lines = [line[::-1] for line in lines]

        if not self._rotation:
            return lines
        if self._rotation == 1:
            return rotate(lines)
        if self._rotation == 2:
            return [line[::-1] for line in lines[::-1]]

        return rotate(lines, -1)


def is_match(tile, constraints):
    if constraints['top'] and tile.top != constraints['top']:
        return False
    if constraints['bottom'] and tile.bottom != constraints['bottom']:
        return False
    if constraints['left'] and tile.left != constraints['left']:
        return False
    if constraints['right'] and tile.right != constraints['right']:
        return False
    
    return True


def find_rotation(tile, constraints):
    if is_match(tile, constraints):
        return True

    for _ in range(0, 3):
        tile.rotate()
        if is_match(tile, constraints):
            return True

    return False


def find_orientation(tile, constraints):
    tile.reset()
    if find_rotation(tile, constraints):
        return True

    tile.reset()
    tile.flip()
    return find_rotation(tile, constraints)


def find_match(pos, grid, loose):
    x, y = pos
    match = None

    constraints = {
        'top': grid[(x, y + 1)].bottom if (x, y + 1) in grid else None,
        'bottom': grid[(x, y - 1)].top if (x, y - 1) in grid else None,
        'left': grid[(x - 1, y)].right if (x - 1, y) in grid else None,
        'right': grid[(x + 1, y)].left if (x + 1, y) in grid else None,
    }
    #print(f'FIND: {x}, {y},', constraints)

    for tile in loose.values():
        if find_orientation(tile, constraints):
            match = tile
            break

    if not match:
        return False

    grid[pos] = match
    del loose[match.id]
    #print(f'MATCH: {x}, {y} - tile', tile.id, tile._flipped, tile._rotation, f'T: {tile.top} B: {tile.bottom} L: {tile.left} R: {tile.right}')
    return True


def populate(pos, grid, loose, edges, stack):
    x, y = pos
    #print(f'POPULATE: {x}, {y}')

    if (edges['top'] is None or edges['top'] > y) and (x, y + 1) not in grid:
        ok = find_match((x, y + 1), grid, loose)
        if ok:
            stack.append((x, y + 1))
        elif edges['top'] is None:
            edges['top'] = y
            #print('TOP EDGE =', y)

    if (edges['right'] is None or edges['right'] > x) and (x + 1, y) not in grid:
        ok = find_match((x + 1, y), grid, loose)
        if ok:
            stack.append((x + 1, y))
        elif edges['right'] is None:
            edges['right'] = x
            #print('RIGHT EDGE =', x)

    if (edges['bottom'] is None or edges['bottom'] < y) and (x, y - 1) not in grid:
        ok = find_match((x, y - 1), grid, loose)
        if ok:
            stack.append((x, y - 1))
        elif edges['bottom'] is None:
            edges['bottom'] = y
            #print('BOTTOM EDGE =', y)

    if (edges['left'] is None or edges['left'] < x) and (x - 1, y) not in grid:
        ok = find_match((x - 1, y), grid, loose)
        if ok:
            stack.append((x - 1, y))
        elif edges['left'] is None:
            edges['left'] = x
            #print('LEFT EDGE =', x)


def get_grid():
    loose = {}
    grid = {}
    edges = {'left': None, 'right': None, 'top': None, 'bottom': None}
    stack = []

    try:
        while True:
            tile = Tile(sys.stdin)
            loose[tile.id] = tile
    except Exception:
        pass

    _, tile = loose.popitem()
    grid[(0, 0)] = tile
    stack = [(0, 0)]
    #print('MATCH: 0, 0 - tile', tile.id)

    while stack:
        populate(stack.pop(), grid, loose, edges, stack)

    return grid, edges
