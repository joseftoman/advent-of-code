#!/usr/bin/env python

import sys

MOVES = ((-1, 0), (0, -1), (0, 1), (1, 0))


def get_pos(square, move):
    return square[0] + move[0], square[1] + move[1]


def get_adjacent(pos):
    for move in MOVES:
        yield get_pos(pos, move)


def main():
    garden = {}
    total = 0

    for y, line in enumerate(_.strip() for _ in sys.stdin):
        for x, plant in enumerate(line):
            garden[(y, x)] = plant

    remaining = set(garden.keys())

    while remaining:
        plot = remaining.pop()
        plant = garden[plot]
        stack = [plot]
        area = 0
        perimeter = 0

        while stack:
            plot = stack.pop()
            area += 1

            for adjacent_plot in get_adjacent(plot):
                adjacent_plant = garden.get(adjacent_plot)

                if adjacent_plant != plant:
                    perimeter += 1
                elif adjacent_plot in remaining:
                    remaining.remove(adjacent_plot)
                    stack.append(adjacent_plot)

        total += area * perimeter

    print(total)


if __name__ == '__main__':
    main()
