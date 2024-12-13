#!/usr/bin/env python

import sys


def read_tiles():
    tiles = {}

    for line in sys.stdin:
        left, right = line.split(',')
        single = (left[0], int(left[2:]))
        interval = [int(_) for _ in right.strip()[2:].split('..')]

        for coord in range(interval[0], interval[1] + 1):
            tile = (single[1], coord) if single[0] == 'x' else (coord, single[1])
            tiles[tile] = '#'

    return tiles


def render(tiles, min_y, max_y, pos = None):
    min_x = min(_[0] for _ in tiles)
    max_x = max(_[0] for _ in tiles)

    if pos is not None:
        min_x = pos[0] - 30
        max_x = pos[0] + 30
        min_y = pos[1] - 30
        max_y = pos[1] + 30

    print()
    for y in range(min_y, max_y + 1):
        print(''.join(tiles.get((x, y), ' ') for x in range(min_x, max_x + 1)))


def pour(tiles, max_y, stack):
    pos = stack.pop()
    if tiles[pos] == '~':
        # This is an outdated location inside a filled container
        return 0

    increment = 0

    # Spread downward
    while pos[1] + 1 <= max_y and tiles.get((pos[0], pos[1] + 1)) is None:
        pos = (pos[0], pos[1] + 1)
        tiles[pos] = '|'
        increment += 1

    if pos[1] == max_y or tiles.get((pos[0], pos[1] + 1)) == '|':
        # We hit a previously reached tile where water is overflowing a filled container.
        # Hitting a tile with steady water is possible and not a reason to stop.
        return increment

    # Spread left & right, optionally filling a container
    while True:
        left = (pos[0] - 1, pos[1])
        while tiles.get(left) != '#':
            if tiles.get(left) is None:
                increment += 1
            tiles[left] = '|'

            under = tiles.get((left[0], left[1] + 1))
            if under is None or under == '|':
                if under is None:
                    stack.append(left)
                break

            left = (left[0] - 1, left[1])

        right = (pos[0] + 1, pos[1])
        while tiles.get(right) != '#':
            if tiles.get(right) is None:
                increment += 1
            tiles[right] = '|'

            under = tiles.get((right[0], right[1] + 1))
            if under is None or under == '|':
                if under is None:
                    stack.append(right)
                break

            right = (right[0] + 1, right[1])

        if tiles.get(left) == '#' and tiles.get(right) == '#':
            for x in range(left[0] + 1, right[0]):
                tiles[(x, pos[1])] = '~'
            pos = (pos[0], pos[1] - 1)
            if tiles.get(pos) is None:
                tiles[pos] = '|'
                increment += 1
        else:
            break

    return increment


def main():
    tiles = read_tiles()
    min_y = min(_[1] for _ in tiles)
    max_y = max(_[1] for _ in tiles)

    tiles[(500, min_y)] = '|'
    stack = [(500, min_y)]
    total = 1

    while stack:
        total += pour(tiles, max_y, stack)

    print(total)


if __name__ == '__main__':
    main()
