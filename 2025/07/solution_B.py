#!/usr/bin/env python

from collections import defaultdict
import sys


def main():
    line = next(sys.stdin)
    beams = {line.index('S'): 1}

    for line in sys.stdin:
        next_beams = defaultdict(int)
        for beam, timelines in beams.items():
            if line[beam] == '^':
                next_beams[beam - 1] += timelines
                next_beams[beam + 1] += timelines
            else:
                next_beams[beam] += timelines

        beams = next_beams

    print(sum(beams.values()))


if __name__ == '__main__':
    main()
