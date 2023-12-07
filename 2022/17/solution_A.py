#!/usr/bin/env python

import sys

width = 7


def is_conflict(chamber, row, rock):
    return sum(rock[rock_row] & (0 if row + rock_row >= len(chamber) else chamber[row + rock_row]) for rock_row in range(len(rock)))


def print_chamber(chamber, row = None, rock = None):
    if rock is not None:
        chamber = chamber[:]
        for _ in range(row - len(chamber)):
            chamber.append(0)
        for _ in range(len(rock) - (len(chamber) - row)):
            chamber.append(0)
        for index in range(len(rock)):
            chamber[row + index] |= rock[index]

    for row in range(len(chamber) - 1, 0, -1):
        level = f'{2 ** width + chamber[row]:b}'[1:].replace('0', '.').replace('1', '#')
        print(f'|{level}|')
    print('+-------+\n')


def main():
    chamber = [2 ** width - 1]
    rock_types = [
        [
            (2 ** 4 - 1) << 1,  # |..####.|
        ],
        [
            2 ** 3,             # |...#...|
            (2 ** 3 - 1) << 2,  # |..###..|
            2 ** 3,             # |...#...|
        ],
        [
            2 ** 2,             # |....#..|
            2 ** 2,             # |....#..|
            (2 ** 3 - 1) << 2,  # |..###..|
        ],
        [
            2 ** 4,             # |..#....|
            2 ** 4,             # |..#....|
            2 ** 4,             # |..#....|
            2 ** 4,             # |..#....|
        ],
        [
            (2 ** 2 - 1) << 3,  # |..##...|
            (2 ** 2 - 1) << 3,  # |..##...|
        ]
    ]
    jets = sys.stdin.readline().strip()
    rock_index = 0
    jet_index = 0

    for _ in range(2022):
        rock = rock_types[rock_index][::-1]
        rock_index = (rock_index + 1) % len(rock_types)
        row = len(chamber) + 3

        while row > 0:
            jet = jets[jet_index]
            jet_index = (jet_index + 1) % len(jets)

            if jet == '<' and sum(_ & 2 ** (width - 1) for _ in rock) == 0 and (row >= len(chamber) or not is_conflict(chamber, row, [_ << 1 for _ in rock])):
                rock = [_ << 1 for _ in rock]
            if jet == '>' and sum(_ & 1 for _ in rock) == 0 and (row >= len(chamber) or not is_conflict(chamber, row, [_ >> 1 for _ in rock])):
                rock = [_ >> 1 for _ in rock]

            if row > len(chamber) or not is_conflict(chamber, row - 1, rock):
                row -= 1
            else:
                for _ in range(len(rock) - (len(chamber) - row)):
                    chamber.append(0)
                for index in range(len(rock)):
                    chamber[row + index] |= rock[index]
                break

    print(len(chamber) - 1)


if __name__ == '__main__':
    main()
