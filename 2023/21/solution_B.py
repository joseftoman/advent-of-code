#!/usr/bin/env python

import sys
import numpy as np


def main():
    garden = {}
    plots = []
    step = 0
    mod_y = 0
    mod_x = 0
    target = 26501365
    layers = []

    for y, line in enumerate(sys.stdin):
        mod_y = y + 1
        mod_x = len(line.strip())

        for x, char in enumerate(line.strip()):
            if char == 'S':
                plots.append((y, x))
                char = '.'
            garden[(y, x)] = char

    if mod_y != mod_x or mod_y != 131:
        print('Error: a specific input is required')
        return

    required_steps = [mod_y * _ + mod_y // 2 for _ in [0, 1, 2]]

    while step < required_steps[-1]:
        step += 1
        next_plots = set()

        for y, x in plots:
            for diff in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                ny = y + diff[0]
                nx = x + diff[1]
                if garden[(ny % mod_y, nx % mod_x)] == '#':
                    continue

                next_plots.add((ny, nx))

        plots = list(next_plots)
        if step in required_steps:
            layers.append(len(plots))

    grid_repeats = target // mod_y

    # Constructing the final shape from its parts
    # print(
    #     layers[0]
    #     + grid_repeats * (layers[1] - layers[0])
    #     + (grid_repeats * (grid_repeats - 1) // 2) * (layers[2] - 2 * layers[1] + layers[0])
    # )

    # Using the quadratic rate of increase
    poly = np.linalg.solve([[0, 0, 1], [1, 1, 1], [4, 2, 1]], layers).astype(int)
    print(poly[0] * (grid_repeats ** 2) + poly[1] * grid_repeats + poly[2])



if __name__ == '__main__':
    main()
