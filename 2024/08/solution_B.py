#!/usr/bin/env python

from collections import defaultdict
from itertools import combinations
import sys


def main():
    antennas = defaultdict(list)
    antinodes = set()

    for y, line in enumerate(_.strip() for _ in sys.stdin):
        size_x = len(line)
        size_y = y + 1
        for x, char in enumerate(line):
            if char != '.':
                antennas[char].append((y, x))

    for group in antennas.values():
        group.sort(key=lambda item: item[0])

        for upper, lower in combinations(group, 2):
            antinodes.add(upper)
            antinodes.add(lower)

            diff_y = lower[0] - upper[0]
            diff_x = lower[1] - upper[1]

            # In most cases, this grossly overshoots the map borders, but it's simple and good enough.
            for resonation in range(1, max(size_y, size_x) // min(abs(diff_y), abs(diff_x))):
                for antinode in [
                    (upper[0] - diff_y * resonation, upper[1] - diff_x * resonation),
                    (lower[0] + diff_y * resonation, lower[1] + diff_x * resonation),
                ]:
                    if 0 <= antinode[0] < size_y and 0 <= antinode[1] < size_x:
                        antinodes.add(antinode)

    print(len(antinodes))


if __name__ == '__main__':
    main()
