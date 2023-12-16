#!/usr/bin/env python

import sys

RIGHT = 0
DOWN = 1
LEFT = 2
UP = 3

DIFFS = {
    RIGHT: (0, 1),
    DOWN: (1, 0),
    LEFT: (0, -1),
    UP: (-1, 0),
}

BENDS = {
    '/': {RIGHT: UP, DOWN: LEFT, LEFT: DOWN, UP: RIGHT},
    '\\': {RIGHT: DOWN, DOWN: RIGHT, LEFT: UP, UP: LEFT},
}


def main():
    energized = {(0, 0)}
    beams = [((0, 0), RIGHT)]
    walked = set(beams)
    grid = [_.strip() for _ in sys.stdin]
    max_y = len(grid)
    max_x = len(grid[0])

    while beams:
        next_beams = set()

        for beam in beams:
            y, x = beam[0]
            direction = beam[1]
            char = grid[y][x]
            out = []

            if char == '.' or (char == '-' and direction in {RIGHT, LEFT}) or (char == '|' and direction in {DOWN, UP}):
                out.append(direction)
            elif char == '|':
                out.extend([DOWN, UP])
            elif char == '-':
                out.extend([RIGHT, LEFT])
            else:
                out.append(BENDS[char][direction])

            for direction in out:
                dy, dx = DIFFS[direction]
                ny = y + dy
                nx = x + dx
                if 0 <= ny < max_y and 0 <= nx < max_x:
                    next_beam = ((ny, nx), direction)
                    if next_beam not in walked:
                        next_beams.add(next_beam)
                        walked.add(next_beam)

        for pos, _ in next_beams:
            energized.add(pos)
        beams = list(next_beams)

    print(len(energized))


if __name__ == '__main__':
    main()
