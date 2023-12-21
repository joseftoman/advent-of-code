#!/usr/bin/env python

import sys


def main():
    garden = {}
    plots = []
    step = 0
    max_y = 0
    max_x = 0
    target = 64

    for y, line in enumerate(sys.stdin):
        max_y = y
        max_x = len(line.strip()) - 1

        for x, char in enumerate(line.strip()):
            if char == 'S':
                plots.append((y, x))
                char = '.'
            garden[(y, x)] = char

    while step < target:
        step += 1
        next_plots = set()

        for y, x in plots:
            for diff in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                ny = y + diff[0]
                nx = x + diff[1]
                if nx < 0 or ny < 0 or nx > max_x or ny > max_y or garden[(ny, nx)] == '#':
                    continue

                next_plots.add((ny, nx))

        plots = list(next_plots)

    print(len(plots))


if __name__ == '__main__':
    main()
