#!/usr/bin/env python

from collections import defaultdict
import sys

ROTATE = {(-1, 0): (0, 1), (0, 1): (1, 0), (1, 0): (0, -1), (0, -1): (-1, 0)}


def simple_walk(lab, size_x, size_y, pos, heading):
    walked = set()

    while True:
        next_pos = pos[0] + heading[0], pos[1] + heading[1]
        if not (0 <= next_pos[0] < size_y and 0 <= next_pos[1] < size_x):
            break
        while lab[next_pos] == '#':
            heading = ROTATE[heading]
            next_pos = pos[0] + heading[0], pos[1] + heading[1]

        pos = next_pos
        walked.add(pos)

    return walked


def detect_cycle(lab, size_x, size_y, pos, heading):
    walked = set()

    while True:
        next_pos = pos[0] + heading[0], pos[1] + heading[1]
        if not (0 <= next_pos[0] < size_y and 0 <= next_pos[1] < size_x):
            return 0
        while lab[next_pos] == '#':
            heading = ROTATE[heading]
            next_pos = pos[0] + heading[0], pos[1] + heading[1]

        pos = next_pos
        if (pos, heading) in walked:
            return 1
        walked.add((pos, heading))


def main():
    heading = (-1, 0)
    lab = {}

    for y, line in enumerate(_.strip() for _ in sys.stdin):
        size_x = len(line)
        size_y = y + 1
        for x, char in enumerate(line):
            lab[(y, x)] = char
            if char == '^':
                start_pos = (y, x)

    to_try = simple_walk(lab, size_x, size_y, start_pos, heading)
    total = 0

    for obstacle in to_try:
        lab[obstacle] = '#'
        total += detect_cycle(lab, size_x, size_y, start_pos, heading)
        lab[obstacle] = '.'

    print(total)


if __name__ == '__main__':
    main()
