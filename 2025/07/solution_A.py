#!/usr/bin/env python

import sys


def main():
    line = next(sys.stdin)
    beams = {line.index('S')}
    splits = 0

    for line in sys.stdin:
        next_beams = set()
        for beam in beams:
            if line[beam] == '^':
                next_beams.add(beam - 1)
                next_beams.add(beam + 1)
                splits += 1
            else:
                next_beams.add(beam)

        beams = next_beams

    print(splits)


if __name__ == '__main__':
    main()
