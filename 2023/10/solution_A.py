#!/usr/bin/env python

import math
import sys

UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)

moves = {
    '|': {UP: UP, DOWN: DOWN},
    '-': {LEFT: LEFT, RIGHT: RIGHT},
    'L': {DOWN: RIGHT, LEFT: UP},
    'J': {DOWN: LEFT, RIGHT: UP},
    '7': {RIGHT: DOWN, UP: LEFT},
    'F': {LEFT: DOWN, UP: RIGHT},
}


def check_next_step(area, pos, max_y, max_x, step):
    ny, nx = pos[0] + step[0], pos[1] + step[1]
    if ny < 0 or ny == max_y:
        return None
    if nx < 0 or nx == max_x:
        return None

    char = area[ny][nx]
    next_step = moves.get(char, {}).get(step)
    if next_step is None and char != 'S':
        return None
    return (ny, nx), next_step


def initial_steps(area, pos, max_y, max_x):
    for step in [UP, DOWN, LEFT, RIGHT]:
        next_step = check_next_step(area, pos, max_y, max_x, step)
        if next_step is not None:
            yield pos, step


def main():
    area = [list(_.strip()) for _ in sys.stdin]
    for y, line in enumerate(area):
        if y == 0:
            max_x = len(line)
        for x, char in enumerate(line):
            if char == 'S':
                start = y, x
    max_y = len(area)

    tails = [[_] for _ in initial_steps(area, start, max_y, max_x)]

    while True:
        new_tails = []
        for tail in tails:
            pos, step = tail[-1]
            next_step = check_next_step(area, pos, max_y, max_x, step)
            if next_step is not None:
                if next_step[1] is None:
                    print(math.floor(len(tail) / 2))
                    return
                tail.append(next_step)
                new_tails.append(tail)

if __name__ == '__main__':
    main()
