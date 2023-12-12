#!/usr/bin/env python

import sys

expand = 1000000


def main():
    row_heights = []
    column_widths = []
    rows = [_.strip() for _ in sys.stdin]
    for row in rows:
        row_heights.append(1 if '#' in row else expand)

    for x in range(len(rows[0])):
        column_widths.append(expand if all(_[x] == '.' for _ in rows) else 1)

    galaxies = []
    for y, row in enumerate(rows):
        for x, char in enumerate(row):
            if char == '#':
                galaxies.append((y, x))

    total = 0

    for i in range(len(galaxies)):
        for j in range(i + 1, len(galaxies)):
            y1, y2 = min(galaxies[i][0], galaxies[j][0]), max(galaxies[i][0], galaxies[j][0])
            diff_y = sum(row_heights[_] for _ in range(y1 + 1, y2 + 1))
            x1, x2 = min(galaxies[i][1], galaxies[j][1]), max(galaxies[i][1], galaxies[j][1])
            diff_x = sum(column_widths[_] for _ in range(x1 + 1, x2 + 1))
            total += diff_y + diff_x

    print(total)


if __name__ == '__main__':
    main()
