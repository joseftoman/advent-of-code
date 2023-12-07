#!/usr/bin/env python

import sys

chamber_width = 7
rocks_requested = 10 ** 12


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
        level = f'{2 ** chamber_width + chamber[row]:b}'[1:].replace('0', '.').replace('1', '#')
        print(f'|{level}|')
    print('+-------+\n')


def main():
    chamber = [2 ** chamber_width - 1]
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
    rock_type_index = 0
    rock_index = 0
    jet_index = 0
    jet_resets = {}
    target = None

    first_batch = first_batch_height = cycle_len = cycles = at_repeat_height = None

    while target is None or rock_index < target:
        rock = rock_types[rock_type_index][::-1]
        rock_type_index = (rock_type_index + 1) % len(rock_types)
        row = len(chamber) + 3
        drop = 0

        while row > 0:
            if jet_index == 0 and rock_index > 0:
                jet_key = ((rock_type_index - 1) % 5, drop)
                if jet_key not in jet_resets:
                    jet_resets[jet_key] = (rock_index, len(chamber) - 1)
                else:
                    at_repeat_height = len(chamber) - 1
                    first_batch, first_batch_height = jet_resets[jet_key]
                    cycle_len = rock_index - first_batch
                    cycles = (rocks_requested - first_batch) // cycle_len
                    target = rock_index + rocks_requested - (cycles * cycle_len + first_batch)

            jet = jets[jet_index]
            jet_index = (jet_index + 1) % len(jets)

            if jet == '<' and sum(_ & 2 ** (chamber_width - 1) for _ in rock) == 0 and (row >= len(chamber) or not is_conflict(chamber, row, [_ << 1 for _ in rock])):
                rock = [_ << 1 for _ in rock]
            if jet == '>' and sum(_ & 1 for _ in rock) == 0 and (row >= len(chamber) or not is_conflict(chamber, row, [_ >> 1 for _ in rock])):
                rock = [_ >> 1 for _ in rock]

            if row > len(chamber) or not is_conflict(chamber, row - 1, rock):
                row -= 1
                drop += 1
            else:
                for _ in range(len(rock) - (len(chamber) - row)):
                    chamber.append(0)
                for index in range(len(rock)):
                    chamber[row + index] |= rock[index]
                rock_index += 1
                break

    print(cycles * (at_repeat_height - first_batch_height) + first_batch_height + (len(chamber) - 1 - at_repeat_height))


if __name__ == '__main__':
    main()
