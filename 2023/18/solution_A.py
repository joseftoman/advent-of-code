#!/usr/bin/env python

import sys

from skspatial.measurement import area_signed

RIGHT = 'R'
DOWN = 'D'
LEFT = 'L'
UP = 'U'

DIFFS = {
    RIGHT: (0, 1),
    DOWN: (1, 0),
    LEFT: (0, -1),
    UP: (-1, 0),
}

THICK = {
    (RIGHT, DOWN): ((0, 1), (1, 0)),
    (RIGHT, UP): ((0, 0), (1, 1)),
    (DOWN, RIGHT): ((0, 1), (1, 0)),
    (DOWN, LEFT): ((1, 1), (0, 0)),
    (LEFT, DOWN): ((1, 1), (0, 0)),
    (LEFT, UP): ((1, 0), (0, 1)),
    (UP, RIGHT): ((0, 0), (1, 1)),
    (UP, LEFT): ((1, 0), (0, 1)),
}


def main():
    wraps = [[], []]
    pos = (0, 0)
    prev = None
    first = None

    for line in sys.stdin:
        where, amount, _ = line.split()
        amount = int(amount)

        if first is None:
            first = where
            prev = where
        else:
            for index, wrap in enumerate(wraps):
                correction = THICK[(prev, where)][index]
                wrap.append((pos[0] + correction[0], pos[1] + correction[1]))
            prev = where

        dy, dx = DIFFS[where]
        pos = (pos[0] + dy * amount, pos[1] + dx * amount)

    for index, wrap in enumerate(wraps):
        correction = THICK[(prev, first)][index]
        wrap.append((pos[0] + correction[0], pos[1] + correction[1]))

    print(max(int(abs(area_signed(_))) for _ in wraps))


if __name__ == '__main__':
    main()
