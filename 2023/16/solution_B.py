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


def run_beams(grid, entry):
    energized = {entry[0]}
    beams = [entry]
    walked = set(beams)
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

    return len(energized)


def main():
    grid = [_.strip() for _ in sys.stdin]
    best = 0

    for y in range(len(grid)):
        score = max([run_beams(grid, ((y, 0), RIGHT)), run_beams(grid, ((y, len(grid[0]) - 1), LEFT))])
        if score > best:
            best = score

    for x in range(len(grid[0])):
        score = max([run_beams(grid, ((0, x), DOWN)), run_beams(grid, ((len(grid) - 1, x), UP))])
        if score > best:
            best = score

    print(best)


if __name__ == '__main__':
    main()
