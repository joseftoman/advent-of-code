#!/usr/bin/env python

import sys


def main():
    rows = [_.strip() for _ in sys.stdin]
    new_rows = []
    for row in rows:
        new_rows.append(row)
        if not '#' in row:
            new_rows.append(row)

    rows = new_rows
    extra = 0
    for x in range(len(rows[0])):
        if all(_[x + extra] == '.' for _ in rows):
            rows = [_[:x + extra] + '.' + _[x + extra:] for _ in rows]
            extra += 1

    galaxies = []
    for y, row in enumerate(rows):
        for x, char in enumerate(row):
            if char == '#':
                galaxies.append((y, x))

    total = 0

    for i in range(len(galaxies)):
        for j in range(i + 1, len(galaxies)):
            total += abs(galaxies[i][0] - galaxies[j][0]) + abs(galaxies[i][1] - galaxies[j][1])

    print(total)


if __name__ == '__main__':
    main()
