#!/usr/bin/env python

from collections import defaultdict
import sys

MOVES = ((-1, 0), (0, -1), (0, 1), (1, 0))


def get_pos(square, move):
    return square[0] + move[0], square[1] + move[1]


def get_adjacent(pos):
    for move in MOVES:
        yield get_pos(pos, move)


def get_segments_count(borders):
    segments = 1
    borders.sort()

    prev = borders[0]

    for item in borders[1:]:
        if item > prev + 1:
            segments += 1
        prev = item

    return segments


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
        horizontal = defaultdict(list)
        vertical = defaultdict(list)

        while stack:
            plot = stack.pop()
            area += 1

            for adjacent_plot in get_adjacent(plot):
                adjacent_plant = garden.get(adjacent_plot)

                if adjacent_plant != plant:
                    if plot[0] != adjacent_plot[0]:
                        up = adjacent_plot[0] < plot[0]
                        horizontal[plot[0] + (0 if up else 1)].append((plot[1] + 1) * (1 if up else -1))
                    else:
                        left = adjacent_plot[1] < plot[1]
                        vertical[plot[1] + (0 if left else 1)].append((plot[0] + 1) * (1 if left else -1))
                elif adjacent_plot in remaining:
                    remaining.remove(adjacent_plot)
                    stack.append(adjacent_plot)

        perimeter = sum(get_segments_count(borders) for borders in [*horizontal.values(), *vertical.values()])
        total += area * perimeter

    print(total)


if __name__ == '__main__':
    main()
