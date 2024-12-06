#!/usr/bin/env python

from collections import defaultdict
import sys

ROTATE = {(-1, 0): (0, 1), (0, 1): (1, 0), (1, 0): (0, -1), (0, -1): (-1, 0)}


def main():
    lab = {}
    for y, line in enumerate(_.strip() for _ in sys.stdin):
        size_x = len(line)
        size_y = y + 1
        for x, char in enumerate(line):
            lab[(y, x)] = char
            if char == '^':
                pos = (y, x)

    heading = (-1, 0)
    walked = set()
    walked.add(pos)

    while True:
        next_pos = pos[0] + heading[0], pos[1] + heading[1]
        if not (0 <= next_pos[0] < size_y and 0 <= next_pos[1] < size_x):
            break
        while lab[next_pos] == '#':
            heading = ROTATE[heading]
            next_pos = pos[0] + heading[0], pos[1] + heading[1]

        pos = next_pos
        walked.add(pos)

    print(len(walked))


if __name__ == '__main__':
    main()
